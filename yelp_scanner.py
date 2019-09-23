from yelp_yoink.yelp_sdk import Yelp_Search, Yelp_Connector
import config.yelp_conf as yelp_conf
from math import sin,pi


location = '"Dallas, TX"'
limit = 51
offset = 0

radius = 10 # meters
# For complete coverage we need to increment by the length of the side of the largest square that can fit inside the radius
increment = 2*radius*sin(pi/4)

connector = Yelp_Connector(yelp_conf.client_id,yelp_conf.api_key)
search = connector.search()
search.set_location(location)
print(search.execute_search())