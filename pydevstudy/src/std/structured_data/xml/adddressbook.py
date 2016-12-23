# -*- coding: utf-8 -*-

'''
Created on 2011-9-10
@author: slieer
http://blog.csdn.net/zzllabcd/article/details/3070120
'''
from xml.sax import make_parser, SAXException
from xml.sax.handler import ContentHandler

class PhoneContentHandler(ContentHandler):#定义一个handler类
    def __init__(self, name):
        self.look_for = name
        self.is_name, self.is_mobile = None, None#定义两个flag
        self.buffer = ''
    def startElement(self, name, attrs):
        if name == 'phone' and attrs.get('type') == 'mobile':# 判断师傅是phone tag,并且属性名是type, 属性值是mobile(注:我在2.52里面查reference看到应为attrs是属于Attributes 抽象类的对象,所以,他的发应该是attrs.getValue('type') == 'mobile' )
            self.is_mobile = 1
        elif name == 'name':  
            self.is_name = 1
    def endElement(self, name):
        if self.is_name:#判断是否是tag的结尾.
            self.current_name = self.buffer.strip()#得到tag里面的内容,这个是unicode的string,根据自己要的字符集可以用encode方法来转换一下
            self.buffer = ''
            self.is_name = None
        elif self.is_mobile and self.current_name == self.look_for:
            self.mobile = self.buffer
            raise SAXException('Found mobile phone') # stop parsing
    def characters(self, chars):
        if self.is_name or self.is_mobile:  
            self.buffer += chars

def find_mobile_phone(name):
    handler = PhoneContentHandler(name)
    parser = make_parser()
    parser.setContentHandler(handler)
    try:
        parser.parse(open('addressbook.xml'))
    except SAXException:
        return handler.mobile
    return None

if __name__ == '__main__':
    import sys
    name = ' '.join(sys.argv[1:])
    phone = find_mobile_phone(name)
    if phone:
        print('Mobile phone is', phone)
    else:
        print('No mobile phone found for', name)
