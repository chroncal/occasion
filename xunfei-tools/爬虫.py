
import requests
import re
import os

num=0 #批量命名图片信息

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82',
        'Cookie':'BAIDUID=3DEBA4EB6B997F18ADA10476942B2A64:FG=1; BIDUPSID=3DEBA4EB6B997F18ADA10476942B2A64; PSTM=1686022870; BDUSS=1VUbDVNN3VSdy10c2FrYTNwdHN5eDFqQVE2WTlGYmgxblVMdHpId0xBNUJyOTFrSUFBQUFBJCQAAAAAAAAAAAEAAAAlcjxEsK7QprXEsq6-9Lntue0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEEitmRBIrZkM; BDUSS_BFESS=1VUbDVNN3VSdy10c2FrYTNwdHN5eDFqQVE2WTlGYmgxblVMdHpId0xBNUJyOTFrSUFBQUFBJCQAAAAAAAAAAAEAAAAlcjxEsK7QprXEsq6-9Lntue0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEEitmRBIrZkM; BAIDUID_BFESS=3DEBA4EB6B997F18ADA10476942B2A64:FG=1; delPer=0; PSINO=5; H_PS_PSSID=36554_38643_39026_39024_38943_38879_38955_38983_38960_38810_38989_39089_26350_39042_39095_39100_38952; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=0g248lag2k81a00000al042j1ibccec1p; ZFY=tUgCDsHiiLwS7BUE:AWaxRShL3KkAErkl91oIV7jvyUo:C; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_MGMyMTJlNWE3YWFhOWIzNGE0MzlkM2ZiM2NmNmE3NzI2ODUxMzBhMTk4YzYyZmI4OWQ4ODE2NWRjNjA3MGE2ZWZhZTBjODc4MTYwOWU0NDVlZDcxM2JiNjFiMTMwMGVlNDVjNDI3M2Y3ZjMzZmFlNzQyYmQ2YmMzMDlmNzc5MWZkYmQ0NzE4NTJhNDRkZTY0NTFmOGI4MDc3ZjMyYTY1ZA==',
        'Accept':'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection':'keep-alive'
        }

def get_img(url,path):
    #预处理url
    html=requests.get(url,headers=header)
    html.encoding='utf8'#防止乱码
    print(html.text)
    #设置图片保存路径
    if not os.path.exists(path):
        os.mkdir(path)
    #正则表达式 筛选图片源地址
    res=re.findall('"objURL":"(.*?)"',html)
    #遍历
    for i in res:
        num=num+1
        img=requests.get(i)#获得图片大图
        file_name=path+str(num)+".jpeg"
        f=open(file_name,"wb")
        f.write(img.content)
        print(i)
    f.close()

if __name__=="__main__":
    url='https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDEsNiw0LDUsMiw3LDgsOQ%3D%3D&word=%E7%99%BD%E8%89%B2%E8%83%8C%E6%99%AF%E9%BB%84%E7%93%9C'
    path='C:\\Users\\Meow_Sakura\\Desktop\\1'
