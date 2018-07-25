#! /usr/bin/python
#-*- coding: utf-8 -*-
import ConfigParser
import os.path

import urllib2

config = ConfigParser.ConfigParser()
config.read('config.ini')
site = config.get("cdn","site")
base_path = config.get("cdn","path")

def run():
    print('读取 %s 下面的所有mp4文件'% (base_path,))
    for (root, dirs, files) in os.walk(base_path):
        for file in files:
            path = os.path.join(root, file)
            if file.endswith('.mp4'):
                isExists(path)

def isExists(filePath):
    url = filePath.replace(base_path, '')
    url = site + url
    try:
        print('准备请求'+url)
        response =  urllib2.urlopen(url)
        code = response.getcode()
        if code == 200:
            print('视频:%s, cdn存在%s, 准备进行删除' % (filePath, url) )
            os.remove(filePath)

    except urllib2.HTTPError, e:
        print('视频:%s, cdn不存在存在' % (filePath,) )

if __name__ == '__main__':
    run()