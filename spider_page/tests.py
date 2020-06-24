from django.test import TestCase

# Create your tests here.
# test = {
#     "node_name": "WORKGROUP10",
#     "status": "ok",
#     "pending": [],
#     "running": [
#         {
#             "id": "2ff1650a9b2611eaa0e940b0769e5174",
#             "spider": "hezongyy_py",
#             "pid": 22312,
#             "start_time": "2020-05-21 13:44:51.454624"
#         },
#         {
#             "id": "c2a004a69b2611eaa19b40b0769e5174",
#             "spider": "hezongyy_py",
#             "pid": 16556,
#             "start_time": "2020-05-21 13:48:56.467085"
#         }
#     ],
#     "finished": [
#         {
#             "id": "3df38e5e9b2711ea85b940b0769e5174",
#             "spider": "hezongyy_py",
#             "start_time": "2020-05-21 13:52:23.373316",
#             "end_time": "2020-05-21 13:53:05.808515"
#         }
#     ]
# }
#
# test1 = test["running"]
# list1 = []
# for i in range(len(test1)):
#     list1.append(test1[i]["id"])
# print(list1)
# str = "c2a004a69b2611eaa19b40b0769e5174"
# if str in list1:
#     print("成功")
# else:
#     print("失败")
import requests
# url = 'http://localhost:6800/schedule.json'
# data = {'project': 'ScrapyPage', 'spider': 'hezongyy_py'}
# startjob = requests.post(url=url, data=data).text
# data=eval(startjob)
# print(data["jobid"])
# url2 = 'http://127.0.0.1:6800/listjobs.json?project=ScrapyPage'
# listjobs = requests.get(url=url2).text
# print(listjobs)
# listjobs1 = eval(listjobs)["running"]
# print(listjobs1)
# def test1():
#     global a
#     a = 1
# test = test1()
# def test2():
#     print(test.a)

# url = "http://192.168.31.221:6800/logs/ScrapyPage/hezongyy_py/abea720a9eea11ea928f40b0769e5174.log"
# res = requests.request(method="get", url=url)
# print(res.text)
# if "Spider closed" in res.text:
#     print("pass")
# else:
#     print("fail")
for i in range(1, 6):
    print(i)