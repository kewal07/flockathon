import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
import os,sys,linecache
from categories.models import Category
from django.template.defaultfilters import slugify
from login.models import ExtendedUser
import hashlib
import hmac
from login.models import ExtendedUser,Company
from datetime import date
from django.core.urlresolvers import resolve,reverse
# Create your models here.

shakey=(settings.SHAKEY).encode('utf-8')

def get_file_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "choice%s.%s" % (instance.question.id,ext)
	folder_day = date.today()
	profilePath = (os.path.join(settings.BASE_DIR,'media'+os.sep+'choices'+os.sep+str(folder_day)))
	return os.path.join(profilePath,filename)

def get_file_path_featured(instance, filename):
	ext = filename.split('.')[-1]
	filename = "featured%s.%s" % (instance.id,ext)
	folder_day = date.today()
	profilePath = (os.path.join(settings.BASE_DIR,'media'+os.sep+'featuredimages'+os.sep+str(folder_day)))
	return os.path.join(profilePath,filename)

def get_file_path_email(instance, filename):
	ext = filename.split('.')[-1]
	filename = "email%s.%s" % (instance.id,ext)
	folder_day = date.today()
	profilePath = (os.path.join(settings.BASE_DIR,'media'+os.sep+'emailimages'+os.sep+str(folder_day)))
	return os.path.join(profilePath,filename)

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	pub_date = models.DateTimeField('Date Published')
	description = models.CharField(max_length=400,null=True,blank=True)
	que_slug = models.SlugField(null=True,blank=True)
	created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
	upvoteCount = models.IntegerField(default=0)
	isBet = models.BooleanField(default=0)
	winning_choice = models.IntegerField(blank=True,null=True)
	numViews = models.IntegerField(blank=True,null=True,default=0)
	last_accessed = models.DateTimeField(null=True,blank=True)
	home_visible = models.BooleanField(default=1)
	protectResult = models.BooleanField(default=0)
	featured_image = models.ImageField(upload_to=get_file_path_featured,blank=True,null=True)


class Survey(models.Model):
	survey_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date Published')
	description = models.CharField(max_length=2000,null=True,blank=True)
	survey_slug = models.SlugField(null=True,blank=True)
	created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
	numViews = models.IntegerField(blank=True,null=True,default=0)
	expected_time = models.IntegerField(blank=True,null=True,default=0)


