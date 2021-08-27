from django.db import models

# Create your models here.

class Banner(models.Model):
	title = models.CharField(max_length = 50, blank = False)
	desc = models.TextField(blank = True)
	image = models.ImageField('media', blank = False)
	status = models.BooleanField()
	status.default = False

class Category(models.Model):
	title = models.CharField(max_length = 100, blank = False, unique = True)
	image = models.ImageField('media/category', blank = False, upload_to = 'category')
	status = models.BooleanField()
	status.default = False

	def __str__(self):
		return self.title

class Portfolio(models.Model):
	cat_id = models.ForeignKey(
		'pg.Category',
		on_delete=models.CASCADE
	)
	image = models.ImageField('media/portfolio', blank = False, upload_to = 'portfolio')
	status = models.BooleanField()
	status.default = True
	created_date = models.DateField()
	created_date.null = True

class Blog(models.Model):
	title = models.CharField(max_length = 100, blank = False)
	desc = models.TextField(blank = True)
	image = models.ImageField('media/blog', blank = False, upload_to = 'blog')
	status = models.BooleanField()
	status.default = False
	created_date = models.DateField()
	created_date.null = True

class Contact(models.Model):
	name = models.CharField(max_length = 100, blank = False)
	email = models.EmailField(max_length = 100, blank = False)
	phone = models.PositiveBigIntegerField(blank = False)
	message = models.TextField(blank = False)
	created_date = models.PositiveIntegerField()