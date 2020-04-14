FROM python:3.8
LABEL maintainer="Ksenia Kargina <kargina.ks@gmail.com>"
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python", "send_alert.py" ]
