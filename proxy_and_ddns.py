from flask import Flask, request
import Ddns
application = Flask(__name__)


@application.route('/ipv6')
def ipv6():
    code = request.args['code']
    if code != '80':
        return 'Bad Request'
    ip = request.remote_addr
    d = Ddns.Ddns()
    t=d.update(ip)
    return t

if __name__ == '__main__':
    application.debug = True
    application.run()
