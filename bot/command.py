#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# コマンドをここにかく

import os
import time

from akad.ttypes import Message


class Command:

    def __init__(self):
        pass

    def is_command(self, msg:Message, cmds:list, prefix:list=[], typ:str="is", to_types:list=[0,1,2]) -> bool:

        if msg.text and msg.toType in to_types:
            text  = msg.text
            lower = text.lower()

            if prefix:
                cmds = [p+c for c in cmds for p in prefix]

            if typ == "is" and lower in cmds:
                return True
            elif typ == "in":
                for cmd in cmds:
                    if cmd in lower:
                        return True
            elif typ == "st":
                for cmd in cmds:
                    if lower.startswith(cmd):
                        return True
        return False

    def get_help(self, msg):
        self.sendMessage(msg.to, f"[help]" + "\n" \
                                 f"[test]" + "\n" \
                                 f"[speed]")

    def test(self, msg):
        self.sendMessage(msg.to, "Ready 未定 Bot")

    def get_speed(self, msg):
        start_time = time.time()
        _msg = self.sendMessage(msg.to, "...")
        process_time = time.time() - start_time
        receive_time = (_msg.createdTime - msg.createdTime) / 1000
        self.sendMessage(msg.to, f"[recv]: {receive_time:.5f}" + "\n" \
                                 f"[send]: {process_time:.5f}")

    def reboot(self, msg):
        self.sendMessage(msg.to, "...")
        os.execvp("python3", ["python3", "main.py", msg.to])
