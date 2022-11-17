import RectracAPI 
import wpdconfig

api = RectracAPI.API()

api.auth(username=wpdconfig.USERNAME,password=wpdconfig.PASSWORD)

def PoC_print_data(data):
    for i in data[1]:
        print(i)

params = {'fields': 'FacilityCode', 'limit': 55}
data = api.query_endpoint(endpoint='facilities', params=params)
PoC_print_data(data)

params = {'limit': 5}
data = api.query_endpoint(endpoint='households', params=params)
PoC_print_data(data)
