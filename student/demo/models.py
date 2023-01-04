from django.db import models

class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    position = models.CharField( max_length=50)
    

    def __str__(self):
        return self.name


class user(models.Model):
    username= models.CharField( max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self) :
        return self.username