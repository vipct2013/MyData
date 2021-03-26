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
    # ����.csv�ļ�
    data = pd.read_excel(r'C:\Users\86177\Desktop\v2_shipping\shipping\excel\testTESE.xls')

    dateStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("<��ʼ�����ѯ����{}>".format(dateStart))
    # ������������Ϣ���Լ�������Ҫ�ظ���ѯ����Ϣ

    while num < data.count()['���']:

        # ѡȡ�������Ϣ
        container = data['���'][num]
        # ѡȡ������ַ��Ϣ
        url = data['����˾��ѯ��ַ'][num]
        # ����˾���
        shipping_name = data['����˾���'][num]
        # ��ǰ״̬
        now_status = data['��ǰ״̬'][num]
        # ������
        arrival_date = data['������'][num]

        # ѡȡ��Ӧ�Ĺ�˾���������ݶ�ȡ
        if shipping_name == "CMA":  # �����-�洢�����

            print("\n��{}��  {}���п�ʼ������".format(num, shipping_name))
            print(shipping_name)
            num = cmaCgm_startOut(container, url, shipping_name, now_status, arrival_date, num)
            print("��{}��  {}���н���~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "COSCO":  # �����-�洢�����

            print("\n��{}��  {}���п�ʼ������".format(num, shipping_name))
            num = Coscofob001_startOut(container, url, shipping_name, now_status, arrival_date, num)
            print("��{}��  {}���н���~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "EMC":  # �����-�洢�����

            print("\n��{}��  {}���п�ʼ������".format(num, shipping_name))
            num = evergreen_startOut(container, url, shipping_name, now_status, arrival_date, num)
            print("��{}��  {}���н���~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "HMM":  # �����ظ����ң�������Ҫ�ֶ���ѯ - ����ɴ洢

            print("\n��{}��  {}���п�ʼ������".format(num, shipping_name))
            print("��")
            search("��Ҫ�ֶ�����", num)
            num = num + 1
            print("��{}��  {}���н���~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "WHL":  # �����--����ɴ惦

            print("\n��{}��  {}���п�ʼ������".format(num, shipping_name))
            num = wanhai(container, url, shipping_name, now_status, arrival_date, num)
            print("��{}��  {}���н���~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "MSK":  # �����--����ɴ洢

            print("\n��{}��  {}���п�ʼ������".format(num, shipping_name))
            num = Mskfob001_startOut(container, url, shipping_name, now_status, arrival_date, num)
            print("��{}��  {}���н���~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "ONE":  # �����--����ɴ惦

            print("\n��{}��  {}���п�ʼ������".format(num, shipping_name))
            num = ecommOneLine(container, url, shipping_name, now_status, arrival_date, num)
            print("��{}��  {}���н���~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "OOCL":

            # ----------��Ҫ���������֤��
            print("��")
            num = search("��Ҫ�ֶ�����", num)
            num = num + 1
            time.sleep(3)

        elif shipping_name == "HPL":  # �����--����ɴ惦

            print("\n��{}��  {}���п�ʼ������".format(num, shipping_name))
            num = hapag_lloyd(container, url, shipping_name, now_status, arrival_date, num)
            print("��{}��  {}���н���~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "YML":  # �����--

            print("\n��{}��  {}���п�ʼ������".format(num, shipping_name))
            num = yangmingStart(container, url, num)
            print("��{}��  {}���н���~~~".format(num - 1, shipping_name))
            time.sleep(3)

        elif shipping_name == "ZIM":

            # ----------��Ҫ���������֤��
            print("��")
            num = search("��Ҫ�ֶ�����", num)
            num = num + 1
            # print("�]��")
            # num = num + 1
            # dic = {'id':num,'container':container,'url':url,"notice":"Y"}
            # writer_repetitionFile(dic)
            # time.sleep(3)
        else:
            num = num + 1
            print("��������")

    dateStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("\n<���������ѯ����{}>".format(dateStart))






