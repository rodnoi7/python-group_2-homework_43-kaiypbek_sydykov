# Generated by Django 2.1 on 2018-12-15 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ManyToManyField(related_name='commented_article', to='blog.Article', verbose_name='Commented'),
        ),
        migrations.AddField(
            model_name='mark',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mark_author', to='blog.User', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='articles_author', to='blog.User', verbose_name='Author'),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ManyToManyField(related_name='comment_author', to='blog.User', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_article', to='blog.Article', verbose_name='Article'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='saved_article', to='blog.Article', verbose_name='Article'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='saved_author', to='blog.User', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(related_name='favorite_articles', through='blog.Favorites', to='blog.Article', verbose_name='Favorites'),
        ),
    ]
