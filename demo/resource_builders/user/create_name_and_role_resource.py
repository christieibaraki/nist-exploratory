import random
from main.utility.io_utility import *

'''
This creates a resource file from which first names, last names, and roles
can be selected to generate user data.
'''

name_column = 0
job_column = 1
num_first_name = 2000
num_last_name = 3000
num_jobs = 1000
first_names = []
last_names = []
jobs = []

firstname_list = read_csv_to_list(get_main_path("resources/User Raw Data/yob2017.txt"))
lastname_list = read_csv_to_list(get_main_path("resources/User Raw Data/Names_2010Census.csv"))
lastname_list.pop(0)  # remove header

firstname_indices = random.sample(range(1, len(firstname_list)), num_first_name)
for i in firstname_indices:
    first_names.append(firstname_list[i][name_column].upper())

lastname_indices = random.sample(range(1, len(lastname_list)), num_last_name)
for i in lastname_indices:
    last_names.append(lastname_list[i][name_column].upper())

print("number of first names: " + str(len(first_names)))
print("number of last names: " + str(len(last_names)))

job_list = read_csv_to_list(get_main_path("resources/User Raw Data/Job_Titles_by_Classification.csv"))
job_list.pop(0)  # remove header

i = 0
while (len(jobs) < num_jobs and i < len(job_list)):
    if ',' not in job_list[i][job_column]:
        jobs.append(job_list[i][job_column].upper())
    i += 1

print("number of jobs: " + str(len(jobs)))

results = {}
results["first_names"] = first_names
results["last_names"] = last_names
results["roles"] = jobs

write_dictionary_to_file(results, get_main_path("resources/User Raw Data/names_roles.json"))
