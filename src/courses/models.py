import string
import random

from django.db import models
from django.utils.text import slugify


def rand_slug():
    return ''.join(random.choice(string.ascii_letters) for _ in range(6))


class Course(models.Model):
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # allowed_memberships = models.ManyToManyField

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super().save(*args, **kwargs)


class Lesson(models.Model):
    slug = models.SlugField(blank=True)
    position = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    video = models.CharField(max_length=255)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super().save(*args, **kwargs)
