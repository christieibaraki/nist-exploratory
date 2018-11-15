import random
from datetime import datetime, timedelta
from main.utility.io_utility import *

class FieldGenerator():

    DEFAULT_MIN_YEAR = 1980

    def __init__(self):
        self.agency_data = read_dictionary_from_file(get_main_path("resources/User Raw Data/department_agency.json"))
        name_role_data = read_dictionary_from_file(get_main_path("resources/User Raw Data/names_roles.json"))
        self.first_name_data = name_role_data['first_names']
        self.last_name_data = name_role_data['last_names']
        self.role_data = name_role_data['roles']
        self.address_data = read_dictionary_from_file(get_main_path("resources/User Raw Data/address.json"))

    # Output: dictionary with the following keys:
    # street, city, state, zip, country
    def __get_address(self):
        return FieldGenerator.get_random_element(self.address_data)

    @staticmethod
    def generate_date_YYYYMMDD(min_year = None):
        min_year = FieldGenerator.DEFAULT_MIN_YEAR  if min_year is None else min_year
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = datetime.now().year - min_year + 1
        end = start + timedelta(days=365 * years)
        date_time = start + (end - start) * random.random()
        return date_time.strftime("%Y%m%d")

    # Output: dictionary with the following keys:
    # agency, department
    def __get_agency_and_department(self):
        return FieldGenerator.get_random_element(self.agency_data)

    @staticmethod
    def get_device_name(self):
        pass

    @staticmethod
    def get_device_type(self):
        pass

    @staticmethod
    def get_dns_name(self):
        pass

    def get_hostname(self):
        pass

    @staticmethod
    def get_email_address(username, agency, department):
        pass

    def __get_first_name(self):
        return FieldGenerator.get_random_element(self.first_name_data)

    def __get_last_name(self):
        return FieldGenerator.get_random_element(self.last_name_data)

    def __get_role(self):
        return FieldGenerator.get_random_element(self.role_data)

    @staticmethod
    def get_ip_address():
        pass

    @staticmethod
    def get_mac_address():
        pass

    @staticmethod
    def get_office():
        pass

    @staticmethod
    def get_ad_account():
        pass



    @staticmethod
    def get_password_strength():
        # TODO
        pass



    @staticmethod
    def get_random_element(element_list):
        return element_list[random.randint(0, len(element_list) - 1)]

    @staticmethod
    def generate_account_number():
        return str(random.randint(1000000, 9999999))

    @staticmethod
    def create_user_name(first_name, last_name):
        return first_name + '.' + last_name
