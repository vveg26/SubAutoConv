import requests 
import configparser

conf=configparser.ConfigParser()

conf.read("./config.ini")
# 连接转换
ourls= conf.options('v2url') 
for ourl in ourls:
    url = conf.get('v2url', ourl)
    api = conf.get('common','api')
    endurl = r'target=clash&url='+url

    # 目标链接
    tarurl = api+endurl
    r = requests.get(tarurl,allow_redirects=True)
    filepath = "./sub/"+ourl+".yaml" 
    with open(filepath, "wb") as code:
            code.write(r.content)

    print(tarurl)


