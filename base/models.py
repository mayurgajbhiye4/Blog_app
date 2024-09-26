from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from autoslug import AutoSlugField

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = AutoSlugField(populate_from = 'title', unique=True, null=True, default=None, blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
