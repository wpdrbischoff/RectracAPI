import RectracAPI 
import wpdconfig

api = RectracAPI.API()

api.auth(username=wpdconfig.USERNAME,password=wpdconfig.PASSWORD)

#params = {'fields': 'FacilityCode', 'limit': 55}
#data = api.query_endpoint(endpoint='facilities', params=params)
#PoC_print_data(data)

#params = {'limit': 5}
#data = api.query_endpoint(endpoint='households', params=params)
#PoC_print_data(data)

params = {'tablename': 'SASearchIndex', 
        'limit': 999, 
        'filterField': 'WordIndex', 
        'FilterBy': 'contains',
        'FilterValue': 'MO:AR*WB:Yes*MS:Active'}

table = 'SASearchIndex'

data = api.query_endpoint(endpoint=f'tables/{table}/data', params=params)
print(len(data['SASearchIndex']))
print(data['nextpage'])
