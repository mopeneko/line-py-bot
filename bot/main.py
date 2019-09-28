#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from linepy import LINE, OEPoll
from akad.ttypes import Message

from .operator import Operator


class LinePyBot(Operator):
    """
    Usage:
        from bot import LinePyBot
        line = LinePyBot(authToken)
        line.start()
    """

    def __init__(self, token:str):
        self.line = LINE(token, appType="IOS", customThrift=True)
        self.poll = OEPoll(self.line)
        self.mid = self.line.profile.mid

        self.check_restart()
        super().__init__()

    def check_restart(self):
        argv = sys.argv
        if len(argv) >= 2:
            to = argv[1]
            self.sendMessage(to, "再起動しました")
