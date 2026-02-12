from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    #Custom permission to obly allow owners of a task to edit or delete it

    def has_object_permission(self, request, view, obj):
        #Permission are only allowed to the owner of the task
        #obj is the Task instanc we are checking
        return obj.user == request.user