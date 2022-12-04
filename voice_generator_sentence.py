# 네이버 음성합성 Open API
import os
import sys
import urllib.request
import json


#init
client_id = ""
client_secret = ""
url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"

request = urllib.request.Request(url)
request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
request.add_header("X-NCP-APIGW-API-KEY",client_secret)

#speaker : 성우
#volume : 
#speed : integer	- 음성 속도
#pitch : 음성 피치
#emotion : 음성 감정 0: 중립, 1: 슬픔, 2: 기쁨, 3: 분노
#emotion-strength : 감정의 강도 0: 약함, 1: 보통, 2: 강함
# text : 음성 합성할 문장
#word 데이터

f = open("./json/longSentence.json", encoding='UTF-8')

jsonObject = json.load(f)

longSentence = jsonObject.get("longSentence")
for list in longSentence:
    title = list.get("title")
    contents = list.get("contents")

    for i in range(1,11) : 
        Object = contents.get(str(i))

        encText = urllib.parse.quote(Object)
        data = "speaker=nara&volume=0&speed=2&pitch=0&emotion=0&format=mp3&text=" + encText;
        response = urllib.request.urlopen(request, data=data.encode('utf-8'))
        rescode = response.getcode()

        if(rescode==200):
            response_body = response.read()
            path = './mp3/longSentence/longSentence_'+ title + '_' + str(i) + '.mp3'
            with open(path, 'wb') as f:
                f.write(response_body)
        else:
            print("Error Code:" + rescode)


