from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = (
    ('cat1','CATEGORY1'),
    ('cat2','CATEGORY2'),
    ('cat3','CATEGORY3'),
    ('cat4','CATEGORY4'),
    ('cat5','CATEGORY5'),

)


Tags_CHOICES = (
    ('tag1','TAG1'),
    ('tag2','TAG2'),
    ('tag3','TAG3'),
    ('tag4','TAG4'),
    ('tag5','TAG5'),

)



class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    project_details = models.CharField(max_length=500)
    total_target = models.IntegerField()
    total_donations = models.IntegerField(default=0)
    avg_rate = models.FloatField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    tag = models.CharField(max_length=6, choices=Tags_CHOICES, default='tag1')
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default='cat1')
    raters = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Projectcomments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=1000)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment

class Commentsreport(models.Model):
    comment_id = models.ForeignKey(Projectcomments, on_delete=models.CASCADE)
    report_comment = models.CharField(max_length=1000)

class ProjectsReport(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    report_project = models.CharField(max_length=1000)

class Projectpictures(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics/')

