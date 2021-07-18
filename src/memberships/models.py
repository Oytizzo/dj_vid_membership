from django.db import models
from django.conf import settings


class Memberships(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(max_length=25)
    price = models.IntegerField()
    strip_plan_id = models.CharField(max_length=255)

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    stripe_customer_id = models.CharField(max_length=100)
    membership = models.ForeignKey(Memberships, on_delete=models.SET_NULL, null=True)
