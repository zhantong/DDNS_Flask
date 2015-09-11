import urllib.request
import os
import re


class Ddns():

    def update_nginx_config(self, ip):
        with open('/etc/nginx/sites-available/default', 'r') as f:
            s = f.read()
        r = re.compile(r'http://\[(.*?)\]; \# for raspberry pi')
        s = s.replace(r.findall(s)[0], ip)
        with open('/etc/nginx/sites-available/default', 'w') as f:
            f.write(s)
        os.popen('service nginx restart')

    def update_dnspod(self, ip):
        url = 'https://dnsapi.cn/Record.Modify'
        info = {
            'login_email': 'xxx',
            'login_password': 'xxx',
            'format': 'json',
            'domain_id': '23606146',
            'record_id': '116841773',
            'record_line': '默认',
            'sub_domain': 'test',
            'record_type': 'AAAA',
            'value': ip
        }

        data = urllib.parse.urlencode(info).encode()
        t = urllib.request.urlopen(url, data=data)
        return t.read().decode('utf-8')

    def update(self, ip):
        t=self.update_dnspod(ip)
        self.update_nginx_config(ip)
        return t
