from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

'''
 django model field : 
    - html widget
'''

JOB_TYPE = (
    ('full time', 'full time'),
    ('part time', 'part time')

)

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

class Job(models.Model):  # table
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # column
    #location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE, null=True)
    description = models.TextField(max_length=2000, null=True)
    publiched_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=image_upload, null=True)
    slug = models.SlugField(blank=True,null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):

        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    webiste = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name