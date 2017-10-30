# -*- coding: UTF-8 -*-
# import requests
import requests
import urlparse
import sys
import os
from WebParse import DLParser
from WebConstant import WebConstant
class WebSiteDL(object):

    def __init__(self):
        self.content = ""
        self.down_path = ""
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}#构造头部
        self.cook={"Cookie":'ll="118205"; _ga=GA1.2.740277333.1448884744; _gat=1; bid="iu5QJoQtotc"; ps=y; '}

    def download_web(self,url):
        result = urlparse.urlparse(url,False)
        self.down_path = self.generate_path(result[1],result[2])
        response = requests.get(url,cookies=self.cook,headers=self.headers)
        self.content = response.text

    def download_img(self,imgs = []):
        for i in xrange(0,len(imgs)):
            img = imgs[i]
            if img.endswith("jpg") or img.endswith("png") or img.endswith("gif"):
                response = requests.get(img,cookies=self.cook,headers=self.headers)
                result = urlparse.urlparse(img,False)
                print "第%d张图片下载完成"%i
                path = result[2]
                name = path.split("/")[-1]
                with open(self.down_path+os.sep+name,"wb") as f:
                    f.write(response.content)

    def generate_path(self,domain,path):
        if os.path.exists(WebConstant.download_path):
            path = WebConstant.download_path + domain +''.join(path.split("/")[:-1])
            if not os.path.exists(path):
                os.makedirs(path)
            return path
        else:
            raise Exception("下载路径不存在")


if __name__ == "__main__":
    WebConstant.load_config()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    dl = WebSiteDL()
    dl.download_web(WebConstant.web_url)
    parser = DLParser()
    parser.feed(dl.content)
    dl.download_img(parser.img)
