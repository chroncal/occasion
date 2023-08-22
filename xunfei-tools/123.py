import re  
import requests
import os 

num=0    
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82',
        'Cookie':'BAIDUID=3DEBA4EB6B997F18ADA10476942B2A64:FG=1; BIDUPSID=3DEBA4EB6B997F18ADA10476942B2A64; PSTM=1686022870; BDUSS=1VUbDVNN3VSdy10c2FrYTNwdHN5eDFqQVE2WTlGYmgxblVMdHpId0xBNUJyOTFrSUFBQUFBJCQAAAAAAAAAAAEAAAAlcjxEsK7QprXEsq6-9Lntue0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEEitmRBIrZkM; BDUSS_BFESS=1VUbDVNN3VSdy10c2FrYTNwdHN5eDFqQVE2WTlGYmgxblVMdHpId0xBNUJyOTFrSUFBQUFBJCQAAAAAAAAAAAEAAAAlcjxEsK7QprXEsq6-9Lntue0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEEitmRBIrZkM; BAIDUID_BFESS=3DEBA4EB6B997F18ADA10476942B2A64:FG=1; delPer=0; PSINO=5; H_PS_PSSID=36554_38643_39026_39024_38943_38879_38955_38983_38960_38810_38989_39089_26350_39042_39095_39100_38952; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=0g248lag2k81a00000al042j1ibccec1p; ZFY=tUgCDsHiiLwS7BUE:AWaxRShL3KkAErkl91oIV7jvyUo:C; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_MGMyMTJlNWE3YWFhOWIzNGE0MzlkM2ZiM2NmNmE3NzI2ODUxMzBhMTk4YzYyZmI4OWQ4ODE2NWRjNjA3MGE2ZWZhZTBjODc4MTYwOWU0NDVlZDcxM2JiNjFiMTMwMGVlNDVjNDI3M2Y3ZjMzZmFlNzQyYmQ2YmMzMDlmNzc5MWZkYmQ0NzE4NTJhNDRkZTY0NTFmOGI4MDc3ZjMyYTY1ZA==',#这里需要大家根据自己的浏览器情况自行填写
        'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection':'keep-alive'
        }  
url='https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDEsNiw0LDcsOCw1LDIsOQ%3D%3D&word=%E7%99%BD%E8%89%B2%E8%83%8C%E6%99%AF%E4%B8%80%E6%A0%B9%E9%BB%84%E7%93%9C'
html=requests.get(url,headers=header)
html.encoding='utf8'
 
html=html.text
path='C:\\Users\\Meow_Sakura\\Desktop\\1'
if not os.path.exists(path):
    os.mkdir(path)
 
res=re.findall('"objURL":"(.*?)"',html)  #正则表达式，筛选出html页面中符合条件的图片源代码地址url
for i in res:   #遍历
    num=num+1
    picture=requests.get(i)       
    file_name='C:\\Users\\Meow_Sakura\\Desktop\\1'+str(num)+".jpg"   #给下载下来的图片命名。加数字，是为了名字不重复
    f=open(file_name,"wb")#以二进制写入的方式打开图片
    f.write(picture.content)   
 
    print(i)    #看看有哪些url
f.close()      #结束f文件操作