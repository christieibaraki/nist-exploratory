from main.utility.io_utility import *

agency_list = []
agency_data = read_csv_to_list(get_main_path("resources/User Raw Data/agency_data.csv"))
agency_data.pop(0)
for x in agency_data:
    item = {}
    item['department'] = x[0]
    item['agency'] = x[1]
    if item['agency'] != "":
        agency_list.append(item)
print(agency_list)

write_dictionary_to_file(agency_list, get_main_path("resources/User Raw Data/department_agency.json"))
