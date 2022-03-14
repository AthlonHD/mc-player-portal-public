# -*- encoding=utf8 -*-

__author__ = "athlonhd"

from aiomcrcon import Client
import asyncio
import json
import re


async def rcon(command, server):

    # Minecraft服务器地址、rcon端口、密码
    with open('config.json') as f:
        rcon_json = json.loads(f.read())
    url = rcon_json['rcon']['url']
    port1 = rcon_json['rcon']['port1']
    port2 = rcon_json['rcon']['port2']
    port3 = rcon_json['rcon']['port3']
    port4 = rcon_json['rcon']['port4']
    port_list = [port1, port2, port3, port4]
    passwd = rcon_json['rcon']['passwd']

    print(port_list[int(server)])
    client = Client(url, port_list[int(server)], passwd)
    await client.connect()
    response_raw = await client.send_cmd(command)
    await client.close()

    response = re.sub(r'\n', '', re.sub(r'§.', '', response_raw[0]))
    print(response)

    return response


if __name__ == '__main__':
    asyncio.run(rcon('money give AthlonHD 100', '0'))

