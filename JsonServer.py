#coding=utf8

import json

class Singleton(type):
    def __init__(self,name,bases,class_dict):
        super(Singleton,self).__init__(name,bases,class_dict)
        self._instance=None
    def __call__(self,*args,**kwargs):
        if self._instance is None:
            self._instance=super(Singleton,self).__call__(*args,**kwargs)
        return self._instance

class JsonDecode(object):
        __metaclass__=Singleton 

        def decode(self, content):
            if content == -1 or content == -2:
                return 'please input again'
            js = json.loads(content)
            try:
                result = js['trans_result']
                return result[0]['dst']
            except Exception, e:
                print js
                return 'error'
            
