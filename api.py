# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys

import urllib.request
import json 

client_id = "lxJGkOeMAIMOo6Tf5dZx"
client_secret = "Y79oJ07GkN"

location = "완도"
encText = urllib.parse.quote(location+" 맛집") #검색어 

url = "https://openapi.naver.com/v1/search/local.json?sort=comment&query=" + encText+"&display=5" # json형식:리뷰순, 5개씩 보여주기


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id) #내가 누구인지 헤더에 보내줌
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request) #응답 객체
rescode = response.getcode() #응답 코드
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8')) #한국말
else:
    print("Error Code:" + rescode)

resdata = response_body.decode('utf-8') #데이터, 한국말

#응답받은 파일을 json파일로 내보내기
with open('wando.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(resdata, ensure_ascii=False))

pydata = json.loads(resdata)
data = pydata['items'] #array 형식으로 데이터 가져옴
print(data[0])  

