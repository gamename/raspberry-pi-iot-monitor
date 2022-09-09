#!/bin/bash
source $HOME/.ssh/agent-environment
cd "${HOME}/raspberry-pi-iot-monitor/ansible"
ansible-playbook gather-telemetry.yaml -v

