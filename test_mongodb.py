
from pymongo import MongoClient
# 连接数据库 需要host和用户名和密码
client = MongoClient("mongodb://localhost:27017/",
                     username='admin',
                     password='tangpei123')
# 创建数据库
mydb = client["studydb"]
# 创建集合
mycollection = mydb["student_size"]
# 插入一个文档，这个文档在python里面是字典
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
# 插入一个用insert_one
#            x = mycollection.insert_one(mydict)
mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
# 插入一个数组的文档用insert_many
#            x = mycollection.insert_many(mylist)

# 用many弄的需要变为inserted_ids多了个s
#            print(x.inserted_ids)

# 查找所有
for x in mycollection.find():
    print(x)
print("-----------------")
# 查询指定字段的数据，将要返回的字段对应值设置为 1。但是必须指定一个0，如果只指定了一个0其他都默认为1
for x in mycollection.find({},{ "_id": 0, "name": 1, "alexa": 1 }):
    print(x)
print("-----------------")
# 在这里可以输出Ascii大于H的的值---$gt
myquery = {"name": {"$gt": "H"}}
x = mycollection.find(myquery)
for i in x:
    print(i)
print("-----------------")
# 还可以通过正则表达式查询----$regex
myre = {"name": {"$regex": "^R"}}
x1 = mycollection.find(myre)
for i in x1:
    print(i)
print("-----------------")
# 也可以用limit()控制输出的条数,limit里面只能放一个参数
limit_output = mycollection.find().limit(3)
for i in limit_output:
    print(i)
print("-----------------")
# 可以在 MongoDB 中使用 update_one(x,y) 方法修改文档中的记录。该方法第一个参数x为查询的条件，第二个参数y为要修改的字段。如果查找到的匹配数据多于一条，则只会修改第一条。
origin = {'alexa': '10000'}
update_data = {"$set": {'alexa':  '12345'}}
mycollection.update_one(origin, update_data)
for x in mycollection.find():
  print(x)
print("-----------------")
# 反之update_many(x,y)可以输出所有的匹配值
#      mycollection.update_many(origin,update_data)

# 用sort()来排序，
# 升序
sort_up = mycollection.find().sort("alexa")
# 降序
sort_down = mycollection.find().sort("alexa", -1)

for i in sort_up:
    print(i)
print("-----------------")
for w in sort_down:
    print(w)
print("-----------------")

# 在这里进行删除操作
# 删除一个指定的文档,如果搜索出来有多个只删除第一个
mycollection.delete_one({"name": "Taobao"})
for i in mycollection.find():
    print(i)
print("-----------------")
# 删除指定的所有指定的文档
mycollection.delete_many({"name": {"$regex": "^F"}})
for i in mycollection.find():
    print(i)

# 删除集合中所有的文档
#       x = mycollection.delete_many({})

# 删除集合
# mycollection.drop()
