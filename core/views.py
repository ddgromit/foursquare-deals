from django.shortcuts import render
from django import http
from django.contrib.auth import authenticate, login, logout
from lib.foursquare_helpers import init_auth, request_access_token, foursquare_user_id
from lib.site_auth import create_foursquare_user, update_notifo_username, update_boxcar_email, test_notifo
from django.contrib.auth.decorators import login_required


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
		user = create_foursquare_user(
			foursquare_id = foursquare_id,
			access_token = access_token,
		)
		user = authenticate(foursquare_id = int(foursquare_id))

	# Log this user in
	login(request,user)
		
	# Redirect to homepage
	return http.HttpResponseRedirect("/")

@login_required
def update_notifo_handler(request):
	notifo_username = request.POST.get('notifo_username')
	update_notifo_username(request.user, notifo_username)

	return http.HttpResponseRedirect("/")

@login_required
def update_boxcar_handler(request):
	boxcar_email = request.POST.get('boxcar_email')
	update_boxcar_email(request.user, boxcar_email)
	return http.HttpResponseRedirect("/")

@login_required
def test_notifo_handler(request):
	test_notifo(request.user)
	return http.HttpResponse('cool')
	
def logout_handler(request):
	logout(request)
	return http.HttpResponseRedirect("/")