from main.utility.io_utility import *

address_list = []
address_data = read_csv_to_list(get_main_path("resources/User Raw Data/address_data.csv"))
address_data.pop(0)
for x in address_data:
    item = {}
    item['street'] = x[0]
    item['city'] = x[1]
    item['state'] = x[2]
    item['zip'] = x[3]
    item['country'] = x[4]
    address_list.append(item)
print(address_list )

write_dictionary_to_file(address_list, get_main_path("resources/User Raw Data/address.json"))