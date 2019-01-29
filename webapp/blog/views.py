from django.views.generic import ListView, DetailView, TemplateView, View, RedirectView, FormView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import User, Article, Comment, Mark, Favorites
from django.http import Http404, HttpResponseForbidden
from django.db.models import Q
from blog.forms import SearchProjectForm, ProjectForm, UserForm, CommentForm, CommentAnswerForm
from django.urls import reverse_lazy, reverse


class ArticlesListView(ListView, FormView):
    model = Article
    template_name = 'index.html'
    form_class = SearchProjectForm


    # def dispatch(self, request, *args, **kwargs):
    # if not request.user.is_authenticated:
    #     return redirect('%s' % reverse('webauth:login'))
    # return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        project_name = self.request.GET.get('project_name')
        if not project_name:
            return Article.objects.all()
        else:
            return Article.objects.filter(title__icontains=project_name)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'view.html'


class ProjectCreateView(CreateView):
   model = Article
   form_class = ProjectForm
   template_name = 'create_view.html'
   success_url = reverse_lazy('blog:index')


class ProjectUpdateView(UpdateView):
    model = Article
    form_class = ProjectForm
    template_name = 'update_article.html'
    success_url = reverse_lazy('blog:article')


class ProjectDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('blog:index')


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'create_user_view.html'
    success_url = reverse_lazy('blog:user')


class UsersListView(ListView):
    model = User
    template_name = 'users_view.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('blog.index'):
            return HttpResponseForbidden()
        else:
            return super().dispatch(request, *args, **kwargs)


class UserDetailView(DetailView):
    model = User
    template_name = 'user.html'


def favorite(request, user_pk):
    if request.method == 'GET':
        user = User.objects.get(pk=user_pk)
        context = {
            'user': user,
        }
        return render(request, 'saved_articles.html', context)

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_pk']=self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        form.instance.article = Article.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:article', kwargs={'pk': self.object.article.pk})

class AnswerCommentCreateView(CreateView):
    model = Comment
    form_class = CommentAnswerForm
    template_name = 'comment_answer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_pk']=self.kwargs.get('pk')
        context['parrent_comment']=self.kwargs.get('comment_pk')
        return context

    def form_valid(self, form):
        form.instance.article = Article.objects.get(pk=self.kwargs.get('pk'))
        form.instance.parrent_comment = Comment.objects.get(pk=self.kwargs.get('comment_pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:article', kwargs={'pk': self.object.article.pk})



def change_comment(request, article_pk, comment_pk):
    if request.method == 'GET':
        comment = Comment.objects.get(pk=comment_pk)
        context = {
            'comment': comment,
        }
        return render(request, 'update_comment.html', context)
    elif request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        article = Article.objects.get(pk=article_pk)
        author = User.objects.get(pk=article.author.pk)
        comment.text = request.POST.get('text')
        comment.save() 
        comment = Comment.objects.all()
        context = {
            'comment': comment
        }
        return redirect('blog:article', article_pk)


def add_favorite(request, article_pk):
    if request.method == 'GET':
        article = Article.objects.get(pk=article_pk)
        user = User.objects.all()
        context = {
            'article': article,
            'users': user,
        }
        return render(request, 'add_favorites.html', context)        
    elif request.method == 'POST':
        print(request.POST.get('user'))
        user = User.objects.get(pk=(request.POST.get('user')))
        article = Article.objects.get(pk=article_pk)
        favorite = Favorites.objects.create(user=user, article=article)
        favorite.save()
        return redirect('blog:article', article_pk)