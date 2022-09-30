from ast import Delete
from email.mime import application
from http.client import NOT_MODIFIED
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
DEVELOPER = 'dev'
DESIGNER = 'des'
ROLE_CHOICES = [
    (DESIGNER, 'Designer'),
    (DEVELOPER, 'Developer'),        
]






class Recruitment_season(models.Model):   
    year = models.IntegerField(max_length=4, primary_key=True)
    name = models.TextField()
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default=DEVELOPER)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()

class Rounds(models.Model):  
    WRITTEN = 'w'
    INTERVIEW = 'i'
    ROUND_CHOICES = [
        (WRITTEN, 'Written Test'),
        (INTERVIEW, 'Interview'),
    ] 
    season_id = models.ForeignKey(Recruitment_season, related_name='year')
    type = models.CharField(max_length=1, choices=ROUND_CHOICES, default=WRITTEN)

class Section(models.Model):   
    round_id = models.ForeignKey(Rounds, on_delete=CASCADE, related_name='id')
    name = models.TextField()
    weightage = models.FloatField()

class Applicant(models.Model):   
    enrollment_no = models.IntegerField(max_length=8, primary_key=True) 
    name = models.TextField()
    email = models.EmailField()
    mob = models.PositiveIntegerField(max_length=10)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default=DEVELOPER)
    cg = models.FloatField()
    round_id = models.ForeignKey(Rounds, on_delete=CASCADE, related_name='id')
    # called = models.BooleanField(default=False)
    
    

class IMG_member(models.Model):   
    enrollment_no = models.IntegerField(max_length=8, primary_key=True) 
    name = models.TextField()
    email = models.TextField()
    mob = models.PositiveIntegerField(max_length=10)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default=DEVELOPER)
    year = models.IntegerField(max_length=4)



class Question(models.Model):   
    id = models.IntegerField(primary_key=True)
    section_id = models.ForeignKey(Section, on_delete=CASCADE, related_name='id')
    text = models.TextField()
    mark = models.FloatField()
    assignee = models.ForeignKey(IMG_member, on_delete=CASCADE, related_name='enrollment_no')
    
class Interview_panel(models.Model): 
    INACTIVE = 'in'
    OCCUPIED = 'oc'
    IDLE = 'id'
    STATUS_CHOICES = [
        (INACTIVE, 'Inactive'),
        (OCCUPIED, 'Occupied'),
        (IDLE, 'Idle'),
    ]  
    panel_name = models.TextField()
    panelist = models.ManyToManyField(IMG_member, on_delete=CASCADE, related_name='enrollment_no')
    room_no = models.IntegerField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=INACTIVE)
    season_id = models.ForeignKey(Recruitment_season, on_delete=CASCADE, related_name='year')

class Candidate_marks(models.Model):   
    # round_id = models.ForeignKey(Rounds, on_delete=CASCADE, related_name='id')
    applicant_id = models.ForeignKey(Applicant, related_name='enrollment_no')
    checked = models.BooleanField(default=False)
    queston_id = models.ForeignKey(Question, on_delete=CASCADE, related_name='question_id')
    marks = models.FloatField()
    remarks = models.TextField()

class Remarks(models.Model):   
    NOT_NOTIFIED = 'NN'
    NOTIFIED = 'N'
    IN_WAITING_ROOM = 'WR'
    IN_INTERVIEW = 'IN'
    COMPLETE = 'C'
    ABSENT = 'AB'
    DETAILS_CHOICES = [
        (NOT_NOTIFIED, 'Not Notified'),
        (NOTIFIED, 'Notified'),
        (IN_WAITING_ROOM, 'In waiting room'),
        (IN_INTERVIEW, 'In Interview'),
        (COMPLETE, 'Complete'),
        (ABSENT, 'Absent'),    
    ]
    Candidate_round = models.ForeignKey(Rounds, on_delete=CASCADE, related_name='id')
    applicant_id = models.ForeignKey(Applicant, on_delete=CASCADE, related_name='enrollment_no')
    remark = models.TextField()
    status = models.CharField(max_length=2, choices=DETAILS_CHOICES, default=NOT_NOTIFIED)
    interview_panel = models.ForeignKey(Interview_panel, on_delete=CASCADE, related_name='id')
    time_slot = models.CharField(max_length = 255)