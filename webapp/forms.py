from django import forms
from webapp.models import Article


class SearchProjectForm(forms.Form):
    project_name = forms.CharField(max_length=50, required=False, label="Имя проекта")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'description']
