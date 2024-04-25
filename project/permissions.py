from rest_framework import permissions

class IsTeamLeadorReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if obj.teamlead == request.user:
            return True  
        

        if obj.team.members.filter(id=request.user.id).exists():
           
            return request.method in ['GET', 'POST']

        return False

class IsTeam(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if  obj.members.filter(id=request.user.id).exists() :
            return True 
        else:
            return False

class IsIssueTeam(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the request user is in the team members associated with the project of the issue
        return obj.project.team.members.filter(id=request.user.id).exists()
