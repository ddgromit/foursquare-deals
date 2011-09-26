from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from core.models import UserProfile
from notifo import Notifo
import settings

# Retrieves a User object based on their stored foursquare id on their user profile
def user_by_foursquare_id(foursquare_id):
    try:
        user_profile = UserProfile.objects.get(foursquare_id=foursquare_id)
        return user_profile.user # indicates success
    except UserProfile.DoesNotExist:
        return None

class FoursquareBackend(ModelBackend):
    """ 
    Allows us to use the traditional django auth mechanisms (login(), authenticate()) using 
    a foursquare ID instead of a username/pass
    """
    def authenticate(self, foursquare_id):
        # Either return the user if exists or None if it doesnt
        return user_by_foursquare_id(foursquare_id)


def create_foursquare_user(foursquare_id, access_token):
    # Since we don't have a username, just generate one
    username = "foursquare_user_" + foursquare_id
    fake_email = username + "@example.com" # Don't know why we have to do this
    user = User.objects.create_user(username=username,email=fake_email,password=None)
    user.save()

    try:
        user_profile = UserProfile(
            user = user, 
            foursquare_id = foursquare_id, 
            foursquare_access_token = access_token)
        user_profile.save()
    except Exception:
        # If profile creation fails, clean up the user too
        user.delete()

        # Reraise exception
        raise

    return user


def update_boxcar_email(user,email):
    user_profile = user.get_profile()
    user_profile.boxcar_email = email
    user_profile.save()

def update_notifo_username(user,notifo_username):
    # Update the profile
    user_profile = user.get_profile()
    user_profile.notifo_username = notifo_username
    user_profile.save()

    # Send a subscription request to the user
    notifo = Notifo(
        user = settings.NOTIFO_CONFIG['username'],
        secret = settings.NOTIFO_CONFIG['secret'],
    )
    notifo.subscribe_user(notifo_username)

