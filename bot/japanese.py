#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# akad.ttypesで定義されているものを日本語にする (例: ContactType)


def get_contact_type(_type):
    if not _type:
        return ""
    contact_type = {
        0: "MID",
        1: "電話番号",
        2: "メールアドレス",
        3: "LINEID",
        4: "PROXIMITY",
        5: "グループ",
        6: "USER",
        7: "QRコード",
        8: "PROMOTION_BOT",
        9: "メッセージから",
        10: "友達リクエスト",
        128: "REPAIR",
        2305: "Facebook",
        2306: "SINA",
        2307: "RENREN",
        2308: "FEIXIN",
        2309: "BBM",
        11: "知り合いかも",  # あってるかわからん
    }
    return contact_type[_type]

def get_contact_status(status):
    if not status:
        return ""
    contact_status = {
        0: "末追加",
        1: "友達",
        2: "ブロック(友達)",
        3: "知り合いかも",
        4: "ブロック(知り合いかも)",
        5: "削除済",
        6: "ブロック(削除済)",
    }
    return contact_status[status]
