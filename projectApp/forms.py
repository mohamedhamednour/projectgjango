from django import forms
from django.db.models import fields
from .models import Projects, Projectcomments,Commentsreport,ProjectsReport

class ProjectAddForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'project_details', 'total_target', 'start_date', 'end_date', 'tag', 'category']



class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['avg_rate', 'total_donations']


    
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Projectcomments
        fields = ['comment', 'project_id']

class AddReportForm(forms.ModelForm):
    class Meta:
        model = Commentsreport
        fields = ['report_comment', 'comment_id']

class AddReportProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectsReport
        fields = ['report_project', 'project_id']
