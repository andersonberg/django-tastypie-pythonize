from django.db import models
from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(default=now)
    text = models.CharField(max_length=200)
    slug = models.SlugField()

    def __unicode__(self):
        return self.text

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.text)[:50]
        return super(Post, self).save(*args, **kwargs)
