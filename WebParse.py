# -*- coding: UTF-8 -*-
from HTMLParser import HTMLParser
#from htmlentitydefs import name2codepoint

class ImgHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.img = []

    def handle_starttag(self, tag, attrs):
        # print "Encountered a start tag:", tag
        if tag == "img":
            # print attrs
            for kv in attrs:
                if kv[0] == "src":
                    self.img.append(kv[1])

'''
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data
    def handle_comment(self, data):
        print "Comment  :", data

    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c

    def handle_decl(self, data):
        print "Decl     :", data
'''

class DLParser(object):


    def __init__(self):
        self.img = []
        self.parse = ImgHTMLParser()

    def feed(self,content):
        self.parse.feed(content)
        self.img = self.parse.img
    def close(self):
        self.parse.close()

dlparser =  DLParser()

if __name__ == "__main__":
    pass
