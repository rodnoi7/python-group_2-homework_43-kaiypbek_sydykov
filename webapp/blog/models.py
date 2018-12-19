from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Name')
	surname = models.CharField(max_length=200, null=False, blank=False, verbose_name='Surname')
	login = models.CharField(max_length=20, null=False, blank=False, verbose_name='login')
	password = models.CharField(max_length=100, null=False, blank=False, verbose_name='password')
	email = models.CharField(max_length=200, null=False, blank=False, verbose_name='email')
	about_yourself = models.TextField(max_length=1000, null=True, blank=False, verbose_name='About yourself')
	favorites = models.ManyToManyField("Article", through='Favorites', through_fields=('user', 'article'), related_name='favorite_articles', verbose_name='Favorites', null=True, blank=False)

	def __str__(self):
		return "%s %s" % (self.surname, self.name)


class Article(models.Model):
	author = models.ForeignKey('User', on_delete=models.PROTECT, related_name='articles_author', verbose_name='Author')
	title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Title')
	text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Text')

	def __str__(self):
		return "%s. %s - %s" % (self.pk, self.title, self.author)


class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comment_author', verbose_name='Author')
	article = models.ManyToManyField(Article, related_name='commented_article', verbose_name='Article')
	text = models.CharField(max_length=3000, null=False, blank=True, verbose_name='Comment')



class Mark(models.Model):
	MARK_VARY_BAD = 'Vary bad'
	MARK_BAD = 'Bad'
	MARK_NORMAL = 'Normal'
	MARK_GOOD = 'Good'
	MARK_FINE = 'Fine'

	MARK_CHOICES = (
		(MARK_VARY_BAD, 'Vary bad'),
		(MARK_BAD, 'Bad'),
		(MARK_NORMAL, 'Normal'),
		(MARK_GOOD, 'Good'),
		(MARK_FINE, 'Fine'),
	)

	user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='mark_author', verbose_name='Author', null=True)
	article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='to_article', verbose_name='Article')
	mark = models.CharField(max_length=20, choices=MARK_CHOICES, verbose_name="Mark")


class Favorites(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='saved_author', verbose_name='Author')
	article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='saved_article', verbose_name='Article')