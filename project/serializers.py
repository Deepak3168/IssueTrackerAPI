from rest_framework import serializers
from .models import Project,Team,Issue


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id','teamlead','team','title','description','created_at','issues')
        model = Project

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name','members')
        model = Team
class IssueSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('name','project','assigned_to','description','created_at','status')
        model = Issue
