from django.db import models

# Create your models here.
class ComicInfo(models.Model):
    comic_name=models.IntegerField()
    bubble_id=models.IntegerField()
    person_num=models.IntegerField()
    bubble_num=models.IntegerField()
    availability=models.IntegerField()
    utter1=models.CharField(max_length=1000)
    utter2=models.CharField(max_length=1000)
    x1=models.FloatField(default=0)
    y1=models.FloatField(default=0)
    x2=models.FloatField(default=0)
    y2=models.FloatField(default=0)
    pn=models.IntegerField(default=0)
    
    def __str__(self):
        return "<{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}>".format(self.comic_name,self.bubble_id,self.person_num,self.bubble_num,self.availability,self.utter1,self.utter2,self.x1,self.y1,self.x2,self.y2,self.pn)

class Doing(models.Model):
    comic_name=models.IntegerField()
    bubble_id=models.IntegerField()
    flag=models.IntegerField(default=0)
    
    def __str__(self):
        return "<{0},{1},{2}>".format(self.comic_name,self.bubble_id,self.flag)

class Mood(models.Model):
    mood_id=models.IntegerField()
    mood_name=models.CharField(max_length=100)

    def __str__(self):
        return "<{0},{1}>".format(self.mood_id,self.mood_name)

class Title(models.Model):
    comic_id=models.IntegerField()
    comic_name=models.CharField(max_length=400)

    def __str__(self):
        return "<{0},{1}>".format(self.comic_id,self.comic_name)
