from mongoengine import *
from datetime import datetime
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
    artical = StringField(max_lengths=20000,required=True)
    date = DateTimeField(default=datetime.now(), required=True)

#cate = Categories(name="pet",artnum=100)
#cate.save()
#cate = Categories.objects.all()
 
# 返回所有符合查询条件的结果的文档对象列表
#cate = petSearch.objects(name="pet")
#for c in cate:
#    print(c.date)
# 更新查询到的文档:
