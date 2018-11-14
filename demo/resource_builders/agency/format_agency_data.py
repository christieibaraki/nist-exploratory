from main.utility.io_utility import *

results = []
agency_data = read_csv_to_list(get_main_path("resources/User Raw Data/ou_data.csv"))
print(agency_data[0])
agency_data.pop(0)
cfo_col = 0
has_parent = 1
parent_col = 2
parent_abbrev_col = 3
agency_col = 4
agency_abbrev_col = 5
missing = "NA"

relationships = {}
current_id = 1
executive_branch = {'name':'executive branch', 'level': 1, 'id':current_id}


for row in agency_data:
    cfo = row[cfo_col]
    has_parent = row[has_parent]
    parent = row[parent_col]
    parent_abbrev = row[parent_abbrev_col]
    agency_col = row[agency_col]
    agency_abrev = row[agency_abbrev_col]