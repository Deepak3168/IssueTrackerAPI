from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Project,Team

# Create your tests here\
class TeamandProjectTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser2 = User.objects.create_user(
            username='testuser2', password='abc123')

        test_team = Team.objects.create(name="testteam")
        test_team.members.add(testuser1, testuser2)

        test_project = Project.objects.create(
            teamlead = testuser1,title = "projecttitle",description = "project description..",
            team = test_team
        )
        test_project.save()

    def test_team(self):
        team = Team.objects.get(id=1)
        team_name = f"{team.name}"
        team_members = team.members.all()
    def test_team(self):
        team = Team.objects.get(id=1)
        team_name = f"{team.name}"
        team_members = team.members
        self.assertEqual(team_name,'testteam')
    def test_project(self):
        project = Project.objects.get(id=1)
        team = project.team
        teamlead = project.teamlead
        title = f"{project.title}"
        description = f"{project.description}"
        self.assertEqual(title,"projecttitle")
        self.assertEqual(description,"project description..")





