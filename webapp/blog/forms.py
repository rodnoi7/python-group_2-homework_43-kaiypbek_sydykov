from django import forms
from blog.models import Article, User, Comment


class SearchProjectForm(forms.Form):
    project_name = forms.CharField(max_length=50, required=False, label="Article's name")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'author']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'login', 'email', 'password', 'about_yourself']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['article', 'parrent_comment']

class CommentAnswerForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ['parrent_comment', 'article']