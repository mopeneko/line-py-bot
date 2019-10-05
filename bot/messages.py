#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# linepyで足りないメッセージの関数を補う

import re
from base64 import b64encode
import time

import simplejson as json
import requests

from akad.ttypes import Message, ContentType, FeatureType


class Messages:
    reqSeq={}

    def sendMessageWithMention(self, to, text, mids):
        # TODO: ユーザーの名前がデコ文字の場合の対応
        """
        params
            text: 'hogehoge @{}'
            mids: list
        """
        if text.count("@{}") != len(mids):
            raise Exception

        mentionees = []
        names = list(map(lambda mid: self.line.getContact(mid).displayName, mids))
        text = text.format(*names)

        for name, mid in zip(names, mids):
            start = text.find("@" + name)
            end = start + len("@" + name)
            mentionees.append({"S": str(start), "E": str(end), "M": mid})

        contentMetadata = {'MENTION': json.dumps({"MENTIONEES": mentionees})}
        return self.sendMessage(to, text, contentMetadata=contentMetadata)

    def sendMessage(self, to, text=None, location=None, contentType=0, contentMetadata={}, relatedMessageId=None):
        msg = Message()
        msg.to = to
        msg.text = text
        msg.location = location
        msg.contentType = contentType
        msg.contentMetadata = contentMetadata

        if relatedMessageId:
            msg.relatedMessageId = relatedMessageId
            msg.relatedMessageServiceCode = 1
            msg.messageRelationType = 3

        if to not in self.reqSeq:
            self.reqSeq[to] = 0
        self.reqSeq[to] += 1

        return self.line.talk.sendMessage(self.reqSeq, msg), self.reqSeq[to]

    def sendImage(self, msg, path):
        reqSeq = self.sendMessage(msg.to, contentType=ContentType.IMAGE)[1]

        params = b64encode(json.dumps({
            "reqseq": str(reqSeq),
            "ver": "1.0",
            "tomid": msg.to,
            "type": "image",
            "oid": "reqseq",
            "name": path,
            "cat": "original"
        }).encode("utf-8"))

        f = open(path, 'rb')
        data = f.read()

        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/octet-stream',
            'X-Line-Application': self.line.server.APP_NAME,
            'Connection': 'Keep-Alive',
            'x-obs-params': params,
            'X-Line-Access': self.line.acquireEncryptedAccessToken(FeatureType.OBS_GENERAL),
            'X-Line-Carrier': self.line.server.CARRIER,
            'Accept-Language': 'ja-jp',
            'User-Agent': f'LI/{self.line.server.APP_VER} iPhone8,1 {self.line.server.SYSTEM_VER}',
            'Accept-Encoding': 'gzip',
            'Content-Length': str(len(data)),
        }

        r = requests.post("https://obs-jp.line-apps.com:443/r/talk/m/reqseq", headers=headers, data=data)

        return r.headers
