from allauth.account.signals import user_logged_in


def logged_in(request, user):
    print("user logged in, hello kitty")


user_logged_in.connect(logged_in)
