#!/usr/bin/env python

#### NGINX CONF AWS CLOUDFRONT IP LIST ####
## Payungsak Klinchampa
## Network / Cloud Engineer 
## PaOCLOUD ACADEMY 
## pao@paocloud.in.th , +66-937738265

import requests, json

d = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').text
l = json.loads(d)

f = open("cloudfront-ip-list-real-ip.conf","w+")

for ip_range in [x['ip_prefix'] for x in l['prefixes'] if x['service'] =='CLOUDFRONT' ]:
        f.write("set_real_ip_from " + ip_range + ";" + "\r\n")
### Private IP ###
f.write ("set_real_ip_from 10.0.0.0/8;\r\n")
f.write ("set_real_ip_from 172.16.0.0/12;\r\n")
f.write ("set_real_ip_from 192.168.0.0/16;\r\n")

### Set Real IP from X-Forwarded-For HTTP Header ###
f.write ("real_ip_header X-Forwarded-For;\r\n")
### Enable REAL IP Recursive ###
f.write ("real_ip_recursive on;")

print ("Generate NGINX CONFIG FILE SUCCESSFULLY !!")
### END ###
