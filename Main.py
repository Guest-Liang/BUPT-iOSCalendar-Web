import requests
import icalendar
import re
import datetime
import execjs
from Constant import *

#是否写入本地html
IsLocalHtml=False

def GetXNXQ(): #获取学年学期，形如'2022-2023-2'，2-7月为第二学期，8-次年1月为第一学期
    CurrentYear=datetime.datetime.now().year
    CurrentMonth=datetime.datetime.now().month
    if CurrentMonth>=2 and CurrentMonth<=7:
        XNXQ=str(CurrentYear-1)+'-'+str(CurrentYear)+'-2'
    else:
        XNXQ=str(CurrentYear)+'-'+str(CurrentYear+1)+'-1'
    return XNXQ

#直接编译运行js文件，获取加密后的学号和密码
ctx=execjs.compile(CONWORK_JS_DECODED)
Encoded=str(ctx.call("encodeInp", SchoolID))+"%%%"+str(ctx.call("encodeInp", Password_jwgl)) #加密后的学号和密码

Xueqi=GetXNXQ(); #获取学年学期，形如'2022-2023-2'
#Xueqi='' #可以手动输入学年学期，形如'2022-2023-2'
UserData={'userAccount':SchoolID,'userPassword':Password_jwgl,'encoded':Encoded} #用户数据，保存在Constant.py中，根据需要修改

#登录教务系统
print('登录北邮教务管理系统')
Session=requests.Session()
Login=Session.get(url=LOGIN_URL,headers={'User-Agent':USER_AGENT})
Cookies1=Login.cookies.items() #处理cookies
Cookie=''
for Name, Value in Cookies1:
    Cookie+=f'{Name}={Value};'

#设置headers，先post用户数据
Headers_UserData={
    'Host':'jwgl.bupt.edu.cn',
    'Referer':'https://jwgl.bupt.edu.cn/jsxsd/xk/LoginToXk?method=exit&tktime=1631723647000',
    'User-Agent':USER_AGENT,
    'cookie':Cookie
}
Session.post(url=POST_URL,data=UserData,headers=Headers_UserData) #由LOGIN_URL的html决定是post方法，action='/jsxsd/xk/LoginToXk'
Cookies2=Login.cookies.items() #登录后cookie可能变了，重新处理一下
Cookie_Logged_In=''
for Name, Value in Cookies2:
    Cookie_Logged_In+='{0}={1}; '.format(Name,Value)

#设置headers
Headers={
    'User-Agent':USER_AGENT,
    'cookie':Cookie_Logged_In
}
#周次（默认全部），学年学期（默认当前学期），课表节次id，课表类别
Info={'zc':'','xnxq01id':Xueqi,'kbjcmsid':KBJCMSID['0'],'kblb':KBLB['0']}
Url='https://jwgl.bupt.edu.cn/jsxsd/xskb/xskb_list.do'
Data=requests.post(url=Url,headers=Headers,data=Info) #获取课表html
if "请先登录系统" in Data.text:
    print("登录失败，请检查学号和密码以及网络连接，并重新运行程序")
    exit()

#将.do写入本地html文件
if IsLocalHtml:
    print("正在写入本地html")
    try:
        with open(f'./{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")}.html', 'w', encoding='utf-8') as file:
            file.write(Data.text)
            print(f'[success]')
    except Exception:
        print("生成文件失败")

