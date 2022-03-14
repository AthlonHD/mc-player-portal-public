# -*- encoding=utf8 -*-

__author__ = "athlonhd"

from flask import Flask, request
import json
from db_progress import *
from wsgiref.simple_server import make_server
from rcon import rcon
import asyncio
import lottery
import re

app = Flask(__name__)
db = DbConn()


@app.route('/checkid', methods=['POST'])
def check_id():
    """
    {
        'game_id': ''
    }
    :return:
    """
    response = {'code': '0', 'message': 'ID无重复可以使用！', 'data': ''}
    data = json.loads(request.get_data())
    result = db.check_id(data['game_id'])

    if not result:
        return json.dumps(response)
    else:
        response['code'] = '100'
        response['message'] = '此ID已经被使用！'
        return json.dumps(response)


@app.route('/createid', methods=['POST'])
def create_id():
    """
    {
        'game_id': '',
        'phone_num': '',
        'sub_id': ''
    }

    :return:
    """
    response = {'code': '0', 'message': '绑定成功！', 'data': ''}
    data = json.loads(request.get_data())
    validate_result = db.check_id(data['game_id'])
    print(validate_result)

    # 验证用户名是否重复
    if not validate_result:
        phone_result = db.check_phone(data['phone_num'])
        # 验证手机号是否存在
        if not phone_result:
            result = db.create_id(data['game_id'], data['phone_num'], data['sub_id'])
            if not result:
                return json.dumps(response)
        # 手机号已经存在
        else:
            response['code'] = '200'
            response['message'] = '此手机号已绑定白名单！'
            return json.dumps(response)
    # id已被注册
    else:
        response['code'] = '100'
        response['message'] = '此ID已经被使用！'
        return json.dumps(response)


@app.route('/searchid', methods=['POST'])
def search_id():
    """
    {
        'phone_num': ''
    }
    :return:
    """

    response = {'code': '100', 'message': '当前账号下无绑定白名单ID！', 'data': ''}
    data = json.loads(request.get_data())
    result = db.search_id(data['phone_num'])
    print(result)

    if not result:
        return json.dumps(response)
    else:
        game_id = result[0][0]
        response['code'] = '0'
        response['message'] = '成功查询到当前账号绑定ID！'
        response['data'] = game_id
        return json.dumps(response)


@app.route('/dailysign', methods=['POST'])
def daily_sign():
    """
    {
        'phone_num': '',
        'server': ''
    }
    :return:
    """
    response = {'code': '0', 'message': '签到成功！奖励已发放至游戏账户！', 'data': ''}
    data = json.loads(request.get_data())
    # 查询今天是否签到过
    result = db.search_daily_sign_record(data['phone_num'])
    print(result)

    if not result:
        db.daily_sign_record(data['phone_num'])

        # 查询对应游戏id
        result = db.search_id(data['phone_num'])
        print(result)
        try:
            game_id = result[0][0]
        except IndexError:
            response['code'] = '300'
            response['message'] = '未能找到玩家id！'
            return json.dumps(response)

        # 执行rcon
        command = 'money give % s 200' % game_id
        result = asyncio.run(rcon(command, server=data['server']))
        response['data'] = result
        return json.dumps(response)

    else:
        response['code'] = '100'
        response['message'] = '今天已经签到过啦~明天再来吧！'
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

    if data['cmd'] == '':
        response['code'] = '100'
        response['message'] = '请输入执行内容！'
        return json.dumps(response)
    else:
        result = asyncio.run(rcon(data['cmd'], server=data['server']))
        response['data'] = result
        return json.dumps(response)


@app.route('/checkmoney', methods=['POST'])
def check_money():
    """
    {
        'phone_num': ''，
        'server: ''
    }
    :return:
    """
    response = {'code': '100', 'message': '未能查询到相关用户！', 'data': ''}
    data = json.loads(request.get_data())

    # 查询当前账号id
    try:
        game_id = db.search_id(data['phone_num'])[0][0]
    except IndexError:
        return json.dumps(response)

    command = 'money % s' % game_id
    result = asyncio.run(rcon(command, server=data['server']))
    response['code'] = '0'
    response['message'] = '查询成功！'
    response['data'] = result
    return json.dumps(response)


@app.route('/checkadmin', methods=['POST'])
def check_admin():
    """
    {
        'sub_id': ''
    }
    :return:
    """
    response = {'code': '0', 'message': '当前账号是管理员账号', 'data':''}
    data = json.loads(request.get_data())

    # 查询当前账号是否属于管理员账号
    result = db.check_admin(data['sub_id'])

    try:
        if result:
            return json.dumps(response)
        else:
            response['code'] = '100'
            response['message'] = '当前账号不属于管理账号！'
            return json.dumps(response)
    except IndexError:
        response['code'] = '100'
        response['message'] = '当前账号不属于管理账号！'
        return json.dumps(response)


@app.route('/lottery.bindserver', methods=['POST'])
def lottery_bind_server():
    """
    {
        'sub_id': '',
        'bind_server': ''
    }
    :return:
    """
    response = {'code': '0', 'message': '绑定成功！', 'data': ''}
    data = json.loads(request.get_data())

    result = db.search_lottery_bind_server(data['sub_id'])
    try:
        if result[0][0]:
            response['code'] = '100'
            response['message'] = '您已绑定过区服，请勿重复绑定！'
            return json.dumps(response)

    except IndexError:
        db.create_lottery_bind_server(data['sub_id'], data['bind_server'])

        return json.dumps(response)


@app.route('/lottery.checkmoney', methods=['POST'])
def lottery_check_money():
    """
    {
        'sub_id': ''
    }
    :return:
    """
    response = {'code': '100', 'message': '请先绑定账号！', 'data': ''}
    data = json.loads(request.get_data())

    result = db.search_lottery_bind_server(data['sub_id'])
    try:
        if result[0][0]:
            game_id = db.search_id_by_sub_id(data['sub_id'])[0][0]
            server = db.search_lottery_bind_server(data['sub_id'])[0][0]

            command = 'money % s' % game_id
            result = asyncio.run(rcon(command, server))
            # AthlonHD 的金钱: 12,032.57铜板

            response['code'] = '0'
            response['message'] = '查询成功！'
            response['data'] = result
            return json.dumps(response)
    except IndexError:
        return json.dumps(response)


@app.route('/lottery.single', methods=['POST'])
def lottery_single():
    """
    {
        'sub_id': ''
    }
    :return:
    """
    response = {'code': '100', 'message': '请先绑定账号！', 'data': ''}
    data = json.loads(request.get_data())

    result = db.search_lottery_bind_server(data['sub_id'])

    try:
        if result[0][0]:
            game_id = db.search_id_by_sub_id(data['sub_id'])[0][0]
            server = db.search_lottery_bind_server(data['sub_id'])[0][0]

            command = 'money % s' % game_id
            result = asyncio.run(rcon(command, server))
            re_result = re.findall(r": \d+.+", result)[0].replace(': ', '').replace(',', '').replace('铜板', '')
            print(re_result)
            money = re.sub(r"\.\d+", '', re_result)
            print(money)

            if int(money) < 100:
                response['code'] = '200'
                response['message'] = '余额不足！'
                return json.dumps(response)
            else:
                command = 'money take % s 100' % game_id
                result = asyncio.run(rcon(command, server))
                response['code'] = '0'
                response['message'] = '支付成功'

                lottery_result = lottery.lottery()
                response['data'] = lottery_result
                db.save_lottery_record(data['sub_id'], lottery_result)
                return json.dumps(response)
    except IndexError:
        return json.dumps(response)


@app.route('/lottery.queryreward', methods=['POST'])
def lottery_query_reward():
    """
    {
        'sub_id': ''
    }
    :return:
    """
    response = {'code': '100', 'message': '未查询到相关数据！', 'data': ''}
    data = json.loads(request.get_data())

    reward_list = db.query_lottery_reward(data['sub_id'])

    try:
        if reward_list[0][0]:
            reward = []
            for i in reward_list:
                reward_dict = {'reward': i[0]}
                reward.append(reward_dict)

            print(reward)

            response['code'] = '0'
            response['message'] = '查询成功！'
            response['data'] = reward
            return json.dumps(response)
    except IndexError:
        return json.dumps(response)


@app.route('/lottery.pushreward', methods=['POST'])
def lottery_push_reward():
    """
    {
        'sub_id': '',
        'reward': ''
    }
    :return:
    """
    response = {'code': '0', 'message': '发放成功！', 'data': ''}
    data = json.loads(request.get_data())

    db.drop_lottery_reward_record(data['sub_id'], data['reward'])

    game_id = db.search_id_by_sub_id(data['sub_id'])[0][0]
    server = db.search_lottery_bind_server(data['sub_id'])[0][0]

    result = lottery.push_reward(game_id, data['reward'], server)

    response['data'] = result

    return json.dumps(response)


httpd = make_server('', 23333, app)
print('Serving HTTP on port 23333...')
httpd.serve_forever()

# httpd = make_server('', 23334, app)
# print('Serving HTTP on port 23334...')
# httpd.serve_forever()


if __name__ == '__main__':
    app.run()
