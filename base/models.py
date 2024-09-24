from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from autoslug import AutoSlugField

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = AutoSlugField(populate_from = 'title', unique=True, null=True, default=None, blank=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
