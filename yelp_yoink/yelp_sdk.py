import requests
import json

class Url_Builder:
    '''
    Builds a URL based on the base path and parameters provided
    '''
    def __init__(self, base_url):
        self.params = {}
        self.base_url = base_url

    def set_param(self, param, value):
        self.params[param] = value
        return self

    def generate_url(self):
        search_url = []
        search_url.append(self.base_url)
        first_param = True
        for param,value in self.params.items():
            if value != None:
                if not first_param:
                    search_url.append("&")
                else:
                    first_param = False
                    search_url.append("?")
                search_url.append(param+"="+value)
        return ''.join(search_url)

class Yelp_Search:
    '''
    Used to define and execute a call to the Yelp API
    '''
    YELP_SEARCH = 'https://api.yelp.com/v3/businesses/search'

    def __init__(self, api_key):
        self.headers = {'Authorization':'Bearer '+api_key}
        self.url_builder = Url_Builder(self.YELP_SEARCH)

    def execute_search(self):
        search_url = self.url_builder.generate_url()
        resp = requests.get(search_url, headers=self.headers)
        search_results = json.loads(resp.text)
        return search_results

    def set_param(self, param, value):
        self.url_builder.set_param(param,value)
        return self

    def set_location(self, location):
        return self.set_param('location',location)
    
    def set_page_size(self, size):
        return self.set_param('limit',size)

    def set_result_offset(self, offset):
        return self.set_param('offset',offset)

    def set_latitude(self, latitude):
        return self.set_param('latitude',latitude)

    def set_longitude(self, longitude):
        return self.set_param('longitude',longitude)

    def set_radius(self, radius):
        return self.set_param('radius',radius)


class Yelp_Connector:
    def __init__(self, client_id, api_key):
        self.client_id = client_id
        self.api_key = api_key
    
    def search(self):
        return Yelp_Search(self.api_key)