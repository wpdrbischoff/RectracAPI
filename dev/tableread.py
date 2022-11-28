import RectracAPI
import wpdconfig
import pprint

api = RectracAPI.API()

api.auth(username=wpdconfig.USERNAME,password=wpdconfig.PASSWORD)

#testing table query  / / gets all active, display on web, sections
params = {'tablename': 'SASearchIndex',
        'limit': 999,
        'filterField': 'WordIndex',
        'FilterBy': 'contains',
        'FilterValue': 'MO:AR*WB:Yes*MS:Active'}

table = 'SASearchIndex'
data = api.query_endpoint(endpoint=f'tables/{table}/data', params=params)
pprint.pprint(data)



#testing offset table query
#params = {'tablename': 'SASearchIndex',
#        'limit': 2,
#        'offset': 999
#        'filterField': 'WordIndex',
#        'FilterBy': 'contains',
#        'FilterValue': 'MO:AR*WB:Yes*MS:Active'}

#data = api.query_endpoint(endpoint=f'tables/{table}/data', params=params)
#pprint.pprint(data['SASearchIndex'])
#pprint.pprint(data)
