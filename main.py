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
params = {'tablename': 'SASearchIndex', 
        'limit': 999, 
        'filterField': 'WordIndex', 
        'FilterBy': 'contains',
        'FilterValue': 'MO:AR*WB:Yes*MS:Active'}

table = 'SASearchIndex'

data = api.query_endpoint(endpoint=f'tables/{table}/data', params=params)
print(len(data['SASearchIndex']))
#print(data['nextpage'])

#testing offset table query
params = {'tablename': 'SASearchIndex', 
        'limit': 999,
        'offset': 999,
        'filterField': 'WordIndex', 
        'FilterBy': 'contains',
        'FilterValue': 'MO:AR*WB:Yes*MS:Active'}

data = api.query_endpoint(endpoint=f'tables/{table}/data', params=params)
print(len(data['SASearchIndex']))
pprint.pprint(data['SASearchIndex'])
