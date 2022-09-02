import json
import requests
from cookie import login
import time

def qiang(name,password,time1,time2,dai,seat):
    cookie = login(name,password)
    # print(cookie)
    time1 =time.strftime('%Y-%m-%d')+' '+time1
    time2 =time.strftime('%Y-%m-%d') + ' ' + time2
    # print('开始时间',time1)
    # print('结束时间',time2)
    headers={
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': cookie,
        'Origin': 'http://seat.ysu.edu.cn',
        'Referer': 'http://seat.ysu.edu.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'lan': '1',
        # 'token': seat
    }
    # print(headers)
    data={"sysKind": 8,"appAccNo": dai,"memberKind":1,"resvMember":[dai],"resvBeginTime":time1,"resvEndTime":time2,"testName":"","captcha":"","resvProperty":0,"resvDev":[seat],"memo":""}

    response=requests.post('http://seat.ysu.edu.cn/ic-web/reserve',headers=headers,data=json.dumps(data))
    A=response.text
    B=dict(json.loads(A))
    print(B['message'])
    return B['message']


name = '' ##账号
password = '' ##密码
x='13:30:00' ##开始时间
y='22:00:00' ##结束时间
dai=421316 ##个人数据填写区域，dai为你个人学号在系统中的代码
seat=1551 ##座位代码

time.sleep(10)
if qiang(name, password, x, y, dai, seat) == '用户未登录，请重新登录':
    qiang(name, password, x, y, dai, seat)
    time.sleep(5)
    exit()
else:
    time.sleep(5)
    exit()

