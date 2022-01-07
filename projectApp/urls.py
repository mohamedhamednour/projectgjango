from  django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views  as Authentication

import userApp.views
from userApp import views
from projectApp import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', userApp.views.home),
    path('projectadd',views.AddProject,name='projectadd'),
    path('viewprojects',views.viewproject,name='viewprojects'),
    path('viewLatest',views.viewLatest,name='viewLatest'),
    path('idproject/<int:id>/',views.projectDetails,name='projectdetails'),
    path('delteproject/<int:id>/',views.deleteProject,name='deleteProject'),
    path('UpdateProjectView',views.UpdateProjectView, name='UpdateProjectView'),
    path('viewcomment',views.viewComments,name='viewcomment'),
    path('viewreport', views.viewReports, name='viewreport'),
    path('viewProjectsReports', views.viewProjectsReports, name='viewProjectsReports'),
    # path('comment',views.AddCommentView, name="Addcomment"),
    path('report', views.AddReportView, name="AddReport"),
    path('reportProject', views.AddReportProjectView, name="AddReportProject"),
    path('api',views.ApiStudent.as_view(),name='api'),


]