import random
from datetime import datetime, timedelta
from main.generation.abstract_data_generator import AbstractDataGenerator
from main.utility.io_utility import *

class UserDataGenerator(AbstractDataGenerator):

    FIELDS = ["FIRST_NAME", "LAST_NAME", "ACCOUNT_NUMBER", "USERNAME", "AGENCY", "DEPARTMENT", "HIRE_DATE",
              "ADDRESS_STREET", "ADDRESS_CITY", "ADDRESS_STATE", "ADDRESS_ZIP", "ADDRESS_COUNTRY", "ROLE"]

    def __init__(self):
        super().__init__(UserDataGenerator.FIELDS)
        self.agency_data = read_dictionary_from_file(get_main_path("resources/User Raw Data/department_agency.json"))
        name_role_data = read_dictionary_from_file(get_main_path("resources/User Raw Data/names_roles.json"))
        self.first_name_data = name_role_data['first_names']
        self.last_name_data = name_role_data['last_names']
        self.role_data = name_role_data['roles']
        self.address_data = read_dictionary_from_file(get_main_path("resources/User Raw Data/address.json"))

    def __get_first_name(self):
        return UserDataGenerator.get_random_element(self.first_name_data)

    def __get_last_name(self):
        return UserDataGenerator.get_random_element(self.last_name_data)

    def __get_role(self):
        return UserDataGenerator.get_random_element(self.role_data)

    def __get_agency_and_department(self):
        return UserDataGenerator.get_random_element(self.agency_data)

    def __get_address(self):
        return UserDataGenerator.get_random_element(self.address_data)

    @staticmethod
    def generate_hire_date():
        min_year = 1980
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = datetime.now().year - min_year + 1
        end = start + timedelta(days=365 * years)
        date_time = start + (end - start) * random.random()
        return date_time.strftime("%Y%m%d")

    @staticmethod
    def get_random_element(element_list):
        return element_list[random.randint(0, len(element_list)-1)]

    @staticmethod
    def generate_account_number():
        return str(random.randint(1000000, 9999999))

    @staticmethod
    def create_user_name(first_name, last_name):
        return first_name+'.'+last_name

    def generate_data(self, num_records):
        for i in range(0, num_records):
            first_name = self.__get_first_name()
            last_name = self.__get_last_name()
            account_number = UserDataGenerator.generate_account_number()
            username = UserDataGenerator.create_user_name(first_name, last_name)
            agency_dict = self.__get_agency_and_department()
            agency = agency_dict['agency']
            department = agency_dict['department']
            hire_date = UserDataGenerator.generate_hire_date()
            address_dict = self.__get_address()
            street = address_dict['street']
            city = address_dict['city']
            state = address_dict['state']
            zipcode = address_dict['zip']
            country = address_dict['country']
            role = self.__get_role()

            self.data.append([first_name, last_name, account_number, username, agency, department, hire_date,
                              street, city, state, zipcode, country, role])
