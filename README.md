
# Table of Contents
<br><br>
# Overview
I've accumulated quite a farm of Raspberry Pis over the years.  One problem is making sure 
they are operating properly.  This project is meant to verify that.
<br><br>

# Technical Description
There are two primary technologies in use here.  One is Amazon Web Services (AWS) Internet of Things 
(IoT) core services. The other is Ansible. AWS IoT Core provides the infrastructure needed to 
interact with the RPis and send SMS text messages to my cell phone when anomalies are detected. 
Ansible is an enterprise-grade tool to ssh into endpoints and gather relevant information.

The IoT device, which I'll call the "broker", is connected to AWS.  It periodically runs an Ansible 
script to connect to each RPi and gather telemetry information. As the ansible playbook runs, any anomalies are
flagged using a special message string.  The message sting is given to a python utility which then forwards it 
to AWS. AWS IoT Core causes it to be sent as a text message on my cell phone.
<br><br>

# Design Diagram
![](.README_images/overview-diagram.png)

# Sequence of Events
![](.README_images/logic-sequence-diagram.png)
1. A cron job is scheduled on the broker
2. The bash script `report.sh` is executed, which calls `ansible-playbook`
3. The ansible playbook `gather-telemetry.yaml` queries the target RPi for the first piece of telemetry data, the RPi's core temperature.
4. The RPi responds with the temperature data.
5. Subsequent queries are sent
6. Each query gets an answer
7. The ansible playbook completes
8. We grep the output to find any error conditions
9. IF errors are found, we invoke the `notify.py` script with the offending information
10. We forward that information to AWS
11. AWS creates SMS message(s) which is sent to my cell phone
12. The `notify.py` script exits
# Installation

# FAQ
Q. Why not use MQTT to connect to the different Raspberry Pis?<br>
A. That is one possible solution.  But it requires a continuously running script in each RPi. So you have to configure
each RPi individually.  My solution relies on configuring only the broker system and leaves the others untouched.
<br><br>
Q. Why not use IFTTT to send an SMS message? <br>
A. That is also a possible solution. But I am familiar with AWS and I like the robust services it offers. 
<br><br>
Q. What telemetry do you gather?<br>
A. Uptime, CPU utilization, internal temperature, disk utilization, and of course, accessibility.
<br><br>
Q. What happens if one of the telemetry values indicates a problem?<br>
A. A message is sent via AWS IoT which triggers an SMS message.