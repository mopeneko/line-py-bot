#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# linepyで足りないメッセージの関数を補う

import re

import simplejson as json
from akad.ttypes import Message


class Messages:

    def __init__(self):
        self.mention_mid_pattern = re.compile(r"@[ua-zA-z0-9]{33}")

    def get_mention_metadata(self, text):
        """何故か文字数のカウントが異なるため使用不可"""
        mentionees = []
        count = len(self.mention_mid_pattern.findall(text))
        flag = 0
        for i in range(count):
            matched = self.mention_mid_pattern.search(text, flag)
            start = matched.span()[0]
            mid = matched.group()[1:]

            displayName = self.line.getContact(mid).displayName
            string_name = f"@{displayName}"
            oend = start + 34
            end = start + len(string_name)

            text = text[:start] + string_name + text[oend:]

            flag = end

            mentionees.append({"S": str(start), "E": str(end), "M": mid})
        return text, {'MENTION': json.dumps({"MENTIONEES": mentionees})}

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
