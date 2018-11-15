from main.utility.io_utility import *

results = []
agency_data = read_csv_to_list(get_main_path("resources/User Raw Data/ou_data.csv"))
print(agency_data[0])
agency_data.pop(0)
cfo_col = 0
has_parent_col = 1
parent_col = 2
parent_abbrev_col = 3
agency_col = 4
agency_abbrev_col = 5
missing = "NA"

results = [["ORGANIZATION_ID", "PARENT_ORGANIZATION_ID", "NAME", "ABBREV", "NESTING_LEVEL", "PARENT"]]

relationships = {}
levels = {}
ids = {}
current_id = 1
executive_branch = {'name': 'executive branch'.upper(), 'level': 1, 'id':current_id}
results.append([executive_branch['id'], 'NA', executive_branch['name'], 'NA', executive_branch['level'], 'NA'])

current_id+=1

for row in agency_data:
    cfo = row[cfo_col]
    print(row)
    has_parent = row[has_parent_col].strip().upper()
    parent = row[parent_col].strip().upper()
    parent_abbrev = row[parent_abbrev_col].strip().upper()
    agency = row[agency_col].strip().upper()
    agency_abrev = row[agency_abbrev_col].strip().upper()

    if not parent in relationships.keys():

        if has_parent == "FALSE":
            relationships[parent] = executive_branch

        grand_parent = relationships[parent]
        grand_parent_level = grand_parent['level']
        level = grand_parent_level + 1
        id = current_id
        results.append([id, grand_parent['id'], parent, parent_abbrev, level, grand_parent['name']])
        levels[parent] = level
        ids[parent] = id
        current_id += 1

    if not agency == missing:

        agency_level = levels[parent] + 1
        parent_id = ids[parent]
        relationships[agency] = {'name':parent, 'level': level, 'id': id}
        agency_id = current_id
        results.append([agency_id, parent_id, agency, agency_abrev, agency_level, parent])
        levels[agency] = agency_level
        ids[agency] = agency_id
        current_id+=1


write_list_to_csv(results , get_main_path("resources/" + 'formatted_ou_data.csv'))
