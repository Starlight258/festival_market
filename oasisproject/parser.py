import json 

import sys,io,os 
import django 

#장고 불러오기
sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oasisproject.settings")
django.setup() 

from myapp.models import goheungRestaurant 

#파싱 함수
def parsing(): #스크랩한 문자열을 json파일로 바꾼후에 수행하기
    with open('goheung.json', encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)

    post = []

    for i in range(5):
        post.append({
            'name':json_data['items'][i]['title'],
            'loc': json_data['items'][i]['roadAddress'],
            'lat':json_data['items'][i]['mapx'],
            'lon':json_data['items'][i]['mapy']
        })
    return post

if __name__=='__main__':
    post = parsing() #파싱한 후에
    # db에 저장
    for i in range(len(post)):
        goheungRestaurant(
            name=post[i]['name'],
            location=post[i]['loc'],
            latitude=post[i]['lat'],
            longitude=post[i]['lon']
        ).save()