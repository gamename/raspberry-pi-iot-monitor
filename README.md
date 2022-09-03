
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
script to connect to each RPi and gather telemetry information. Ansible gathers data and calls it 
'facts' which are really just JSON files. The files are kept in a subdirectory.  After the facts 
are gathered, we use a python script to post-process the information and flag issues.  Any flagged 
issues are forwarded to AWS to trigger SMS messaging.
<br><br>

# Design Diagram

# FAQ
Q. Why not use MQTT to connect to the different Raspberry Pis?<br>
<br><br>
Q. Why not use IFTTT to send an SMS message? <br>
<br><br>
Q. What telemetry do you gather?<br>
A. Uptime, CPU utilization, internal temperature, disk utilization, and of course, accessibility.
<br><br>
Q. What happens if one of the telemetry values indicates a problem?<br>
A. A message is sent via AWS IoT which triggers an SMS message.