from main.utility.io_utility import *

data = []
for line in open(get_main_path("resources/splunk/winEventLog60min_all_fields_7-November.json"), 'r'):
    data.append(json.loads(line))

print("number of records " + str(len(data)))

for record in data:
    if record['preview'] != False:
        print(record['preview'])

keys = set(data[0]['result'].keys())
print("key set size " + str(len(keys)))
for record in data:
    keys.update(list(record['result'].keys()))
    print("key set size " + str(len(keys)))

keys = list(sorted(keys))


field_type = {}
for record in data:
    result = record['result']
    for x in keys:
        try:
            value_type = str(type(result[x]))
            try:
                current_value = field_type[x]
                if value_type is not current_value:
                    if value_type == '<class \'str\'>' and current_value == ' <class \'list\'>':
                        pass
                    elif value_type == '<class \'list\'>' and current_value == ' <class \'str\'>':
                        field_type[x] = value_type
                else:
                    raise ValueError('type does not match; key = ' + x + ' current = ' + current_value + ' ;new = ' + value_type)
            except KeyError:
                field_type[x] = value_type
        except KeyError:
            pass






