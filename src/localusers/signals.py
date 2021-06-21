from allauth.account.signals import user_logged_in
from django.dispatch import receiver


@receiver(user_logged_in)
def logged_in(request, user, **kwargs):
    print("user_logged_in signals working just nice. I'm from apps.py > signals.py")

# user_logged_in.connect(logged_in)
