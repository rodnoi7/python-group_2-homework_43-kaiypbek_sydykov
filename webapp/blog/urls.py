from django.contrib import admin
from django.urls import path
from blog.views import ArticlesListView, ProjectCreateView, UserCreateView, UsersListView, ArticleDetailView, UserDetailView, favorite, CommentCreateView, AnswerCommentCreateView, ProjectUpdateView, change_comment, add_favorite, ProjectDeleteView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('', ArticlesListView.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),

    path('article/create', ProjectCreateView.as_view(), name='create_blog'),
    path('projects/<int:pk>/delete', ProjectDeleteView.as_view(), name='article_delete'),
    path('create_user', UserCreateView.as_view(), name='create_user'),

    path('users', UsersListView.as_view(), name='users'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user'),
    
    path('user/<int:user_pk>/favorites', favorite, name='favorite'),
    path('article/<int:article_pk>/save', add_favorite, name='add_favorite'),

    path('article/<int:pk>/create_comment', CommentCreateView.as_view(), name='create_comment'),
    path('article/<int:pk>/comment/<int:comment_pk>/create_answer', AnswerCommentCreateView.as_view(), name='create_comment_answer'),

    path('article/<int:pk>/update', ProjectUpdateView.as_view(), name='change_article'),
    path('article/<int:article_pk>/comment/<int:comment_pk>/update', change_comment, name='change_comment_answer'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)