# -*- encoding=utf8 -*-

__author__ = "athlonhd"

from flask import Flask, request
import json
from wsgiref.simple_server import make_server
import os


app = Flask(__name__)


@app.route('/say', methods=['POST'])
def say():
    """
    {
        'say': ''
    }
    :return:
    """
    response = {'code': '0', 'message': '执行成功', 'data': ''}
    data = json.loads(request.get_data())

    if data['say'] == '':
        response['code'] = '100'
        response['message'] = '请输入执行内容！'
        return json.dumps(response)
    else:
        rcon = 'mcrcon -H % s -p % s "say % s"' % (url, passw, data['say'])
        print(rcon)
        os.system(rcon)
        return json.dumps(response)


@app.route('/cmd', methods=['POST'])
def cmd():
    """
    {
        'cmd': ''，
        'server: ''
    }
    :return:
    """
    response = {'code': '0', 'message': '执行成功', 'data': ''}
    data = json.loads(request.get_data())
    port = port_list[int(data['server'])]

    if data['cmd'] == '':
        response['code'] = '100'
        response['message'] = '请输入执行内容！'
        return json.dumps(response)
    else:
        rcon = 'mcrcon -H % s -P % s -p % s "% s"' % (url, port, passw, data['cmd'])
        print(rcon)
        # os.system(rcon)
        result = os.popen(rcon).read()
        print(result.encode('utf-8'))
        response['message'] = result
        return json.dumps(response)


httpd = make_server('', 11000, app)
print('Serving HTTP on port 11000...')
httpd.serve_forever()


if __name__ == '__main__':
    app.run()
