from django import forms

class SearchProjectForm(forms.Form):
    project_name = forms.CharField(max_length=50, required=False, label="Имя проекта")
