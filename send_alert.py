from flask import Flask, request, abort
import requests
import logging
import os

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.ERROR)

app = Flask(__name__)


@app.route('/send/<chat_id>', methods=['POST'])
def send_data_telegram(chat_id):

    try:
        chat_id = int(chat_id)
    except ValueError:
        abort(404)

    try:
        all_alerts = request.get_json()
    except Exception as e:
        log.error(f"Can't get json: {e}")
        return f"Can't get json: {e}", 400

    for alert in all_alerts['alerts']:

        if alert['status'] == 'firing':
            message = '🔥\n'
        if alert['status'] == 'resolved':
            message = '✅\n'

        message += f"{alert['labels']['alertname']}: {alert['labels']['instance']}\n"
        message += f"Description: {alert['annotations']['description']}"

        data = {
            'chat_id': chat_id,
            'text': message
        }

        try:
            request_result = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data=data)
        except requests.exceptions.RequestException as e:
            log.error(f"Can't send message: {e}")
            return f"Can't send message: {e}"

    return "Message was send"


if __name__ == '__main__':

    token = os.getenv("TELEGRAM_TOKEN", "")
    if not token:
        log.error("Env var TELEGRAM_TOKEN must be set, exit")
        exit(1)
    app.run()
