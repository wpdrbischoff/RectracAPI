import RectracAPI
import wpdconfig
import pprint

api = RectracAPI.API()

api.auth(username=wpdconfig.USERNAME,password=wpdconfig.PASSWORD)

#testing table query  / / gets all active, display on web, sections
params = {}
data = api.query_endpoint(endpoint=f'activities', params=params)
pprint.pprint(data)
