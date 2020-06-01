### AWS Cloudfront NGINX Real IP Config file ###

#### If you want to use basic access list by ip (allow / deny) for restrictions your website but your server behide AWS Cloudfront
You must config NGINX to correction source ip address (from user not AWS Cloudfront) , you can fllow this step.

### How to use this script
1. git clone this project
2. Run $ python3.x cloudfront-ip-range.py
3. mv cloudfront-ip-list-real-ip.conf /etc/nginx/
4. edit your virtual host config for example

server {
  listen 80;
  ...
  server_name admin.mycompany.co.th;
  include /etc/nginx/cloudfront-ip-list-real-ip.conf ### Include this config file
  
  allow 1.2.3.0/24; ### Your whitelist IP Address or Subnet
  deny all;
  ...
  ...
}
  
