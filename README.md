### AWS Cloudfront NGINX Real IP Config file ###

If you want to use basic access list by ip (allow / deny) for restrictions your website but your server behind AWS Cloudfront
<br/>You must config NGINX to correction source ip address (from user not AWS Cloudfront) , you can follow this step.

### How to use this script
1. git clone this project
2. Run $ python3.x cloudfront-ip-range.py
3. mv cloudfront-ip-list-real-ip.conf /etc/nginx/
4. edit your virtual host config for example


server {<br/>
  listen 80;<br/>
  ...<br/>
  server_name admin.mycompany.co.th;<br/>
  include /etc/nginx/cloudfront-ip-list-real-ip.conf ### Include this config file<br/>
  <br/>
  allow 1.2.3.0/24; ### Your whitelist IP Address or Subnet<br/>
  deny all;<br/>
  ...<br/>
  ...<br/>
}<br/>

