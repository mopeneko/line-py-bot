#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from bot import LinePyBot

line = LinePyBot(os.environ.get("AUTHTOKEN"))
line.start()
