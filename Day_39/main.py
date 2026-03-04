import flight_data as fd
import flight_search as fs
import data_manager as dm
import notification_manager as sm

token = fd.FlightData() # validating and getting token
f_dest = fs.FlightSearch(token.token)
sen_msg = sm.NotificationManager()
f_s = dm.DataManager() # constructor gets data from google sheet

# f_s.put_data_series(f_dest.get_iata_codes(city_list=f_s.get_cities())) # updating iata codes on google sheet
# f_dest.get_cheapest_flights_v2()
# print(f_s.get_cities())
# print(f_dest.get_iata_codes(city_list=f_s.get_cities()))
# lis = f_dest.get_iata_codes(city_list=f_s.get_cities())
# f_dest.get_kgmid_to_file(f_s.get_cities())
# f_s.put_data_series(what='cityLocCode',data_list=list_)
# list_ = f_dest.retrieve_kgmid_from_file()
# f_dest.get_cheapest_flights_v4(data_list=list_)
# print(f_s.make_a_dict())

f_dest.get_fl_of_search()

# fd = f_s.make_flights_dict()
# msg = (f'Low price alert ! Only €{fd['Paris']['price']} to fly from {fd['Paris']['depCode']}'
#  f' to {fd['Paris']['arrCode']} on {fd['Paris']['depDate']}')
#
# bargain_prices = [value for value in f_s.make_a_dict().values()]
# actual_prices = [int(value['price']) for value in f_s.make_flights_dict().values()]
#
# for _ in range(len(actual_prices)):
#   if actual_prices[_] < bargain_prices[_]:
#     print('bargain !')
#     sen_msg.send_sms(msg=msg)
#   else:
#     print('maybe next time')
