#!/bin/bash
#
# We call ansible and grep the output for notable messages. Specifically, we are looking for telemetry errors and
# fatal ansible-related errors. In either case, we then call the notify.py script to forward that info to AWS where
# it can be converted to a text message and sent to my cell phone.
#

cd "${HOME}/raspberry-pi-iot-monitor/ansible"
gather_out=$(ansible-playbook gather-telemetry.yaml |
             grep --only-matching --extended-regexp "RPIERROR:.*$|fatal:.[^=]*" )

if [ -z "${gather_out}" ]; then
  python3 "${HOME}/raspberry-pi-iot-monitor/iot/notify.py" \
    --endpoint a3u37c52vq0b6j-ats.iot.us-east-1.amazonaws.com \
    --rootCA "${HOME}/root-CA.crt" \
    --cert "${HOME}/pi-monitor.cert.pem" \
    --key "${HOME}/pi-monitor.private.key" \
    --topic "tns/bot/pi-monitor" \
    --message "MSG003: Fivers"
else
  echo "${gather_out}" | while read line; do
    python3 "${HOME}/raspberry-pi-iot-monitor/iot/notify.py" \
      --endpoint a3u37c52vq0b6j-ats.iot.us-east-1.amazonaws.com \
      --rootCA "${HOME}/root-CA.crt" \
      --cert "${HOME}/pi-monitor.cert.pem" \
      --key "${HOME}/pi-monitor.private.key" \
      --topic "tns/bot/pi-monitor" \
      --message "MSG003: ${line}"
  done
fi

