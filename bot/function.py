#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# commandで使用する処理をこっちに書く or その他関数

from datetime import datetime

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

    def get_contact(self, msg, mid):
        contact = self.line.getContact(mid)

        mid = contact.mid
        added_time = self.get_line_time(contact.createdTime, "%Y-%m-%d %H:%M:%S")
        contact_type = get_contact_type(contact.type)
        contact_status = get_contact_status(contact.status)
        # ContactRelationは多分正しくない
        name = contact.displayName
        # phonetic_name = contact.phoneticName if contact.phoneticName else ""
        picture = f"https://obs-jp.line-apps.com/{contact.pictureStatus}" if contact.pictureStatus else ""
        # conatct.statusMessage
        handle_name = self.get_string(contact.displayNameOverridden)  # コテハン
        favorite_time = self.get_line_time(contact.favoriteTime, "%Y-%m-%d %H:%M:%S")
        account_type = "公式アカウント "if contact.capableBuddy else "通常アカウント"
        # contact.musicProfile
        video = f"https://obs-jp.line-apps.com/{contact.pictureStatus}/vp" if contact.videoProfile else ""

        return self.sendMessage(msg.to, f"[MID]\n{mid}" + "\n\n" \
                                        f"[アカウントの種類]\n{account_type}" + "\n\n" \
                                        f"[名前]\n{name}" + "\n\n" \
                                        f"[固定ハンドルネーム]\n{handle_name}" + "\n\n" \
                                        f"[プロフィール画像]\n{picture}" + "\n\n" \
                                        f"[プロフィール動画]\n{video}" + "\n\n" \
                                        f"[関係]\n{contact_status}" + "\n\n" \
                                        f"[追加方法]\n{contact_type}" + "\n\n" \
                                        f"[追加した日時]\n{added_time}" + "\n\n" \
                                        f"[お気に入りにした日時]\n{favorite_time}")
