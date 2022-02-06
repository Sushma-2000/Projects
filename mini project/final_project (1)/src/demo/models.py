from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField()
    
    def __str__(self):
        return self.description
class User(models.Model):
    mailid=models.TextField(primary_key=True)
    password=models.TextField()
    taken_test=models.BooleanField(default=False)
    oops_score=models.TextField()
    dbms_score=models.TextField()
    os_score=models.TextField()
    def __str__(self):
        return self.mailid+" "+self.oops_score+" "+self.dbms_score+" "+self.os_score

class Question(models.Model):
    number=models.IntegerField(primary_key=True)
    description=models.TextField()
    
    def __str__(self):
        return self.description
class Dbms_Question(models.Model):
    number=models.IntegerField(primary_key=True)
    description=models.TextField()
    
    def __str__(self):
        return self.description
class Os_Question(models.Model):
    number=models.IntegerField(primary_key=True)
    description=models.TextField()
    
    def __str__(self):
        return self.description
class Oops_modelans(models.Model):
    id=models.IntegerField(primary_key=True)
    answer1=models.TextField()
    answer2=models.TextField()
    answer3=models.TextField()
    
    def __str__(self):
        return self.answer1
class Dbms_modelans(models.Model):
    id=models.IntegerField(primary_key=True)
    answer1=models.TextField()
    answer2=models.TextField()
    answer3=models.TextField()
    
    def __str__(self):
        return self.answer1
class Os_modelans(models.Model):
    id=models.IntegerField(primary_key=True)
    answer1=models.TextField()
    answer2=models.TextField()
    answer3=models.TextField()
    
    def __str__(self):
        return self.answer1

class Oops_userans(models.Model):
    num=models.IntegerField(default=1)
    mailid=models.TextField(default="xyz")
    answer=models.TextField()
    def __str__(self):
        return self.answer

class Dbms_userans(models.Model):
    num=models.IntegerField(default=1)
    mailid=models.TextField(default="xyz")
    answer=models.TextField()
    def __str__(self):
        return self.answer
class Os_userans(models.Model):
    num=models.IntegerField(default=1)
    mailid=models.TextField(default="xyz")
    answer=models.TextField()
    def __str__(self):
        return self.answer

