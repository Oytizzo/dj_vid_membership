from django.db import models


class Memberships(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(max_length=25)
    price = models.IntegerField()
    strip_plan_id = models.CharField(max_length=255)

    def __str__(self):
        return self.membership_type
