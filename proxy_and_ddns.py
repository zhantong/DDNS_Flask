from flask import Flask,request
import urllib.parse
import re
import os
import Ddns
application=Flask(__name__)
@application.route('/ipv6')
def ipv6():
	code=request.args['code']
	if code!='80':
		return 'Bad Request'
	ip=request.remote_addr
	d=Ddns.Ddns(ip)

if __name__=='__main__':
	application.debug=True
	application.run()