# coding=gbk
import os
from pymongo import MongoClient
from docx import Document

folder = '�ۺϹ�'
label = '2018�ۺϹ�'
venue = ''

# path = "E:/����/1216/�ۺϹ�/1.docx" #�ļ�·��
path = "D:/data/1.docx" #�ļ�·��
document = Document(path) #�����ļ�
tables = document.tables #��ȡ�ļ��еı��

# ����MongoDB���ݿ�����
client = MongoClient('127.0.0.1', 27017)

# �����������ݿ�,serpΪ���ݿ���
db = client.kxjy

# #��֤�û�����
# db.authenticate('serp','serp123456')

# �������ü��ϣ�Ҳ��������ͨ����˵�ı�testΪ����
collection = db.data

print("���ӳɹ�")
# ������Ϳ�����collection����ɶ����ݿ���һЩ����


table_name = ['��ͷ�Ƽ���', '����Ƽ���', '��ݸ�Ƽ���', '��ɽ�Ƽ���', '�㶫��ѧ����', '�������Ƽ���', '���ɹſƼ���', '����̽������', '�й��Ƽ���']

for x in range (0, 10):
    venue = table_name[x]
    table = tables[x]  # ��ȡ�ļ��еĵ�һ�����
    print(venue)

    for i in range(4,len(table.rows)):#�ӱ���5�п�ʼѭ����ȡ������� len(table.rows)
        n = 1
        xh = table.cell(i, n-1).text
        zpmc = table.cell(i, n).text
        jbnr = table.cell(i, n+1).text
        ztmc = table.cell(i, n+2).text
        zsjs = table.cell(i, n+3).text  # ����
        jyx = table.cell(i, n+4).text
        kxx = table.cell(i, n+5).text
        qwx = table.cell(i, n+6).text
        ysx = table.cell(i, n+7).text
        cyx = table.cell(i, n+8).text
        czjd = table.cell(i, n+9).text
        zttc = table.cell(i, n+10).text
        gdmq = table.cell(i, n+11).text
        fgxm = table.cell(i, n+12).text
        wzsmzxgf = table.cell(i, n+13).text     # ����
        szmt = table.cell(i, n+14).text     # ����
        zcsjzyxs = table.cell(i, n+15).text     # ����
        kxzs = table.cell(i, n+16).text     # ����
        zcnrxz = table.cell(i, n+17).text       # ����

        zsjs_new = ""
        for index,letter in enumerate(zsjs):
            if letter == '1':
                zsjs_new += "�������⾫��"
            elif letter == '2':
                zsjs_new += "�������š�ɫ�ʺ�г"
            elif letter == '3':
                zsjs_new += "�ṹ�ι�"
            elif letter == '4':
                zsjs_new += "�����Ź�"
            elif letter == '5':
                zsjs_new += "��ĥ���⻬����ȱ���޼������"
            elif letter == '6':
                zsjs_new += "�����������ࡢ���ͳһ"
            if index!=(len(zsjs)-1) and letter!='/':
                zsjs_new += "/"

        wzsmzxgf_new = ""
        for index,letter in enumerate(wzsmzxgf):
            if letter == '1':
                wzsmzxgf_new += "��һ������˵����������һ������˵��"
            elif letter == '2':
                wzsmzxgf_new += "���塢����������ʽ��������ͳһ"
            elif letter == '3':
                wzsmzxgf_new += "����˵������������ͨ���׶�"
            elif letter == '4':
                wzsmzxgf_new += "ʹ�ü���"
            if index!=(len(wzsmzxgf)-1) and letter!='/':
                wzsmzxgf_new += "/"

        szmt_new = ""
        for index,letter in enumerate(szmt):
            if letter == '1':
                szmt_new += "��Ƶ"
            elif letter == '2':
                szmt_new += "��Ƶ"
            elif letter == '3':
                szmt_new += "����ý�崥����"
            elif letter == '4':
                szmt_new += "������ʵ����"
            elif letter == '5':
                szmt_new += "�龰��������ý��"
            if index!=(len(szmt)-1) and letter!='/':
                szmt_new += "/"

        zcsjzyxs_new = ""
        for index,letter in enumerate(zcsjzyxs):
            if letter == '1':
                zcsjzyxs_new += "ͼ�İ�"
            elif letter == '2':
                zcsjzyxs_new += "ʵ��"
            elif letter == '3':
                zcsjzyxs_new += "ģ��"
            elif letter == '4':
                zcsjzyxs_new += "ԭ����������"
            elif letter == '5':
                zcsjzyxs_new += "���绥��չ��"
            elif letter == '6':
                zcsjzyxs_new += "��ý��"
            elif letter == '7':
                zcsjzyxs_new += "ӰԺ��糡"
            if index!=(len(zcsjzyxs)-1) and letter!='/':
                zcsjzyxs_new += "/"

        kxzs_new = ""
        for index,letter in enumerate(kxzs):
            if letter == '1':
                kxzs_new += "����"
            elif letter == '2':
                kxzs_new += "��ʶ"
            elif letter == '3':
                kxzs_new += "�߿Ƽ�"
            elif letter == '4':
                kxzs_new += "����"
            elif letter == '5':
                kxzs_new += "����"
            if index!=(len(kxzs)-1) and letter!='/':
                kxzs_new += "/"

        zcnrxz_new = ""
        for index,letter in enumerate(zcnrxz):
            if letter == '1':
                zcnrxz_new += "��ѧ"
            elif letter == '2':
                zcnrxz_new += "����"
            elif letter == '3':
                zcnrxz_new += "���"
            elif letter == '4':
                zcnrxz_new += "����"
            if index!=(len(zcnrxz)-1) and letter!='/':
                zcnrxz_new += "/"

        imgList = []
        videoList = []

        item = {"name": zpmc, "content": jbnr, "room": ztmc, "style_design": zsjs_new,
                "selection_principle*educative_nature": jyx, "selection_principle*science_nature": kxx,
                "selection_principle*interesting_nature": qwx, "selection_principle*artistry_nature": ysx,
                "selection_principle*participative_nature": cyx, "selection_principle*operation_nature": czjd,
                "writing_principle*topic_prominence": zttc, "writing_principle*clear_standpoint": gdmq, "writing_principle*style_distinctive": fgxm, "writing_norm": wzsmzxgf_new,
                "digital_media": szmt_new, "exhibit_style": zcsjzyxs_new, "science_knowledge": kxzs_new, "exhibit_content": zcnrxz_new}

        collection.insert_one({"label": label, "venue": venue, "item": item, "imgList":imgList, "videoList":videoList})

        print(xh)
        print("д��ɹ�\n")

print("д�����")
