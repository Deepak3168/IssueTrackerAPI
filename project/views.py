from django.shortcuts import render
from .models import Project,Team,Issue
from .serializers import ProjectSerializer,TeamSerializer,IssueSerializer
from rest_framework import generics,permissions
from .permissions import IsTeamLeadorReadonly,IsTeam,IsIssueTeam


# Create your views here.
class ProjectList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsTeamLeadorReadonly,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TeamProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    def get_queryset(self):
        team_pk = self.kwargs.get('pk')  # Get the team primary key from the URL
        return Project.objects.filter(team_id=team_pk)
    permission_classes = (IsTeamLeadorReadonly,)

class TeamProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        team_pk = self.kwargs.get('team_pk')  # Get the team primary key from the URL
        return Project.objects.filter(team_id=team_pk)

    def get_object(self):
        queryset = self.get_queryset()
        project_id = self.kwargs.get('project_pk')  # Use a different name for the project primary key
        # Filter the queryset further to retrieve the specific project detail
        obj = queryset.filter(pk=project_id).first()
        return obj
    permission_classes = (IsTeamLeadorReadonly,)

class TeamProjectIssues(generics.ListCreateAPIView):
    serializer_class = IssueSerializer

    def get_queryset(self):
        team_pk = self.kwargs.get('team_pk')
        project_pk = self.kwargs.get('project_pk')
        return Issue.objects.filter(project__team_id=team_pk, project_id=project_pk)
    
    permission_classes = (IsIssueTeam,)


class TeamProjectIssueDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IssueSerializer

    def get_queryset(self):
        team_pk = self.kwargs.get('team_pk')
        project_pk = self.kwargs.get('project_pk')
        return Issue.objects.filter(project__team_id=team_pk, project_id=project_pk)

    def get_object(self):
        queryset = self.get_queryset()
        issue_id = self.kwargs.get('issue_pk')
        obj = queryset.filter(pk=issue_id).first()
        return obj
    
    permission_classes = (IsIssueTeam,)

class TeamList(generics.ListCreateAPIView):
    permission_classes = (IsTeam,permissions.IsAuthenticated)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsTeam,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class IssuesList(generics.ListCreateAPIView):
    permission_classes = (IsIssueTeam,)
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsIssueTeam,)
    queryset  = Issue.objects.all()
    serializer_class = IssueSerializer