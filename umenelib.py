import os
import json
import random
import string
import urllib
from datetime import datetime

import requests
from gtts import gTTS
from imgurpython import ImgurClient


class Api:
    def imageToUrl(self, id_, secret, image_path):
        client = ImgurClient(id_, secret)
        upload = client.upload_from_path(image_path, config=None, anon=True)
        image_url = upload["link"]
        return image_url

    def shortenWithBitly(self, token, url):
        '''URL短縮(要トークン)'''
        params = {
            'access_token': token,
            'longurl': url
        }
        response = requests.get(
            'https://api-ssl.bitly.com/v3/shorten',
            params=params
        )
        shorten_url = response.json()['data']['url']
        return shorten_url

    def textToSpeechWithDocomo(
            self, apiKey, title, message, path="./", speaker="1",
            style="1", rate="1", audio_format="2"):
        '''Docomo Text To Speech API で 読み上げを行う'''
        file_path = path + title + ".wav"
        if os.path.isfile(file_path):
            return
        url = 'https://api.apigw.smt.docomo.ne.jp/crayon/v1/textToSpeech?APIKEY=%s' % apiKey
        params = {
            "Command": "AP_Synth",
            "SpeakerID": speaker,
            "StyleID": style,
            "SpeechRate": rate,
            "AudioFileFormat": audio_format,
            "TextData": message
        }
        response = requests.post(url, data=json.dumps(params))
        if response.status_code != 200:
            return
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path

    def sendLineNotify(self, token, message):
        '''Line Notifyで通知する'''
        headers = {'Authorization': 'Bearer ' + token}
        payload = {'message': message}
        requests.post(
            'https://notify-api.line.me/api/notify',
            headers=headers,
            params=payload
        )


class Other:
    def translateWithGoogle(self, word):
        '''Google翻訳APIで翻訳する'''
        headers = {
            "User-Agent": "GoogleTranslate/5.9.59004 (iPhone; iOS 10.2; ja; iPhone9,1)"
        }
        params = {
            "client": "it",
            "dt": ["t", "rmt", "bd", "rms", "qca", "ss", "md", "ld", "ex"],
            "dj": "1",
            "q": word,
            "tl": "ja"
        }
        response = requests.get(
            "https://translate.google.com/translate_a/single",
            headers=headers,
            params=params
        )
        translated_text = response.json()["sentences"][0]["trans"]
        return translated_text

    def ojichatify(self, name, emojiLevel=3, punctiuationLevel=1):
        '''文字列をおじさん風に'''
        payload = {
            'name': name,
            'emoji_level': emojiLevel,
            "punctiuation_level": punctiuationLevel
        }
        response = requests.post("https://ojichat.appspot.com/post", data=payload)
        ojichatified_text = response.json()['message']
        return ojichatified_text

    def shortenWithTinyurl(self, url):
        '''URL短縮(トークン不要)'''
        response = requests.get("http://tinyurl.com/api-create.php?url=" + url)
        shorten_url = response.text
        return shorten_url

    def generateSearchLink(self, service_name, text):
        """検索リンクを作る"""
        services = {
            "google": 'https://www.google.co.jp/search?',
            "google_image": 'https://www.google.co.jp/search?tbm=isch&q=',
            "youtube": 'https://www.youtube.com/results?search_query=',
            "yahoo": 'https://search.yahoo.co.jp/search?p=',
            "bing": 'https://www.bing.com/search?q='
        }
        if service_name not in services:
            return
        shorten_search_url = self.shortenWithTinyurl(
            services[service_name] + urllib.parse.quote(text))
        return shorten_search_url

    def drawFortune(self):
        '''おみくじをひく'''
        random_result = random.choice(["大吉", "中吉", "小吉", "末吉", "大凶", "凶"])
        return random_result

    def convertFilesize(self, file_size):
        '''ファイルサイズの単位を変換して文字列にする'''
        kb = 1024
        mb = pow(kb, 2)
        gb = pow(kb, 3)
        tb = pow(kb, 4)
        if file_size >= tb:
            target = tb
            unit = "TB"
        elif file_size >= gb:
            target = gb
            unit = "GB"
        elif file_size >= mb:
            target = mb
            unit = "MB"
        elif file_size >= kb:
            target = kb
            unit = "KB"
        else:
            target = 1
            unit = "B"
        new_file_size = file_size / target
        converted_text = f"{new_file_size:.1f}{unit}"
        return converted_text

    def generateRandCharacter(self, quantity=6):
        '''指定した字数のランダムな文字列を作る'''
        random_string = ''.join(
            random.choices(string.ascii_letters + string.digits, k=quantity)
        )
        return random_string

    def convertCiplex(self, word):
        '''簡易暗号化/複合化'''
        string_list = []
        for string in word:
            if string.islower():
                string_list.append(chr(219 - ord(string)))
            else:
                string_list.append(string)
        converted_text = "".join(string_list)
        return converted_text

    def convertLineTime(self, time):
        '''Line Time を 日付文字列にする'''
        date_string = datetime.fromtimestamp(time / 1000).strftime("%Y/%m/%d %H:%M:%S")
        return date_string

    def generateMusicMeta(self, name, track_id="mb00000000016d2e75", artist="", imageurl="https://pixabay.com/images/id-3386570/", url="https://www.google.com/"):
        '''音楽型のMetadataを作る'''
        music_meta = {
            "id": track_id,
            "name": name,
            "artistName": artist,
            "imageUrl": imageurl,
            "url": url,
            "type": "mt",
            "country": "JP"
        }
        return music_meta

    def generateRealFace(self, savename, path="./"):
        '''AIが作成した三次元の存在しない顔の画像をDLする'''
        headers = {
            'Host': 'thispersondoesnotexist.com',
            'User-Agent': r'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': r'en,en-US;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': r'max-age=0',
            'TE': 'Trailers'
        }
        response = requests.get(
            'https://thispersondoesnotexist.com/image',
            headers=headers,
            stream=True
        )
        with open('%s%s.jpeg' % (path, savename), 'wb') as f:
            f.write(response.content)

    def generateVirtualFace(self, savename, path="./"):
        '''AIが作成した二次元の画像をDLする'''
        random_num = random.randint(0, 60000)
        url = f"https://www.thiswaifudoesnotexist.net/example-{random_num}.jpg"

        response = requests.get(url)
        with open('%s%s.jpeg' % (path, savename), 'wb') as f:
            f.write(response.content)

    def textToSpeechWithGoogle(self, text, savename=None, lang="en", path="./"):
        '''Google API で読み上げを行う'''
        goo = gTTS(text=text, lang=lang)
        if savename is None:
            savename = text
        goo.save('%s%s.mp3' % (path, savename))


if __name__ == "__main__":
    lib = Other()
    print(lib.drawFortune())
    print(lib.convertFilesize(12041204))
    print(lib.generateRandCharacter(20))
    print(lib.convertCiplex("UmeneLib"))
    print(lib.convertCiplex(lib.convertCiplex("UmeneLib")))
    print(lib.convertLineTime(11100000))
    print(lib.generateMusicMeta("UmeneLib"))
    print(lib.shortenWithTinyurl("http://gochiusa.com"))
    print(lib.generateSearchLink("google", "Kafuu chino"))
    print(lib.translateWithGoogle("Kafuu chino"))
    print(lib.ojichatify("香風智乃"))
    print(lib.generateVirtualFace("Kafuu chino"))
    print(lib.generateRealFace("Kafuu chino"))
    print(lib.textToSpeechWithGoogle("Kafuu chino", "chino"))
