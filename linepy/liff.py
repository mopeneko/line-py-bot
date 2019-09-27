# -*- coding: utf-8 -*-
from akad.ttypes import *
import json, requests

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin


class Liff(object):
    isLogin = False

    def __init__(self):
        self.isLogin = True
        self.allowLiff()

    @loggedIn
    def allowLiff(self, channelId=None):
        if not channelId:
            channelId = "1649631642"
        url = 'https://access.line.me/dialog/api/permissions'
        data = {'on': ['P','CM'], 'off': []}
        headers = {
            'X-Line-Access': self.authToken,
            'X-Line-Application': self.server.APP_NAME,
            'X-Line-ChannelId': channelId, #'1603968955',
            'Content-Type': 'application/json'
        }
        r = requests.post(url, json=data, headers=headers)
        return r

    @loggedIn
    def issueLiffView(self, to):
        az = LiffChatContext(to)
        ax = LiffContext(chat=az)
        lf = LiffViewRequest('1649631642-4vqAYRMq', ax)
        return self.liff.issueLiffView(lf)

    @loggedIn
    def sendFlex(self, to, data):
        token = self.issueLiffView(to)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [data]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res

    @loggedIn
    def issueLiffSquareView(self, to):
        az = LiffSquareChatContext(to)
        ax = LiffContext(squareChat=az)
        lf = LiffViewRequest('1649631642-4vqAYRMq', ax)
        return self.liff.issueLiffView(lf)

    @loggedIn
    def postSquareTemplate(self, to, data):
        token = self.issueLiffSquareView(to)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {
            'messages': [data]
        }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        return res
