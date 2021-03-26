# coding:gbk
import time
import pandas as pd
from shipping.evergreen.wanhai import wanhai
from shipping.evergreen.hapag_lloyd import hapag_lloyd
from shipping.evergreen.ecommOneLine import ecommOneLine
from shipping.evergreen.cma_cgm_code import cmaCgm_startOut
from shipping.evergreen.yangming import yangmingStart
from shipping.evergreen.evergreen_code import evergreen_startOut
from shipping.evergreen.zhmchina import zhimchina
from shipping.evergreen.Mskfob001 import Mskfob001_startOut
from shipping.evergreen.Coscofob001_code import Coscofob001_startOut
from shipping.read_writer_file.writer_file import writer_file
from shipping.read_writer_file.create_file import createFile
from shipping.read_writer_file.writer_repetitionFile import writer_repetitionFile
from shipping.read_writer_file.repetitionFile import repetitionFile
from shipping.evergreen.cma_cgm_code import cmaCgm_startOut
from shipping.read_writer_file.search_failure import search

def start():

    global num
    num = 0
    # 49.87.133.175:4236
    # 导入.csv文件
    data = pd.read_excel(r'C:\Users\86177\Desktop\v2_shipping\shipping\excel\testTESE.xls')

    dateStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("<开始今天查询任务：{}>".format(dateStart))
    # 创建导出的信息，以及后续需要重复查询的信息

    while num < data.count()['柜号']:

        # 选取出柜号信息
        container = data['柜号'][num]
        # 选取出船网址信息
        url = data['船公司查询网址'][num]
        # 船公司简称
        shipping_name = data['船公司简称'][num]
        # 当前状态
        now_status = data['当前状态'][num]
        # 到港日
        arrival_date = data['到港日'][num]

        # 选取对应的公司，进行数据读取
        if shipping_name == "CMA":  # 已完成-存储已完成

            print("\n第{}行  {}运行开始￥￥￥".format(num, shipping_name))
            print(shipping_name)
            num = cmaCgm_startOut(container, url, shipping_name, now_status, arrival_date, num)
            print("第{}行  {}运行结束~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "COSCO":  # 已完成-存储已完成

            print("\n第{}行  {}运行开始￥￥￥".format(num, shipping_name))
            num = Coscofob001_startOut(container, url, shipping_name, now_status, arrival_date, num)
            print("第{}行  {}运行结束~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "EMC":  # 已完成-存储已完成

            print("\n第{}行  {}运行开始￥￥￥".format(num, shipping_name))
            num = evergreen_startOut(container, url, shipping_name, now_status, arrival_date, num)
            print("第{}行  {}运行结束~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "HMM":  # 导出重复查找，提醒需要手动查询 - 已完成存储

            print("\n第{}行  {}运行开始￥￥￥".format(num, shipping_name))
            print("过")
            search("需要手动查找", num)
            num = num + 1
            print("第{}行  {}运行结束~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "WHL":  # 已完成--已完成存儲

            print("\n第{}行  {}运行开始￥￥￥".format(num, shipping_name))
            num = wanhai(container, url, shipping_name, now_status, arrival_date, num)
            print("第{}行  {}运行结束~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "MSK":  # 已完成--已完成存储

            print("\n第{}行  {}运行开始￥￥￥".format(num, shipping_name))
            num = Mskfob001_startOut(container, url, shipping_name, now_status, arrival_date, num)
            print("第{}行  {}运行结束~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "ONE":  # 已完成--已完成存儲

            print("\n第{}行  {}运行开始￥￥￥".format(num, shipping_name))
            num = ecommOneLine(container, url, shipping_name, now_status, arrival_date, num)
            print("第{}行  {}运行结束~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "OOCL":

            # ----------需要解决滑动验证码
            print("过")
            num = search("需要手动查找", num)
            num = num + 1
            time.sleep(3)

        elif shipping_name == "HPL":  # 已完成--已完成存儲

            print("\n第{}行  {}运行开始￥￥￥".format(num, shipping_name))
            num = hapag_lloyd(container, url, shipping_name, now_status, arrival_date, num)
            print("第{}行  {}运行结束~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "YML":  # 已完成--

            print("\n第{}行  {}运行开始￥￥￥".format(num, shipping_name))
            num = yangmingStart(container, url, num)
            print("第{}行  {}运行结束~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "ZIM":

            # ----------需要解决滑动验证码
            print("过")
            num = search("需要手动查找", num)
            num = num + 1
            # print("沒有")
            # num = num + 1
            # dic = {'id':num,'container':container,'url':url,"notice":"Y"}
            # writer_repetitionFile(dic)
            # time.sleep(3)
        else:
            num = num + 1
            print("过过过！")

    dateStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("\n<结束今天查询任务：{}>".format(dateStart))






