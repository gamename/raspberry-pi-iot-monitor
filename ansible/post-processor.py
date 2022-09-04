"""
This takes facts gathered via ansible and puts certain fields into a csv output file
"""

import argparse
import csv
import glob
import json

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_json_dir", dest='input_json', required=True, help="Input json files directory")
ap.add_argument("-o", "--output_csv", dest='output_csv', required=True, help="Output CSV file")
args = vars(ap.parse_args())

files = "{0}/*".format(args['input_json'])
json_files = glob.glob(files)

hosts = []
for file in sorted(json_files):
    host_dict = {}
    with open(file) as f:
        data = json.load(f)
        host_dict['host_name'] = data['ansible_nodename']
        host_dict['boot_date'] = data['boot_date']
        host_dict['core_temperature'] = data['core_temperature']
        host_dict['cpu_average'] = data['cpu_average']
        host_dict['disk_utilization'] = data['disk_utilization']
        hosts.append(host_dict)


with open(args['output_csv'], mode='w') as csv_file:
    fieldnames = ['host_name', 'boot_date', 'core_temperature', 'cpu_average', 'disk_utilization']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for host in hosts:
        writer.writerow(
            {
                'hostname': str(host['hostname']).split('.')[0],
                'boot_date': host['boot_date'],
                'core_temperature': host['core_temperature'],
                'cpu_average': host['cpu_average'],
                'disk_utilization': host['disk_utilization'],
            }
        )
