from django.db import models

# Create your models here.
class Dept(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=20)
    name = models.TextField()
    def __str__(self):
        return self.code

class Employess(models.Model):
    id = models.IntegerField(primary_key=True)
    ecode = models.CharField(max_length=10)
    name = models.TextField()
    dob = models.DateField()
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    salary = models.FloatField()
