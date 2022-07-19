from django.db import models

# Create your models here.
class yeosuRestaurant(models.Model): #이름,위치,위도,경도
    name=models.CharField(max_length=15) 
    location=models.CharField(max_length=50, default='')

    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)

class jeonjuRestaurant(models.Model): #이름,위치,위도,경도
    name=models.CharField(max_length=15) 
    location=models.CharField(max_length=50, default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)


class product(models.Model): #이름,가격,설명
    name=models.CharField(max_length=200) 
    price=models.IntegerField(null=True)
    description=models.TextField() 
    def __str__(self):
        return self.name


class productdetail(models.Model): #이름,가격,설명
    name=models.CharField(max_length=200) 
    price=models.IntegerField(null=True)
    description=models.TextField() 
    path=models.TextField() 
    def __str__(self):
        return self.name

class wandoRestaurant(models.Model): #이름,위치,위도,경도
    name=models.CharField(max_length=15) 
    location=models.CharField(max_length=50, default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)

class wandoVisit(models.Model): #이름,위치,위도,경도
    name=models.CharField(max_length=15) 
    location=models.CharField(max_length=50, default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)

class yeosuVisit(models.Model): #이름,위치,위도,경도
    name=models.CharField(max_length=15) 
    location=models.CharField(max_length=50, default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)

class jeonjuVisit(models.Model): #이름,위치,위도,경도
    name=models.CharField(max_length=15) 
    location=models.CharField(max_length=50, default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)

class goheungVisit(models.Model): #이름,위치,위도,경도
    name=models.CharField(max_length=15) 
    location=models.CharField(max_length=50, default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)

class gwangyangVisit(models.Model): #이름,위치,위도,경도
    name=models.CharField(max_length=15) 
    location=models.CharField(max_length=50, default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)

class goheungRestaurant(models.Model): #이름,위치,위도,경도
    name=models.CharField(max_length=15) 
    location=models.CharField(max_length=50, default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)

class gwangyangRestaurant(models.Model): #이름,위치,위도,경도
    name=models.CharField(max_length=15) 
    location=models.CharField(max_length=50, default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)
