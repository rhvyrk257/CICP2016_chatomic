from django.db import models

# Create your models here.
class ComicInfo(models.Model):
    file_name=models.CharField(max_length=200)
    path_name=models.CharField(max_length=200)
    person_num=models.IntegerField()
    bubble_num=models.IntegerField()
    availability=models.IntegerField()
    utter=models.CharField(max_length=1000)
    pn=models.IntegerField()
    def __str__(self):
        return "<{0},{1},{2},{3},{4},{5},{6}>".format(self.file_name,self.path_name,self.person_num,self.bubble_num,self.availability,self.utter,self.pn)

