from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
   path('',views.home,name='home'),
   path('acadmics',views.acadmics,name='acadmics'),
   path('code',views.code,name='code'),
   path('clubs',views.clubs,name='clubs'),
   path('happenings',views.happenings,name='happenings'),
   path('projects',views.projects,name='projects'),
   path('contribution',views.contribution,name='contribution'),
   path('developers',views.developers,name='developers')
 

]
