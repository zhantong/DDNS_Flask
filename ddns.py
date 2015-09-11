from flask import Flask,jsonify,request
import urllib.parse
import re
import os
application=Flask(__name__)
@application.route('/ipv6')
def ipv6():
	ip=request.remote_addr
	url='https://dnsapi.cn/Record.Modify'
	info={
		'login_email':'102517642@qq.com',
		'login_password':'cipherpanzer',
		'format':'json',
		'domain_id':'23606146',
		'record_id':'116841773',
		'record_line':'默认',
		'sub_domain':'test',
		'record_type':'AAAA',
		'value':ip
		}
	with open('/etc/nginx/sites-available/default','r') as f:
		s=f.read()
	r=re.compile(r'http://\[(.*?)\]; \# for raspberry pi')
	s=s.replace(r.findall(s)[0],ip)
	with open('/etc/nginx/sites-available/default','w') as f:
		f.write(s)
	os.popen('service nginx restart')
	#data=urllib.parse.urlencode(info).encode()
	#t=urllib.request.urlopen(url,data=data)
	#return t.read().decode('utf-8')
	#return s
	return s

if __name__=='__main__':
	application.debug=True
	application.run()