from django.db import models


class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    # allowed_memberships = models.ManyToManyField

    def __str__(self):
        return self.title


class Lesson(models.Model):
    slug = models.SlugField()
    position = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    video = models.CharField(max_length=255)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
