import RectracAPI
import wpdconfig
import pprint

api = RectracAPI.API()

api.auth(username=wpdconfig.USERNAME,password=wpdconfig.PASSWORD)

#testing facility
#params = {'fields': 'FacilityCode', 'limit': 55}
#data = api.query_endpoint(endpoint='facilities', params=params)
#PoC_print_data(data)

#testing households
#params = {'limit': 5}
#data = api.query_endpoint(endpoint='households', params=params)
#PoC_print_data(data)


#testing table query  / / gets all active, display on web, sections
params = {}
data = api.query_endpoint(endpoint=f'activities', params=params)
pprint.pprint(data)
