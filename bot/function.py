#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# commandで使用する処理をこっちに書く or その他関数

from datetime import datetime

import simplejson as json

from akad.ttypes import MIDType
from .japanese import get_contact_type, get_contact_status


class Function:

    def read_message(self, msg):
        if msg.toType == MIDType.USER:
            self.line.sendChatChecked(msg._from, msg.id)
        else:
            self.line.sendChatChecked(msg.to, msg.id)

    def get_line_time(self, line_time, string):
        return datetime.fromtimestamp(line_time / 1000).strftime(string) if line_time else ""

    def get_string(self, string):
        return string if string else ""

    def send_contact_info(self, msg, mid):
        contact = self.line.getContact(mid)

        mid = contact.mid
        # added_time = self.get_line_time(contact.createdTime, "%Y-%m-%d %H:%M:%S")
        # contact_type = get_contact_type(contact.type)
        # contact_status = get_contact_status(contact.status)
        # ContactRelationは多分正しくない
        name = contact.displayName
        # phonetic_name = contact.phoneticName if contact.phoneticName else ""
        picture = f"https://obs-jp.line-apps.com/{contact.pictureStatus}" if contact.pictureStatus else ""
        # conatct.statusMessage
        # handle_name = self.get_string(contact.displayNameOverridden)  # コテハン
        # favorite_time = self.get_line_time(contact.favoriteTime, "%Y-%m-%d %H:%M:%S")
        account_type = "公式アカウント "if contact.capableBuddy else "通常アカウント"
        # contact.musicProfile
        video = f"https://obs-jp.line-apps.com/{contact.pictureStatus}/vp" if contact.videoProfile else ""

        return self.sendMessage(msg.to, f"[MID]\n{mid}" + "\n\n" \
                                        f"[アカウントの種類]\n{account_type}" + "\n\n" \
                                        f"[名前]\n{name}" + "\n\n" \
                                        f"[プロフィール画像]\n{picture}" + "\n\n" \
                                        f"[プロフィール動画]\n{video}" + "\n\n")

    def send_music_profile_meta(self, msg):
        name = msg.contentMetadata["text"]
        url = msg.contentMetadata["i-linkUri"]  # a-linkUri, linkUri
        artistName = msg.contentMetadata["subText"]
        id = msg.contentMetadata["id"]

        imageUrl = msg.contentMetadata["previewUrl"]
        size_end = imageUrl.rfind("/")
        imageUrl = imageUrl[:size_end] + "/m1043x1043"

        """
        {
            'previewUrl': 'https://obs.line-scdn.net/r/musicjp/c/c07a219ca5060t0a736b45/v256x256',
            'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320',
            'type': 'mt',
            'subText': 'back number',
            'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android',
            'a-packageName': 'jp.linecorp.linemusic.android',
            'countryCode': 'JP',
            'a-linkUri': 'linemusic://open?target=track&item=mb0000000001774fc5&subitem=mt000000000e40912d&cc=JP&from=lc&v=1',
            'i-linkUri': 'linemusic://open?target=track&item=mb0000000001774fc5&subitem=mt000000000e40912d&cc=JP&from=lc&v=1',
            'text': 'こぼれ落ちて',
            'id': 'mt000000000e40912d',
            'linkUri': 'https://music.line.me/launch?target=track&item=mb0000000001774fc5&subitem=mt000000000e40912d&cc=JP&from=lc&v=1'
        }
        """

        music_meta = json.dumps({
            "name": name,
            "url": url,
            "country":"JP",
            "artistName": artistName,
            "id": id,
            "type": "mt",
            "imageUrl": imageUrl
        }, ensure_ascii=False, indent=4)

        return self.sendMessage(msg.to, music_meta)
