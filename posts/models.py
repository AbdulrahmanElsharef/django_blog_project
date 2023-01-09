from django.db import models
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.


class post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=100)
    contents = models.TextField(max_length=5000)
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts/images')
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(post, self).save(*args, **kwargs)  # Call the real save() method
