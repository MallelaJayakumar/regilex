from django.db import models

class Task(models.Model):
    '''
        Model represent books
    '''
    id = models.IntegerField(max_length=10, blank=False)
    name = models.CharField(max_length=100, blank=False)
    Action = models.CharField(default='',max_length=2, choices= [('1','Pending'), ('2','Done'), ('3','Edit')])
    status = models.CharField(default='No',max_length=2, choices= [('1','Yes'), ('2','No')] )
    Objects = models.Manager()