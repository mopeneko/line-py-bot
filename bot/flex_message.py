#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# flexMessageの処理をここに書く
def get_youtubeinfo_flex(word,developerKey="token"):
    youtube = build("youtube", "v3",developerKey=developerKey)
    search_response = youtube.search().list(q=str(word),part="id,snippet",maxResults="50").execute()
    order = {}
    for num,result in enumerate(search_response.get("items", [])):
        if result["id"]["kind"] == "youtube#video":
            order[num] = [result["snippet"]["title"], result["id"]["videoId"], result["snippet"]["channelTitle"]]
    data = {
            "type": "template",
            "altText": "youtube",
            "template": {
                "type": "carousel",
                "columns": [
                    {
                        "thumbnailImageUrl": "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(order[1][1]),
                        "text": "{0}\n{1}".format(order[1][2]), order[1][0])[:60],
                        "defaultAction": {
                            "type": "uri",
                            "uri": "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(order[1][1]),
                        },
                        "actions": [
                            {
                                "type": "uri",
                                "label": "動画はこちらから",
                                "uri": "https://www.youtube.com/watch?v={}".format(order[1][1]),
                            }
                        ]
                    },
                    {
                        "thumbnailImageUrl": "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(order[2][1]),
                        "text": "{0}\n{1}".format(order[2][2]), order[2][0])[:60],
                        "defaultAction": {
                            "type": "uri",
                            "uri": "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(order[2][1]),
                        },
                        "actions": [
                            {
                                "type": "uri",
                                "label": "動画はこちらから",
                                "uri": "https://www.youtube.com/watch?v={}".format(order[2][1]),
                            }
                        ]
                    },
                    {
                        "thumbnailImageUrl": "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(order[3][1]),
                        "text": "{0}\n{1}".format(order[3][2]), order[3][0])[:60],
                        "defaultAction": {
                            "type": "uri",
                            "uri": "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(order[3][1]),
                        },
                        "actions": [
                            {
                                "type": "uri",
                                "label": "動画はこちらから",
                                "uri": "https://www.youtube.com/watch?v={}".format(order[3][1]),
                            }
                        ]
                    },
                    {
                        "thumbnailImageUrl": "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(order[4][1]),
                        "text": "{0}\n{1}".format(order[4][2]), order[4][0])[:60],
                        "defaultAction": {
                            "type": "uri",
                            "uri": "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(order[4][1]),
                        },
                        "actions": [
                            {
                                "type": "uri",
                                "label": "動画はこちらから",
                                "uri": "https://www.youtube.com/watch?v={}".format(order[4][1]),
                            }
                        ]
                    },
                    {
                        "thumbnailImageUrl": "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(order[5][1]),
                        "text": "{0}\n{1}".format(order[5][2]), order[5][0])[:60],
                        "defaultAction": {
                            "type": "uri",
                            "uri": "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(order[5][1]),
                        },
                        "actions": [
                            {
                                "type": "uri",
                                "label": "動画はこちらから",
                                "uri": "https://www.youtube.com/watch?v={}".format(order[5][1]),
                            }
                        ]
                    },
                    {
                        "thumbnailImageUrl": "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(order[6][1]),
                        "text": "{0}\n{1}".format(order[6][2]), order[6][0])[:60],
                        "defaultAction": {
                            "type": "uri",
                            "uri": "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(order[6][1]),
                        },
                        "actions": [
                            {
                                "type": "uri",
                                "label": "動画はこちらから",
                                "uri": "https://www.youtube.com/watch?v={}".format(order[6][1]),
                            }
                        ]
                    },
                    {
                        "thumbnailImageUrl": "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(order[7][1]),
                        "text": "{0}\n{1}".format(order[7][2]), order[7][0])[:60],
                        "defaultAction": {
                            "type": "uri",
                            "uri": "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(order[7][1]),
                        },
                        "actions": [
                            {
                                "type": "uri",
                                "label": "動画はこちらから",
                                "uri": "https://www.youtube.com/watch?v={}".format(order[7][1]),
                            }
                        ]
                    }
                ],
                "imageAspectRatio": "rectangle",
                "imageSize": "cover"
            }
       }
    return data
