# Telegram webhook for Prometheus alertmanager

## Description

Simple python service for send notifications from [Prometheus Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) to Telegram.

## Usage

First, create bot and get token, ask [@botfather](https://t.me/botfather) about it.

Add one or several webhook receivers to your `alertmanager.yml`:

```yaml
# ...
receivers:
  - name: 'my_telegram'
    webhook_configs:
    - send_resolved: true
      url: http://127.0.0.1:5000/send/<your_telegram_id>

  - name: 'some_other_telegram_chat'
    webhook_configs:
    - send_resolved: true
      url: http://127.0.0.1:5000/send/<other_telegram_id>
# ...
```

see [Prometheus docs](https://prometheus.io/docs/alerting/latest/configuration/) for details.

Then run app with docker:

```bash
docker run -d -e TELEGRAM_TOKEN=<YOU_BOT_TOKEN> -p 5000:5000 kargina/prometheus-webhook-telegram:1.0
```

or from shell:

```bash
git clone https://github.com/Kargina/prometheus-webhook-telegram
cd prometheus-webhook-telegram
pip install -r requirements.txt
TELEGRAM_TOKEN=<YOU_BOT_TOKEN> python send_alert.py
```

## Configuration with env variables

`LISTEN_PORT`, port for bind, 5000 by default

`TELEGRAM_TOKEN`, telegram bot token for send notifications

## Build docker image

```bash
git clone https://github.com/Kargina/prometheus-webhook-telegram
cd prometheus-webhook-telegram
docker build .
```
