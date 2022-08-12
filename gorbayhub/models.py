from django.db import models

# Create your models here.

class Roman(models.Model):
	titel = models.CharField(max_length=200, verbose_name='عنوان')
	body = models.TextField(verbose_name='رمان')

	def __str__(self):
		return self.titel

class Roman2(models.Model):
	name = models.CharField(max_length=200, verbose_name= 'نویسنده')
	titel = models.CharField(max_length=200, verbose_name='عنوان')
	slug = models.SlugField(max_length=200, unique=True,verbose_name='نشانی')
	body = models.TextField(verbose_name='رمان')
	view = models.BigIntegerField(verbose_name='بازدید')
	admin = models.CharField(max_length=200, verbose_name= 'ادمین')

	

	class Meta:
		verbose_name = "رمان"
		verbose_name_plural = 'رمان ها'
	def __str__(self):
		return f"{self.titel}-{self.view}-{self.admin}"

class Roman3(models.Model):
	name = models.CharField(max_length=200, verbose_name= 'نویسنده')
	titel = models.CharField(max_length=200, verbose_name='عنوان')
	slug = models.SlugField(max_length=200, unique=True,verbose_name='نشانی')
	body = models.TextField(verbose_name='رمان')
	view = models.BigIntegerField(verbose_name='بازدید')
	admin = models.CharField(max_length=200, verbose_name= 'ادمین')

	

	class Meta:
		verbose_name = "رمان"
		verbose_name_plural = 'رمان ها'
	def __str__(self):
		return f"{self.name}-{self.titel}-{self.view}-{self.admin}"