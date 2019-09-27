#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# commandで使用する処理をこっちに書く or その他関数

from akad.ttypes import MIDType


class Function:

    def __init__(self):
        pass

    def read_message(self, msg):
        if msg.toType == MIDType.USER:
            self.line.sendChatChecked(msg._from, msg.id)
        else:
            self.line.sendChatChecked(msg.to, msg.id)
