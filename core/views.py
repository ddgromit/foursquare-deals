from django.shortcuts import render
from django import http
from django.contrib.auth import authenticate, login
from lib.foursquare_helpers import init_auth, request_access_token, foursquare_user_id
from lib.site_auth import create_foursquare_user

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
	foursquare_id = foursquare_user_id(access_token)

	# Create user if it doesn't exist
	user = authenticate(foursquare_id = int(foursquare_id))
	if not user:
		user = create_foursquare_user(foursquare_id)

	# Log this user in
	login(request,user)
		
	# Redirect to homepage
	return http.HttpResponseRedirect("/")