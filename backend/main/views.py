from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.core.exceptions import PermissionDenied

# class CustomDeadliePermission(BasePermission):
#     def has_permission(self,    request,view):
#         if request.method =='GET':
#             return request.user.is_authenticated
#         else:
#             return request.user.groups.filter(name='Coordenador').exists()

class CustomDeadliePermission(BasePermission):
    def has_permission(self,    request,view):
        if request.method == 'GET':
            return request.user.has_perm('main.view_deadline')
        else:
            return request.user.has_perm('main.add_deadline')
class DeadlineView(ModelViewSet):
    queryset = Deadline.objects.all()
    serializer_class = DeadlineSerializer
    permission_classes = (CustomDeadliePermission,)



    # def get_queryset(self):
    #     user = self.request.user
    #     if user.groups.filter(name='Coordenador').exists():
    #         return Deadline.objects.all()
    #     else:
    #         raise PermissionDenied()

    
