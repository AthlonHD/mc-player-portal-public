# -*- encoding=utf8 -*-

__author__ = "athlonhd"

import time
import pymysql
import json


def t_to_l(t):
    """
    tuple转list
    :param t: tuple
    :return:
    """

    result = []
    for i in t:
        result.append(list(i))

    return result


def get_time():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


class DbConn:

    def __init__(self):
        # 读取配置
        with open('config.json', 'r') as f:
            config_info = json.loads(f.read())
        jdbc = config_info['jdbc']
        host = jdbc['host']
        port = jdbc['port']
        user = jdbc['user']
        passwd = jdbc['passwd']
        db_name = jdbc['db']

        self.db = pymysql.connect(host=host, port=port,
                                  user=user, passwd=passwd, db=db_name, charset='utf8')

        self.cursor = self.db.cursor()

    def db_check(self):
        self.db.ping(reconnect=True)

    def check_id(self, game_id):
        """
        玩家id查重
        game_id: 玩家游戏名称
        :return:
        """
        self.db_check()

        sql = "select game_id from mc.mc_whitelist where game_id = '% s';" % game_id
        print(sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return t_to_l(result)

    def check_phone(self, phone_num):
        """
        手机号查重
        :param phone_num:
        :return:
        """
        self.db_check()

        sql = "select phone_num from mc.mc_whitelist where phone_num = '% s';" % phone_num
        print(sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return t_to_l(result)

    def create_id(self, game_id, phone_num, sub_id):
        """
        创建id
        :param game_id:
        :param phone_num:
        :param sub_id:
        :return:
        """
        self.db_check()

        sql = "INSERT INTO mc.mc_whitelist (game_id, phone_num, sub_id) VALUES ( '% s', '% s', '% s')" \
              % (game_id, phone_num, sub_id)
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()

        sql_2 = "INSERT INTO mc.game_id (username) VALUES ( '% s')" % game_id
        print(sql_2)
        self.cursor.execute(sql_2)
        self.db.commit()

        result = self.cursor.fetchall()
        return t_to_l(result)

    def search_id(self, phone_num):
        """
        通过手机号查找当前账号现有id
        :param phone_num:
        :return:
        """
        self.db_check()

        sql = "SELECT game_id FROM mc.mc_whitelist WHERE phone_num = '% s'" % phone_num
        print(sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return t_to_l(result)

    def search_id_by_sub_id(self, sub_id):
        """
        通过sub_id查找当前账号现有id
        :param sub_id:
        :return:
        """
        self.db_check()

        sql = "SELECT game_id FROM mc.mc_whitelist WHERE sub_id = '% s'" % sub_id
        print(sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return t_to_l(result)

    def daily_sign_record(self, phone_num):
        """
        每日签到记录
        :param phone_num:
        :return:
        """
        self.db_check()

        date = get_time()
        sql = "INSERT INTO mc.daily_sign (phone_num, sign_date) VALUES ( '% s', '% s')" % (phone_num, date)
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()

        result = self.cursor.fetchall()
        return t_to_l(result)

    def search_daily_sign_record(self, phone_num):
        """
        查找当前账号是否有资格签到
        :param phone_num:
        :return:
        """
        self.db_check()

        date = get_time()
        sql = "SELECT phone_num FROM mc.daily_sign WHERE phone_num = '% s' and sign_date = '% s'" % (phone_num, date)
        print(sql)
        self.cursor.execute(sql)

        result = self.cursor.fetchall()
        return t_to_l(result)

    def check_admin(self, sub_id):
        """
        查找当前账号是否属于admin
        :param sub_id:
        :return:
        """
        self.db_check()

        sql = "SELECT admin_sub_id FROM mc.portal_admin WHERE admin_sub_id = '% s'" % sub_id
        print(sql)
        self.cursor.execute(sql)

        result = self.cursor.fetchall()
        return t_to_l(result)

    def check_sub_id(self, phone_num):
        """
        通过手机号查找当前账号sub_id
        :param phone_num:
        :return:
        """
        self.db_check()

        sql = "SELECT sub_id FROM mc.mc_whitelist WHERE phone_num = '% s'" % phone_num
        print(sql)
        self.cursor.execute(sql)

        result = self.cursor.fetchall()
        return t_to_l(result)

    def create_lottery_bind_server(self, sub_id, bind_server):
        """
        添加抽奖绑定区服
        :param sub_id:
        :param bind_server: 0一区；1二区；2三区；3四区
        :return:
        """
        self.db_check()

        sql = "INSERT INTO mc.lottery_bind_server_new (sub_id, bind_server) VALUES ('% s', '% s')" \
              % (sub_id, bind_server)
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()

        result = self.cursor.fetchall()
        return t_to_l(result)

    def search_lottery_bind_server(self, sub_id):
        """
        查询抽奖绑定区服
        :param sub_id:
        :return:
        """
        self.db_check()

        sql = "SELECT bind_server FROM mc.lottery_bind_server_new WHERE sub_id = '% s'" % sub_id
        print(sql)
        self.cursor.execute(sql)

        result = self.cursor.fetchall()
        return t_to_l(result)

    def save_lottery_record(self, sub_id, reward):
        """
        写入中奖纪录
        :param sub_id:
        :param reward:
        :return:
        """
        self.db_check()

        sql = "INSERT INTO mc.lottery_record (sub_id, reward, is_delivered) VALUES ('% s', '% s', 0)" % (sub_id, reward)
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()

        result = self.cursor.fetchall()
        return t_to_l(result)

    def query_lottery_reward(self, sub_id):
        """
        查询中奖纪录
        :param sub_id:
        :return:
        """
        self.db_check()

        sql = "SELECT reward FROM mc.lottery_record WHERE sub_id = '%s' and is_delivered = 0" % sub_id
        print(sql)
        self.cursor.execute(sql)

        result = self.cursor.fetchall()
        return t_to_l(result)

    def drop_lottery_reward_record(self, sub_id, reward):
        """
        发送奖品后修改纪录
        :param sub_id:
        :param reward:
        :return:
        """
        self.db_check()

        sql1 = "SELECT min(id) FROM mc.lottery_record WHERE sub_id = '% s' and reward = '% s' and is_delivered = 0;" \
               % (sub_id, reward)
        print(sql1)
        self.cursor.execute(sql1)
        min_id = t_to_l(self.cursor.fetchall())[0][0]

        sql2 = "UPDATE mc.lottery_record SET is_delivered = 1 WHERE id = % s;" % min_id
        print(sql2)
        self.cursor.execute(sql2)
        self.db.commit()

        result = self.cursor.fetchall()
        return t_to_l(result)


if __name__ == '__main__':
    db = DbConn()

