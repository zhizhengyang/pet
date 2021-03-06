from mongoengine import *
from datetime import datetime
import json
import re
# 连接数据库
connect('petSearch') # 连接本地blog数据库
# 如需验证和指定主机名
# connect('blog', host='192.168.3.1', username='root', password='1234')
 
# 定义分类文档
class petSearch(Document):
    ' 继承Document类,为普通文档 '
    title = StringField(max_length=60, required=True)
    author = StringField(max_length=10,required=True)
    artnum = IntField(default=0, required=True)
    artical_search = StringField(max_lengths=30000,required=True)
    title_search = StringField(max_lengths = 300,required=True)
    artical = StringField(max_lengths=20000,required=True)
    url = StringField(max_length=100,required=True)
    date = DateTimeField(default=datetime.now(), required=True)

#test_data_list = petSearch.objects(__raw__={'$text':{'$search':'不爱动 拉肚子'}}).limit(20)



