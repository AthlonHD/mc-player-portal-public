# -*- encoding=utf8 -*-

__author__ = "athlonhd"

import random
from rcon import rcon
import asyncio


wards_list = [
    '铅粉x128', '镁x128', '铁粉x128', '金粉x128', '铜粉x128', '锌粉x128', '银粉x128', '铝粉x128',
    '铜板￥50', '附魔书：普通x1', '铜板￥100', '铜板￥200', '附魔书：稀有x1', '金锭：24克拉',
    '称号：幸运星', '附魔书：史诗x1', '附魔书：传说x1', '铜板￥500', '龙蛋x1', '加强水力发电机x1',
    '经验+22888', '铜板￥1000', '下界之星x64', '铜板￥5000', '黑金刚石x64', '海洋之星',
    '起泡锭x64', '强化合金x64', '虚空微粒发生器x1', '铜板￥10000', '称号币$1', '天堂陨落长弓x1',
    '无尽圆石发生器x1', '称号币$5', '无尽鞘翅核心x1', '无尽奇点x1'
]

wards_weight = [
    35, 34, 33, 32, 31, 30, 29, 28,
    27, 26, 25, 24, 23, 22,
    21, 20, 19, 18, 17, 16,
    15, 14, 13, 12, 11, 10,
    9, 8, 7, 6, 5, 4,
    3, 3, 2, 1
]

wards_cmd = {
    '铅粉x128': 'sf give % s LEAD_DUST 128',
    '镁x128': 'sf give % s MAGNESIUM_DUST 128',
    '铁粉x128': 'sf give % s IRON_DUST 128',
    '金粉x128': 'sf give % s GOLD_DUST 128',
    '铜粉x128': 'sf give % s COPPER_DUST 128',
    '锌粉x128': 'sf give % s ZINC_DUST 128',
    '银粉x128': 'sf give % s SILVER_DUST 128',
    '铝粉x128': 'sf give % s ALUMINUM_DUST 128',
    '铜板￥50': 'money give % s 50',
    '附魔书：普通x1': 'ecoenchants giverandombook % s common 1',
    '铜板￥100': 'money give % s 100',
    '铜板￥200': 'money give % s 200',
    '附魔书：稀有x1': 'ecoenchants giverandombook % s rare 1',
    '金锭：24克拉': 'sf give % s GOLD_24K 1',
    '称号：幸运星': 'kit luckystar % s',
    '附魔书：史诗x1': 'ecoenchants giverandombook % s epic 1',
    '附魔书：传说x1': 'ecoenchants giverandombook % s legendary 1',
    '铜板￥500': 'money give % s 500',
    '龙蛋x1': 'give % s dragonegg 1',
    '加强水力发电机x1': 'sf give % s REINFORCED_HYDRO_GENERATOR 1',
    '经验+22888': 'exp give % s 22888',
    '铜板￥1000': 'money give % s 1000',
    '下界之星x64': 'give % s netherstar 64',
    '铜板￥5000': 'money give % s 5000',
    '黑金刚石x64': 'sf give % s CARBONADO 64',
    '海洋之星': 'give % s heartofthesea 1',
    '起泡锭x64': 'sf give % s BLISTERING_INGOT_3 64',
    '强化合金x64': 'sf give % s REINFORCED_ALLOY_INGOT 64',
    '虚空微粒发生器x1': 'sf give % s VOID_HARVESTER 1',
    '铜板￥10000': 'money give % s 10000',
    '称号币$1': 'plt addCoin % s 1',
    '天堂陨落长弓x1': 'sf give % s INFINITY_BOW 1',
    '无尽圆石发生器x1': 'sf give % s INFINITY_COBBLE_GEN 1',
    '称号币$5': 'plt addCoin % s 5',
    '无尽鞘翅核心x1': 'sf give % s INFINITY_MATRIX 1',
    '无尽奇点x1': 'sf give % s INFINITY_SINGULARITY 1'
}


def weight_choice(weight):
    """
    :param weight: list对应的权重序列
    :return:
    """
    t = random.randint(0, sum(weight) - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return i


def lottery():
    """
    抽奖
    :return:
    """
    return wards_list[weight_choice(wards_weight)]


def push_reward(game_id, reward, server):
    """
    发放奖品
    :param game_id:
    :param reward:
    :param server:
    :return:
    """

    command = wards_cmd[reward] % game_id
    print(command)

    result = asyncio.run(rcon(command, server))
    return result


if __name__ == "__main__":
    # print(lottery())
    push_reward('AthlonHD', '铜板￥100', '0')
