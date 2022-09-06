The contents of this directory is responsible for gathering the telemetry data from the RPi endpoints.

The primary tool used is [Ansible](https://docs.ansible.com/ansible/latest/index.html), which is a very popular IT 
configuration management platform. Ansible uses secure shell (SSH) to remotely connect to endpoints. In our case, 
we are simply using Ansible to gather data rather that configure the endpoints.

# Directory Inventory

- `ansible.cfg` - This tells Ansible where things like the `hosts` file lives.  You shouldn't have to modify it.
- `gather-telemetry.yaml` - This is the actual script which gathers information from the RPis. You may need to modify the variables in it to match your requirements.
- `sample_hosts` - This is a sample of a hosts file which Ansible uses to connect to the RPi endpoints. You will need to copy it to a `hosts` file and add your RPi names.
- `plugins` - This is a directory containing a simple python script. The script, called a "plugin", is used by ansible to convert timestamps to elapsed days. You will NOT need to modify this.

