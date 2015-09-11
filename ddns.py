from flask import Flask,request
import urllib.parse
import re
import os
application=Flask(__name__)
@application.route('/ipv6')
def ipv6():
	code=request.args['code']
	if code!='80':
		return 'Bad Request'
	ip=request.remote_addr
	with open('/etc/nginx/sites-available/default','r') as f:
		s=f.read()
	r=re.compile(r'http://\[(.*?)\]; \# for raspberry pi')
	s=s.replace(r.findall(s)[0],ip)
	with open('/etc/nginx/sites-available/default','w') as f:
		f.write(s)
	os.popen('service nginx restart')
	url='https://dnsapi.cn/Record.Modify'
	info={
		'login_email':'xxx',
		'login_password':'xxx',
		'format':'json',
		'domain_id':'23606146',
		'record_id':'116841773',
		'record_line':'默认',
		'sub_domain':'test',
		'record_type':'AAAA',
		'value':ip
		}

	data=urllib.parse.urlencode(info).encode()
	t=urllib.request.urlopen(url,data=data)
	return t.read().decode('utf-8')
	return s

if __name__=='__main__':
	application.debug=True
	application.run()