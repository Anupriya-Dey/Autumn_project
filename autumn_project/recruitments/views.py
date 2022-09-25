from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question, Recruitment_season, Rounds, Section
from .serializers import QuestionSerializer, RecruitmentSeasonSerializer, RoundsSerializer, SectionSerializer


class RecruitmentSeasonViewSet(viewsets.ModelViewSet):
    queryset=Recruitment_season.objects.all()
    serializer_class=RecruitmentSeasonSerializer
    ordering_fields=['year','name','start','end', 'role']
    ordering=['year']

class RoundsViewSet(viewsets.ModelViewSet):
    queryset=Rounds.objects.all()
    serializer_class=RoundsSerializer
    ordering_fields=['id', 'season_id', 'type']
    ordering=['id']

class SectionViewSet(viewsets.ModelViewSet):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer
    ordering_fields=['id', 'round_id', 'name', 'weightage']
    ordering=['id']

class QuestionViewSet(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    ordering_fields='__all__'
    ordering=['id']
# Create your views here.
