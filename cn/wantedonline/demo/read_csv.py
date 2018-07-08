import csv
import time
from wxpy import *


def read_info():
    f = open('./sample.csv', 'r', encoding='utf-8')
    reader = csv.DictReader(f)
    return [info for info in reader]


def make_msg(raw_info):
    t = '{n} 同学-请于{t}时间参加{s}课程，地址{a}。收到不要回复，谢谢'
    return [
        t.format(n = info['姓名'],
                 t = info['上课时间'],
                 s = info['课程'],
                 a = info['上课地址'])
        for info in raw_info]


def send(msg):
    bot = Bot()
    friend = bot.friends().search('沈俊林')
    if len(friend) == 1:
        for m in msg:
            friend[0].send(m)
            time.sleep(3)




raw_info = read_info()
send(make_msg(raw_info))