import re  
import requests
import os 


def get_img(header, url, path, num_images=30, num_pages=3):
    '''
        header: 网站请求头
        url: 目标网站
        path: 保存图片路径
        num_images: 爬取的图片数量，默认为30
        num_pages: 爬取的页数，默认为3
    '''
    # 若没有该路径新建一个文件夹
    if not os.path.exists(path):
        os.makedirs(path)

    total_images = 0
    for page in range(num_pages):
        page_url = f"{url}&pn={page * 30}"  # 设置每一页的起始位置
        html = requests.get(page_url, headers=header, timeout=10)
        html.encoding = 'utf8'
        html = html.text

        res = re.findall('"objURL":"(.*?)"', html)
        for i in res:
            if total_images >= num_images:
                return
            try:
                img = requests.get(i, timeout=10)
                img_name = os.path.join(path, str(total_images + 1) + ".jpg")
                with open(img_name, "wb") as f:
                    f.write(img.content)
                print(i, '-->', path)
                total_images += 1
            except (requests.exceptions.Timeout,requests.exceptions.ConnectionError):
                print("请求超时:", i)
                continue

    f.close()
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82',
                'Cookie':'BAIDUID=3DEBA4EB6B997F18ADA10476942B2A64:FG=1; BIDUPSID=3DEBA4EB6B997F18ADA10476942B2A64; PSTM=1686022870; BAIDUID_BFESS=3DEBA4EB6B997F18ADA10476942B2A64:FG=1; BA_HECTOR=0g248lag2k81a00000al042j1ibccec1p; ZFY=tUgCDsHiiLwS7BUE:AWaxRShL3KkAErkl91oIV7jvyUo:C; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[kSyA9a8U-kc]=mk3SLVN4HKm; delPer=0; PSINO=5; H_PS_PSSID=26350; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDUSS=JlWXc4TGZmeTY1eU5pZmVpeUpuRE1SREl4fmxCfnFFV2JIa001cURmTGYtZDFrSUFBQUFBJCQAAAAAAAAAAAEAAAAlcjxEsK7QprXEsq6-9Lntue0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN9stmTfbLZkSk; BDUSS_BFESS=JlWXc4TGZmeTY1eU5pZmVpeUpuRE1SREl4fmxCfnFFV2JIa001cURmTGYtZDFrSUFBQUFBJCQAAAAAAAAAAAEAAAAlcjxEsK7QprXEsq6-9Lntue0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN9stmTfbLZkSk; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; userFrom=null; ab_sr=1.0.1_NzViNzY0NTBiZmM2Y2MwM2FhOTFiZGQ5MDI1ZjA3MTk4YzM1ZDEzNTFmMzRhOTU0MWE2MTg5MjhlNzBmNjY1YjY2NzU1MDAxNmRlODgzMTA2YjYyNjcwMDc3ZTc0NDM5OWZhNWZhYmJkNGJiZmZhMTM3MzZhNjM2MGE4N2FmM2JmMTZiZDhlNGJmOThlNTgwZTA1YzlhYjg0NzY0NDA1Nw==',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept':'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Connection':'keep-alive'
                }  

url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1689683042642_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCwzLDEsNiw0LDUsMiw3LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E7%99%BD%E8%89%B2%E8%83%8C%E6%99%AF+%E6%B0%B4%E7%A8%BB%E6%A4%8D%E6%A0%AA'
path='C:\\Users\\Meow_Sakura\\Desktop\\干扰数据集_1\\rice'
get_img(header=header,url=url,path=path)


