# -*- coding: utf-8 -*-
'''
Created on 2011-9-20
@author: slieer

http://hi.baidu.com/xjtukanif/blog/item/009535d98c7d4c6ad0164e88.html
'''
from twisted.cred import portal, checkers, credentials
from twisted.cred.error import UnauthorizedLogin
from twisted.protocols.basic import LineReceiver
from twisted.internet import protocol, reactor, defer
from zope.interface import Interface, implements

USER_INFO = {'kanif':{'password':'123456', 'money':1000, 'rate':0.1}
            }

class PasswordChecker(object):
    implements(checkers.ICredentialsChecker)
    credentialInterfaces = (credentials.IUsernamePassword,)
    '''
        用户校验通过后， 返回对应的avatarID， 该ID可以和用户名不同
    '''
    def requestAvatarId(self, credentials):
        if credentials.username in USER_INFO and credentials.password == USER_INFO[credentials.username]['password']:
            print 'credentials.password %s' %credentials.password
            return credentials.username
        else:
            raise UnauthorizedLogin('invalid user or password')

class IUserMoneyAvatar(Interface):
        "nothing"

class UserMoneyAvatar():
    def __init__(self, username, money):
        self.username = username
        self.money = money

# portal中使用的中间件，根据接口类型返回不同的avatar
class UserBankRealm:
    implements(portal.IRealm)
    '''
        avatarId: 用于识别用户唯一性的ID
        mind: 一般为None，可根据自己需要使用， 目前只有PB中使用
        interfaces: 一个list， 用于决定返回的avatar类型, 通常只有一个元素
    '''
    def requestAvatar(self, avatarId, mind, *interfaces):
        if IUserMoneyAvatar in interfaces:
            return (IUserMoneyAvatar, UserMoneyAvatar(avatarId, USER_INFO[avatarId]['money']), None)
        else:
            raise KeyError('None of the requested interfaces is supported')

class MoneyProtocol(LineReceiver):
    delimiter = '\n'

    def lineReceived(self, line):
        print '----------------%s' %line
        user, passwod = line.strip().split()
        creds = credentials.UsernamePassword(user, passwod)
        #得到用户名和密码后使用portal的login函数进行用户验证
        try:
            self.factory.portal.login(creds, None, IUserMoneyAvatar).addCallback(self.loginSuc).addErrback(self.loginErr)
        except:
            import traceback
            print traceback.format_exc()
    
    #用户验证成功后的信息包括 avatar类型， avatar实例和退出执行程序
    def loginSuc(self, avatarInfo):
        avatarInterface, avatar, logout = avatarInfo
        self.sendLine('%s login suc.Your money is %s' % (avatar.username, avatar.money))

    def loginErr(self, result):
        self.sendLine('Failed: %s' % result.value)

class BankFactory(protocol.ServerFactory):
    protocol = MoneyProtocol
    def __init__(self, portal):
        self.portal = portal

p = portal.Portal(UserBankRealm())
p.registerChecker(PasswordChecker())
reactor.listenTCP(8003, BankFactory(p))
reactor.run()

