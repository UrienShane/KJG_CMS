# coding=gbk

from pymongo import MongoClient
from docx import Document


# ����MongoDB���ݿ�����
client = MongoClient('127.0.0.1', 27017)

# �����������ݿ�,serpΪ���ݿ���
db = client.serp

# #��֤�û�����
# db.authenticate('serp','serp123456')

# �������ü��ϣ�Ҳ��������ͨ����˵�ı�testΪ����
collection = db.data
# collection.insert_one({"label": "�Ƽ���չƷ", "venue": "������ţ��ͯ��"})

print("���ӳɹ�")
# ������Ϳ�����collection����ɶ����ݿ���һЩ����

path = "E:/����/1216/20180309�Ƽ���չƷ��¼���ܱ�.docx" #�ļ�·��
document = Document(path) #�����ļ�
tables = document.tables #��ȡ�ļ��еı��

table_name = ['�Ϻ��Ƽ���', '�Ϻ���Ȼ�����', '�й��Ƽ���', '������ţ��ͯ��', '�����Ƽ���', '�����Ƽ���', '�㽭ʡ�Ƽ���', '���ݵ�̼��', '���˿Ƽ���', '���ݿƼ���', '����Ƽ���', '�ϷʿƼ���', '���ſƼ���']

for x in range (0, 15):
    venue = table_name[x]
    table = tables[x]  # ��ȡ�ļ��еĵ�һ�����

    print(venue)
    for i in range(2,len(table.rows)):#�ӱ���5�п�ʼѭ����ȡ������� len(table.rows)
        n = 1
        xh = table.cell(i, n-1).text
        zpmc = table.cell(i, n).text
        jbnr = table.cell(i, n+1).text
        kbdjbm = table.cell(i, n+2).text
        kbdjqd = table.cell(i, n+3).text
        rzsp = table.cell(i, n+4).text
        kxtjys = table.cell(i, n+5).text
        stseys = table.cell(i, n+6).text
        kjbj = table.cell(i, n+7).text
        fzjjxs = table.cell(i, n+8).text
        fzjjnr = table.cell(i, n+9).text
        zplb = table.cell(i, n+10).text
        zcfl = table.cell(i, n+11).text
        zpjs = table.cell(i, n+12).text
        jbczykxyyff = table.cell(i, n+13).text
        xxxg = table.cell(i, n+14).text
        cgrs = table.cell(i, n+15).text
        ztmc = table.cell(i, n+16).text
        ztxsjg = table.cell(i, n+17).text
        xq = table.cell(i, n+18).text
        jlsj = table.cell(i, n+19).text
        jlr = table.cell(i, n+20).text

        item = {"name":zpmc, "content":jbnr, "standard_code":kbdjbm, "standard_strength":kbdjqd, "congnition_level":rzsp, "explore_factor":kxtjys, "STSE_factor":stseys, "space_layout":kjbj, "teach_style":fzjjxs, "teach_content":fzjjnr, "exhibit_class":zplb, "exhibition_class":zcfl, "exhibit_tech":zpjs, "method":jbczykxyyff, "effect":xxxg, "people_number":cgrs, "room":ztmc, "narrate_stru":ztxsjg, "weekend":xq, "record_time":jlsj, "record_people":jlr}


        collection.insert_one({"label": "�Ƽ���չƷ", "venue": venue, "item": item})

        print(xh)
        print("д��ɹ�\n")

print("д�����")
