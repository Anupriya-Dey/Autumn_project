from ast import Delete
from email.mime import application
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Recruitment_season(models.Model):   
    year = models.IntegerField(max_length=4, primary_key=True)
    name = models.TextField()
    role = models.TextField()
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()

class Rounds(models.Model):   
    season_id = models.ForeignKey(Recruitment_season, related_name='year')
    type = models.TextField()

class Section(models.Model):   
    round_id = models.ForeignKey(Rounds, on_delete=CASCADE, related_name='id')
    name = models.TextField()
    weightage = models.FloatField()

class Applicant(models.Model):   
    enrollment_no = models.IntegerField(max_length=8, primary_key=True) 
    name = models.TextField()
    email = models.TextField()
    mob = models.PositiveIntegerField(max_length=10)
    role = models.CharField(max_length=15)
    cg = models.FloatField()
    round_id = models.ForeignKey(Rounds, on_delete=CASCADE, related_name='id')
    called = models.BooleanField(default=False)
    season_id = models.ForeignKey(Recruitment_season, related_name='year')
    

class IMG_member(models.Model):   
    enrollment_no = models.IntegerField(max_length=8, primary_key=True) 
    name = models.TextField()
    email = models.TextField()
    mob = models.PositiveIntegerField(max_length=10)
    role = models.CharField(max_length=15)
    year = models.IntegerField(max_length=4)



class Question(models.Model):   
    id = models.IntegerField(primary_key=True)
    section_id = models.ForeignKey(Section, on_delete=CASCADE, related_name='id')
    text = models.TextField()
    mark = models.FloatField()
    assignee = models.ForeignKey(IMG_member, on_delete=CASCADE, related_name='enrollment_no')
    
class Interview_panel(models.Model):   
    panel_name = models.TextField()
    panelist = models.ForeignKey(IMG_member, on_delete=CASCADE, related_name='enrollment_no')
    room_no = models.IntegerField()
    status = models.BooleanField(default=False)
    season_id = models.ForeignKey(Recruitment_season, on_delete=CASCADE, related_name='year')

class Marks(models.Model):   
    round_id = models.ForeignKey(Rounds, on_delete=CASCADE, related_name='id')
    applicant_id = models.ForeignKey(Applicant, related_name='enrollment_no')
    checked = models.BooleanField(default=False)
    queston_id = models.ForeignKey(Question, on_delete=CASCADE, related_name='question_id')
    marks = models.FloatField()

class Remarks(models.Model):   
    round_id = models.ForeignKey(Rounds, on_delete=CASCADE, related_name='id')
    applicant_id = models.ForeignKey(Applicant, on_delete=CASCADE, related_name='enrollment_no')
    remark = models.TextField()
    status = models.BooleanField(default=False)
    interview_panel = models.ForeignKey(Interview_panel, on_delete=CASCADE, related_name='id')