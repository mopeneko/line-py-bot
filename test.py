#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import simplejson as json

from linepy import LINE

line = LINE("ua55b22c388b6971980af204e590fafe1:aWF0OiAxNTY5NTQyMjg5MzU4Cg==..Djdlo6mgYpZIc5UlkMAc//Sem/Q=", appType="IOS")
#line.updateVideoAndPictureProfile("profile.jpg", "profile.mp4")
line.profile.displayName = "LPB-1"
line.profile.statusMessage = "LPB\nDevelopers: 9"
line.profile.musicProfile = json.dumps({
    "name":"LPB",
    "url":"https://line.me/ti/g2/PqTYdOMscgd0_Lf3XXwoDA",
    "country":"JP",
    "artistName":"",
    "id":"mt000000000e40912d",
    "type":"mt",
    "imageUrl":"https://i.imgur.com/bWUGr1p.jpg"
})
line.updateProfile(line.profile)
