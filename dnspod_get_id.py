import urllib.request
import urllib.parse
import json

login_email = 'xxx'
login_password = 'xxx'


def get_json(url, data):
    con = urllib.request.urlopen(
        url, data=urllib.parse.urlencode(data).encode())
    return json.loads(con.read().decode())


def get_domain_id():
    url = 'https://dnsapi.cn/Domain.List'
    data = {
        'login_email': login_email,
        'login_password': login_password,
        'format': 'json'
    }
    json = get_json(url, data)
    for domain in json['domains']:
        print('domain name:%s\tdomain id:%s' % (domain['name'], domain['id']))


def get_record_id(domain_id):
    url = 'https://dnsapi.cn/Record.List'
    data = {
        'login_email': login_email,
        'login_password': login_password,
        'format': 'json',
        'domain_id': domain_id
    }
    json = get_json(url, data)
    print('domain name:%s\tdomain id:%s' %
          (json['domain']['name'], json['domain']['id']))
    for record in json['records']:
        print('record name:%s\trecord type:%s\trecord id:%s' %
              (record['name'], record['type'], record['id']))


if __name__ == '__main__':
    get_domain_id()
