from django.urls import path 
from .views import ProjectDetail,ProjectList,IssueDetail,IssuesList,TeamDetail,TeamList,TeamProjectList,TeamProjectDetail,TeamProjectIssues,TeamProjectIssueDetail

urlpatterns = [
    path('projects/<int:pk>/',ProjectDetail.as_view()),
    path('projects/',ProjectList.as_view()),
    path('issues/',IssuesList.as_view()),
    path('issues/<int:pk>/',IssueDetail.as_view()),
    path('team/',TeamList.as_view()),
    path('team/<int:pk>/',TeamDetail.as_view()),
    path('team/<int:pk>/projects',TeamProjectList.as_view()),
    path('team/<int:team_pk>/projects/<int:project_pk>/', TeamProjectDetail.as_view(), name='team_project_detail'),
    path('team/<int:team_pk>/projects/<int:project_pk>/issues/',TeamProjectIssues.as_view()),
    path('team/<int:team_pk>/projects/<int:project_pk>/issues/<int:issue_pk>/',TeamProjectIssueDetail.as_view())
    ]