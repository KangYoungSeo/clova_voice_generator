import os
import sys
import json

f = open("./json/shortSentence.json", encoding='UTF-8')

jsonObject = json.load(f)

shortSentence = jsonObject.get("shortSentence")
for list in shortSentence:
    title = list.get("title")
    print("<" + title + ">")
    contents = list.get("contents")

    for i in range(1,2) : 
        Object = contents.get(str(i))
        print(Object)
        


# print(kor)
