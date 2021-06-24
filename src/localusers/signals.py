from allauth.account.signals import user_logged_in, user_logged_out, user_signed_up
from django.dispatch import receiver


@receiver(user_logged_in)
def logged_in(request, user, **kwargs):
    print("user_logged_in signals working just nice. I'm from apps.py > signals.py")

# user_logged_in.connect(logged_in)


@receiver(user_logged_out)
def logged_out(request, user, **kwargs):
    print("You are just logged out! Log in again?")


@receiver(user_signed_up)
def signed_up(request, user):
    print("You are just signed up! Log in?")