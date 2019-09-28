#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# linepyで足りないメッセージの関数を補う

import re

import simplejson as json

from akad.ttypes import Message


class Messages:

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

        return self.line.talk.sendMessage(0, msg)
