import settings
import httplib2
import simplejson
from foursquare import FoursquareAuthHelper, FoursquareClient

# Construct a foursquare auth object from our app's consumer credentials
def init_auth():
	config = settings.FOURSQUARE_CONFIG
	return FoursquareAuthHelper(
		key = config['consumer_key'],
		secret = config['consumer_secret'],
		redirect_uri = config['redirect_uri'],
	)

# Make a request to foursquare for an access token
def request_access_token(code):
	# Generate the url for the reuqest
	auth_helper = init_auth()
	access_token_url = auth_helper.get_access_token_url(code)

	# Make the request
	h = httplib2.Http()
	resp, content = h.request(access_token_url, 'GET')

	# Parse the response
	obj = simplejson.loads(content)

	# The access token should be the only parameter set
	access_token = obj['access_token']
	return access_token


# Make a request to just grab the foursquare user id of the authenticated user
def foursquare_user_id(access_token):
	client = FoursquareClient(access_token)
	json = client.users(user_id = 'self')
	return json['response']['user']['id']
