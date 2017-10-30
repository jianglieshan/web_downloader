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
    def download_web(self,url):
        result = urlparse.urlparse(url,False)
        self.down_path = self.generate_path(result[1],result[2])
        response = requests.get(url)
        self.content = response.text

    def download_img(self,imgs = []):
        for i in xrange(0,len(imgs)):
            img = imgs[i]
            response = requests.get(img)
            result = urlparse.urlparse(img,False)
            print "第%d张图片下载完成"%i
            path = result[2]
            name = path.split("/")[-1]
            with open(self.down_path+"/"+name,"wb") as f:
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
