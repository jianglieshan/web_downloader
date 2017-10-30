# -*- coding: UTF-8 -*-
import json
class WebConstant(object):
    download_path = ""
    web_url = ""
    @staticmethod
    def load_config():
        with open("config.json","r") as f:
            jsonStr = f.read()
            config = json.loads(jsonStr)
            WebConstant.download_path = config["download_path"]
            WebConstant.web_url = config["web_url"]

if __name__ == "__main__":
    WebConstant.load_config()
