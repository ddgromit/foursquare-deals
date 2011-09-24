from django.shortcuts import render
from lib.foursquare import FoursquareAuthHelper, FoursquareClient
import settings
from django import http
import httplib2
import simplejson
from lib.foursquare_helpers import init_auth, request_access_token, foursquare_user_id

def homepage_handler(request):
    return render(request,'homepage.html',{})

# Redirect the user to the foursquare oauth dialog
def foursquare_login_handler(request):
	auth_helper = init_auth()
	return http.HttpResponseRedirect(auth_helper.get_authentication_url())

# On return from foursquare oauth dialog: 
# - grab the access code
# - request their profile from foursquare
# - login the user
def foursquare_login_callback(request):
	# Make sure foursquare login was successful
	code = request.GET.get('code')
	if not code:
		return http.HttpResponse("No code returned")
	
	# Get a token with this code
	access_token = request_access_token(code)

	# Retrieve foursquare user account details
	user_id = foursquare_user_id(access_token)

	# Load or create a user

	# Log this user in

	# Redirect to homepage
	return http.HttpResponse("Foursquare User Id:" + str(user_id))