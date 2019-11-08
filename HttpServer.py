
#coding=utf8

import httplib
import md5
import urllib
import random

class Singleton(type):
    def __init__(self,name,bases,class_dict):
        super(Singleton,self).__init__(name,bases,class_dict)
        self._instance=None
    def __call__(self,*args,**kwargs):
        if self._instance is None:
            self._instance=super(Singleton,self).__call__(*args,**kwargs)
        return self._instance

class HttpServer(object):
    __metaclass__=Singleton 

    def __init__(self):
        self.appid = 'YOUR_APP_ID'
        self.key = 'YOUR_APP_KEY'
        self.url = '/api/trans/vip/translate'
        self.fromType = 'auto'
        self.toType = 'zh'        

    def strCheck(self, content):
        if len(content) >= 2000:
            print 'can not translate too long'
            return -1
        elif len(content) <= 0:
            print 'please input sth...'
            return -2
        return 0

    def querry(self, content):
        if self.strCheck(content) != 0:
            return -1

        content = content.rstrip()
        content = content.lstrip()

        if self.strCheck(content) != 0:
            return -2

        salt = random.randint(32768, 65536)
        sign = self.appid + content + str(salt) + self.key
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        self.httpClinet = httplib.HTTPConnection('api.fanyi.baidu.com')

        querryUrl = self.url + '?appid=' + self.appid + '&q=' + urllib.quote(content) + '&from=' + self.fromType + '&to=' + self.toType + '&salt=' + str(salt) + '&sign=' + sign

        try:
            self.httpClinet.request('GET', querryUrl)

            response = self.httpClinet.getresponse()
            
            return response.read()
        except Exception, e:
            return ('error',e)
        finally:
            self.httpClinet.close()
