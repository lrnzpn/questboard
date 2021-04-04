from django.urls import path
from django.conf import settings

from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('new_questboard/', new_questboard, name="new_questboard"),
    path('questboards/', all_questboards, name="questboards"),
    path('questboard/<str:slug>', view_questboard, name="view_questboard")
]
