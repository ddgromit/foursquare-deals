from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from core.models import UserProfile

class FoursquareBackend(ModelBackend):
    """ Authenticate a user based on their foursquare id
    """

    def authenticate(self, foursquare_id):
        try:
            user_profile = UserProfile.objects.get(foursquare_id=foursquare_id)
            return user_profile.user # indicates success
        except UserProfile.DoesNotExist:
            return None


def create_foursquare_user(foursquare_id):
    # Since we don't have a username, just generate one
    username = "foursquare_user_" + foursquare_id
    fake_email = username + "@example.com" # Don't know why we have to do this
    user = User.objects.create_user(username=username,email=fake_email,password=None)
    user.save()

    try:
        user_profile = UserProfile(user = user, foursquare_id = foursquare_id)
        user_profile.save()
    except Exception:
        # If profile creation fails, clean up the user too
        user.delete()

        # Reraise exception
        raise

    return user

