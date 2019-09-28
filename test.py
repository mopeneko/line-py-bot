#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import simplejson as json

from bot import LinePyBot

line = LinePyBot("ua55b22c388b6971980af204e590fafe1:aWF0OiAxNTY5NTQyMjg5MzU4Cg==..Djdlo6mgYpZIc5UlkMAc//Sem/Q=")
line.updateVideoAndPictureProfile()
line.profile.displayName = "LPB-1"
line.profile.statusMessage = "LPB\nDevelopers: 9"
line.profile.musicProfile = {
    "name":"Wasted Nights",
    "url":"https://line.me/ti/g2/PqTYdOMscgd0_Lf3XXwoDA",
    "country":"JP",
    "artistName":"LPB",
    "id":"mt000000000e40912d",
    "type":"mt",
    "imageUrl":"https://i.imgur.com/bWUGr1p.jpg"
}
