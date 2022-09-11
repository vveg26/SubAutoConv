import requests 
import configparser

conf=configparser.ConfigParser()

conf.read("./config.ini")
# 连接转换

type = conf.get('common','type')

ourls= conf.options(type)
for ourl in ourls:
                url = conf.get(type, ourl)
                api = conf.get('common','api')
                endurl = r'target='+type+r'&url='+url

                # 目标链接
                tarurl = api+endurl
                r = requests.get(tarurl,allow_redirects=True)
                
                if(type == 'clash'):
                        ext = ".yaml"
                elif(type == 'mixed'):
                        ext = ".txt"
                filepath = "./sub/"+ourl+ext 
                with open(filepath, "wb") as code:
                        code.write(r.content)

                print(tarurl) 




