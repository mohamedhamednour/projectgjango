from django.http.response import HttpResponseBase
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from projectApp import models
from .forms import ProjectAddForm , AddCommentForm ,AddReportForm ,Commentsreport,AddReportProjectForm, UpdateProjectForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, generics
from .api import Studentser
from .models import Projects , Projectcomments, ProjectsReport

# Create your views here.

@login_required
def AddProject(request):
    form = ProjectAddForm()
    if request.method == "POST":
        form = ProjectAddForm(request.POST or None)
        if form.is_valid():
            myform = form.save()
            myform.user = request.user
            myform.save()
            return redirect('viewprojects')
    return render(request, 'project/Addproject.html', {'form':form})
@login_required
def viewproject(request):
    projectslist = Projects.objects.all()

    return render(request, 'project/viewproject.html', {'projectslist': projectslist})

@login_required
def projectDetails(request,id):
    detailOfProject = Projects.objects.filter(project_id=id)
    commentsOnproject = Projectcomments.objects.filter(project_id = id)
    updateform = UpdateProjectForm()
    if request.method == "POST":
        updateform = UpdateProjectForm(request.POST)
        if updateform.is_valid():
            # sum_b = Projects.objects.filter(project_id= id).aggregate(sum('total_donations')).get(request.POST['total_donations__sum']) # Takes about 20% more time.
            # oldDonations = Projects.objects.filter(project_id =id,total_donations = donations)
            # print(oldDonations)
            # project = Projects.objects.filter(project_id= id).update(total_donations = request.POST['total_donations'],avg_rate = request.POST['avg_rate'])
            project = Projects.objects.filter(project_id = id)
            project.update(total_donations = (int(project[0].total_donations)+int(request.POST['total_donations'])))
            # -------------------
            # project.update(
            #     avg_rate=(int(project[0].avg_rate) + int(request.POST['avg_rate'])))
            # project.update(raters=(int(project[0].raters) + 1))
            # project.update(avg_rate=int(project[0].avg_rate / project[0].raters))
            project.update(
                avg_rate=(float(project[0].avg_rate) + float(request.POST['avg_rate'])))
            project.update(raters=(float(project[0].raters) + 1))
            project.update(avg_rate=float(project[0].avg_rate / project[0].raters))

            # new_rate = project.update(
            #     avg_rate=(float(project[0].avg_rate) + float(request.POST['avg_rate'])))
            # rate_number = project.update(raters=(int(project[0].raters) + 1))
            # project.update(avg_rate=float(new_rate / rate_number))

            
            

    form = AddCommentForm()
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            myform = form.save()
            myform.user = request.user
            myform.save()
    return render(request,'project/showproject.html',{'detailOfProject':detailOfProject, 'commentsOnproject':commentsOnproject,'form':form, 'updateform':updateform})


class ApiStudent(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = Studentser


@login_required
def viewComments(request):
    comment = Projectcomments.objects.all()
    return render(request, 'project/viewComment.html', {'comment':comment})
@ login_required
def AddReportView(request):
    forms = AddReportForm()
    if request.method == "POST":
        forms = AddReportForm(request.POST)
        if forms.is_valid():
            myforms= forms.save()
            myforms.user = request.user
            myforms.save()
            return redirect('viewprojects')
    return render(request, 'project/AddReport.html', {'forms': forms})
@ login_required
def AddReportProjectView(request):
    forms = AddReportProjectForm()
    if request.method == "POST":
        forms = AddReportProjectForm(request.POST)
        if forms.is_valid():
            myforms= forms.save()
            myforms.user = request.user
            myforms.save()
            return redirect('viewprojects')
    return render(request, 'project/AddReport.html', {'forms': forms})

# student = Students.objects.filter(student_id=st_id).update(student_name=st_name,student_age=st_age)

@login_required
def UpdateProjectView(request, project_id):
    updateform = UpdateProjectForm()
    if request.method == "POST":
        updateform = UpdateProjectForm(request.POST)
        if updateform.is_valid():
            project = Projects.objects.filter(project_id= project_id).update(total_donations = request.POST['total_donations'],avg_rate = request.POST['avg_rate'])
            return redirect('projectdetails')





@login_required
def viewReports(request):
    report = Commentsreport.objects.all()
    
    return render(request, 'project/viewReport.html', {'report':report})

def viewProjectsReports(request):
    report = ProjectsReport.objects.all()
    
    return render(request, 'project/projectreports.html', {'report':report})


def viewLatest(request):
    latestProjects = Projects.objects.all().order_by('-project_id')[:5][::-1]
   

    highestRate = Projects.objects.filter(
    avg_rate__gte=Projects.objects.order_by('-avg_rate')[4].avg_rate
).order_by('-avg_rate')

    highestDonations = Projects.objects.filter(
    total_donations__gte=Projects.objects.order_by('-total_donations')[4].total_donations
).order_by('-total_donations')
    print(highestRate)

    return render(request, 'project/home.html', {'latestProjects': latestProjects, 'highestRate':highestRate, 'highestDonations':highestDonations})


def highestRate(request):
    highestRate = Projects.objects.all().aggregate(max("Avg_rate"))[:5]

    print(highestRate)
    # for i in viewavr:
    #     print(i.Avg_rate)
    dataproject = Projects.objects.all()

    return render(request, 'project/viewproject.html', {'data': dataproject,'highestRate':highestRate})

def deleteProject(request, id):
    project = Projects.objects.filter(project_id=id).delete()
    return redirect('viewprojects')    

# def deleteProject(request, id):
#     donations = Projects.objects.filter(project_id = id ).values_list('total_donations',flat=True)
#     print(donations)
#     target = Projects.objects.filter(project_id=id).values_list('total_target',flat=True)
#     newtarget = target 
#     if donations < newtarget:

#         project = Projects.objects.filter(project_id=id).delete()
#         return redirect('viewprojects')
#     else:
#         return redirect('projectadd')

    # hash
    '''
@login_required
def AddCommentView(request):
    form = AddCommentForm()
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            myform = form.save()
            myform.user = request.user
            myform.save()
            return redirect('viewprojects')
    return render(request, 'project/AddComment.html', {'form': form})
'''