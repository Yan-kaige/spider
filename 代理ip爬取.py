import requests
import re
import random
import csv


def get_ip(new2_ips):  # 爬取代理IP
    new_ips = []
    for i in range(1,10):
        r = requests.get('http://www.xiladaili.com/http/'+str(i))
        ips = re.findall('<td>(.*?):(.*)</td>', r.text)  # 正则表达式过滤ip

        for i in ips:
            if (ips.index(i)) % 2 == 0:
                new_ips.append(i)
            else:
                continue
        for i in new_ips:
            new2_ips.append(i[0]+':'+i[1])


def gethtmltext(url,lista,f):
        header={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
            "cookie":"thw=cn; isg=BMvLGjT8EiVAE07xJHYV_URBQ2-1YN_inmVO3T3Ip4phXOu-xTBvMmn6Mtyy5zfa; cna=jvc9FoCbeGkCAW8SXaXIchFm; t=c1345ff59e8dac9a46fa693825519285; cookie2=12f10daf327113c535fdb1bac0d11973; v=0; _tb_token_=e31453e66d635; l=dBSIWWKPq39SDo0TBOCZourza77tIdAYYuPzaNbMi_5NT681th7OkabESFJ6csWfTCTB4NSiTkp9-etkwqZEMnMgcGAw_xDc.; unb=3243535564; uc1=cookie14=UoTbnxr99XuAmg%3D%3D&lng=zh_CN&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie21=VT5L2FSpccLuJBreK%2BBd&tag=8&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; uc3=nk2=F6k3HMt0%2FuehBePTXlLpXp5YJb0%3D&vt3=F8dByucubyzUX12H4R4%3D&lg2=W5iHLLyFOGW7aA%3D%3D&id2=UNJV3tGwnafDFw%3D%3D; csg=bd75ef92; lgc=t_1491537574293_0631; cookie17=UNJV3tGwnafDFw%3D%3D; dnk=t_1491537574293_0631; skt=0097a1aabb31f6fe; existShop=MTU3MjI3NjYzOA%3D%3D; uc4=nk4=0%40FbMocp0T%2Baqe0jrmfqhJ5tUswE0MVV7AsH7UcPODFg%3D%3D&id4=0%40UgXSqsu5HQg7J52hv%2BzOj4B2gRfT; tracknick=t_1491537574293_0631; _cc_=WqG3DMC9EA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=143; _nk_=t_1491537574293_0631; cookie1=B0OovR6gzsVzqnYQyV1%2BXYD98weyOVgbXx%2B%2BQRPouc0%3D; mt=ci=1_1; enc=mjvb%2BnGT439QXHJ%2F2AUN4TznrmGOPXVXcljuhJMtLTjp6ZPGcO3cUMYyiuUdbizGkW1Wi3g8A3gqwqm%2FthwgMA%3D%3D"
        }

        for q in range(200):    #使用代理ip池
                try:
                        i=random.choice(lista)
                        proxi={
                        'http':'http://'+'str(i)'+"'",

                        }
                        r=requests.get(url,headers=header,proxies=proxi)  #如果请求成功则停止遍历
                        print(i)
                        f.writelines(str(i)+"\n")
                        
                        continue
                        
                except Exception as res:
                    print(res)
                    continue
        r.raise_for_status()
        return r.text
def parsepage(ilt,html):  #解析HTML页面并保存主要属性
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)

        for i in range(30):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
def printgoodslist(ilt):   #输出数据
    tqlt="{:4}\t{:8}\t{:20}"
    print(tqlt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count+=1
        print(tqlt.format(count,g[0],g[1]))
def main():
       
        iplist = []  # 存放ip地址
        get_ip(iplist)           
        start_url="https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
        infolist=[]
        
        for i in range(2):   #设置爬取多少页
            try:
                    m=open(r"xx.txt", 'a+')
                    url=start_url
                    html=gethtmltext(url+'&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s='+str(44*i),iplist,m)
                    # parsepage(infolist,html)
                    m.close()


            except Exception as error:
                print(error)
                continue
        # printgoodslist(infolist)
main()
