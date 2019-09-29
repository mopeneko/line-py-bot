#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# オペレーションごとに関数を分ける
# コマンドはcommandから引っ張ってくる

import time

from akad.ttypes import ContentType, Operation, OpType

from .command import Command
from .messages import Messages
from .function import Function


class Operator(Command, Messages, Function):
    reqSeq_ids = {}

    def __init__(self):
        self.poll.addOpInterruptWithDict({
            OpType.NOTIFIED_INVITE_INTO_GROUP: self.NOTIFIED_INVITE_INTO_GROUP,
            OpType.RECEIVE_MESSAGE: self.RECEIVE_MESSAGE,
        })

        super().__init__()

    def start(self):
        while True:
            self.poll.trace(threading=True)

    def NOTIFIED_INVITE_INTO_GROUP(self, op):
        if self.line.profile.mid in op.param3:
            self.line.acceptGroupInvitation(op.param1)

    def RECEIVE_MESSAGE(self, op:Operation):
        msg = op.message

        if msg.contentType == ContentType.NONE:
            if msg.text:
                text = msg.text
                lowered = text.lower()

                if self.is_command(msg, ["help"], to_types=[1, 2]):
                    self.get_help(msg)

                if self.is_command(msg, ["test"], to_types=[1, 2]):
                    self.test(msg)

                if self.is_command(msg, ["speed"], to_types=[1, 2]):
                    self.get_speed(msg)

                if self.is_command(msg, ["reboot"]):
                    self.reboot(msg)

        if msg.contentType == ContentType.CONTACT:
            if "mid" in msg.contentMetadata:
                self.get_contact(msg, msg.contentMetadata["mid"])

        if msg.contentType == ContentType.MUSIC:
            self.send_music_profile_meta(msg)

        self.read_message(msg)
