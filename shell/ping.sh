#!/bin/bash
#
# We call ansible and grep the output for notable messages. Specifically, we are looking for telemetry errors and
# fatal ansible-related errors. In either case, we then call the notify.py script to forward that info to AWS where
# it can be converted to a text message and sent to my cell phone.
#

cd "${HOME}/raspberry-pi-iot-monitor/ansible"
ansible all -m ping
