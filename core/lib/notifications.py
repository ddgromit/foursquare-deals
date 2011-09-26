from notifo import Notifo
import settings

def init_notifo():
    return Notifo(
        user = settings.NOTIFO_CONFIG['username'],
        secret = settings.NOTIFO_CONFIG['secret'],
    )

def send_notifo_offer(user, lat=None,lon=None):
	notifo = init_notifo()

	username = user.get_profile().notifo_username
	if not username or username == '':
		return False
	
	# Generate a url
	url = "%s/checkin_offers?lat=%slon=%s" % (settings.THIS_HOST,lat,lon)

	# Send notification
	notifo.send_notification(to=username,msg="Deals found near your checkin", uri=url)

	return True

# A debugging function that tries to send a notifo notification to one of our users
def test_notifo(user):
    notifo = init_notifo()
    notifo.send_notification(to='ddgromit',msg='whatup',uri='http://www.google.com')