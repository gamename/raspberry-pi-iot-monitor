#!/bin/bash

python3 "${HOME}/raspberry-pi-iot-monitor/iot/notify.py" \
  --endpoint a3u37c52vq0b6j-ats.iot.us-east-1.amazonaws.com \
  --rootCA "${HOME}/root-CA.crt" \
  --cert "${HOME}/pi-monitor.cert.pem" \
  --key "${HOME}/pi-monitor.private.key" \
  --topic "tns/bot/pi-monitor" \
  --message "MSG003: TEST message"