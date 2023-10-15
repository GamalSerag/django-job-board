from django.db import models

# Create your models here.

'''
 django model field : 
    - html widget
'''

JOB_TYPE = (
    ('full time', 'full time'),
    ('part time', 'part time')

)
class Job(models.Model):  # table
    title = models.CharField(max_length=100)  # column
    job_type = models.CharField(max_length=15, choices=JOB_TYPE, null=True)
    description = models.TextField(max_length=2000, null=True)
    publiched_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=2)

    def __str__(self):
        return self.title

