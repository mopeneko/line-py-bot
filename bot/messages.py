#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# linepyで足りないメッセージの関数を補う

import re

import simplejson as json
from akad.ttypes import Message


class Messages:

    def __init__(self):
        pass

    def sendMessageWithMention(self, to, text):
        mentionees = []
        for matched in self.mention_mid_pattern.finditer(text):
            start, end = matched.span()
            mid = matched.group()[1:]
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
