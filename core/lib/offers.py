from hyperpublic import Hyperpublic
from settings import HYPERPUBLIC_CONFIG

def offers_near(lat,lon):
	hp = Hyperpublic(
		client_id=HYPERPUBLIC_CONFIG['client_id'],
		client_secret = HYPERPUBLIC_CONFIG['client_secret'],
	)
	offers = hp.offers.find(lat=lat,lon=lon,radius=1)
	return offers
