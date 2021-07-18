from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
# import stripe


class Membership(models.Model):
    MEMBERSHIP_FREE = 'F'
    MEMBERSHIP_PRO = 'P'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_FREE, 'Free'),
        (MEMBERSHIP_PRO, 'Pro'),
    ]

    slug = models.SlugField()
    membership_type = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_FREE)
    price = models.IntegerField()
    strip_plan_id = models.CharField(max_length=255)

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    stripe_customer_id = models.CharField(max_length=100)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


def post_save_usermembership_create(sender, instance, created, *args, **kwargs):
    if created:
        UserMembership.objects.get_or_create(user=instance)

    user_membership, created = UserMembership.objects.get_or_create(user=instance)

    # if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id = '':
    #     new_customer_id = stripe.Customer.create(email=instance.email)
    #     user_membership.stripe_customer_id = new_customer_id['id']
    #     user_membership.save()


post_save.connect(post_save_usermembership_create, sender=settings.AUTH_USER_MODEL)


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username
