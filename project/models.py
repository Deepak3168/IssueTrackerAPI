from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Project(models.Model):
    teamlead = models.ForeignKey(User,on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    issues = models.ManyToManyField('Issue', related_name='projects')

    def __str__(self):
        return self.title


class Issue(models.Model):
    STATUS_CHOICES = [
        ('assigned', 'Assigned'),
        ('completed', 'Completed'),
        ('not_assigned', 'Not Assigned'),
    ]
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to=models.Q())
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='not assigned')

    def __str__(self):
        return self.name

    def get_team_member_filter(self):
        return Q(project__team__members=self.project.team.members.all())