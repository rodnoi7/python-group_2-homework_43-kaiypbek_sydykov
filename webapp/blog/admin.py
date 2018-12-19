from django.contrib import admin
from blog.models import User, Article, Comment, Mark, Favorites

# Register your models here.

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Mark)
admin.site.register(Favorites)