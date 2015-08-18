from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import os
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

class Post(models.Model):
	author = models.ForeignKey('auth.User')#mac dinh den truong ForeignKey
	title = models.CharField(max_length=200)#ham se tu khoi tao cho bien va set type data
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	is_sharing = models.BooleanField(default=True)
	# image = models.FileField(upload_to='profile/%Y/%m/%d')
	image = models.FileField(upload_to='profile', max_length=250)
	def publish(self):
		self.published_date=timezone.now()
		self.save()
	def __str__(self):
		return self.title

	# def delete(self):
 #        # You have to prepare what you need before delete the model
 #    	storage, path = self.image.storage, self.image.path
 #        # Delete the model before the file
 #        super(Post, self).delete()
 #        # Delete the file after the model
 #        storage.delete(path)

@receiver(post_delete, sender=Post)
def file_delete(sender, instance, **kwargs):
    try:
        storage, path = instance.image.storage, instance.image.path
        storage.delete(path)
    except Exception:
        pass