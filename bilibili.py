import re
import requests
import json
import time
import csv
import math
import threading
from Useragent import get_user_agent
from get_ip import get_ip
from multiprocessing import Process
list1 = []
f=open("xx.txt", 'a+')
global xunhuan
xunhuan=0
start_time=time.time()
def get_list(base_url,):
    try:
        ip=get_ip()
        proxi={'http':'http://'+ip+"'",  }
        print("当前ip---"+str(ip))
        end_time=time.time()
        time1=end_time-start_time
        time1=math.trunc(time1)
        print("用时："+str(time1)+'s')
        video_list = []
        m = requests.get(base_url,headers=get_user_agent(),proxies=proxi)
        m = json.loads(m.text)
        for i in m['data']['Related']:
            video_list.append(i['aid'])
        for i in video_list:  #遍历推荐视频
            if i in list1:
                continue
            else:
                ip=get_ip()
                proxi={'http':'http://'+ip+"'",    }
                m = requests.get('https://api.bilibili.com/x/web-interface/view/detail?bvid=&aid='+str(i)+'&jsonp=jsonp',headers=get_user_agent(),proxies=proxi)
                m = json.loads(m.text)
                w1 = m['data']['View']['title']
                w2 = m['data']['View']['stat']['view']
                list1.append(i)
                f.writelines(str(i)+','+str(w2)+","+w1+'\n')
                time.sleep(0.2)
        print(len(list1))
        get_list('https://api.bilibili.com/x/web-interface/view/detail?bvid=&aid=%s&jsonp=jsonp' % list1[-1],) #递归调用
    except Exception as error:
        print(error)
def main():
    try:
        lis2=[62162985,46996647,50941399,54385039,50331935,80856554,36945064,35198390,45031807]
        for i in lis2:
            base_url='https://api.bilibili.com/x/web-interface/view/detail?bvid=&aid=%s&jsonp=jsonp'%str(i)
            threading.Thread(target=get_list,args=(base_url,)).start()
    except:
        pass
if __name__ == "__main__":
    main()
