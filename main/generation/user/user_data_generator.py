from main.generation.abstract_data_generator import AbstractDataGenerator


class UserDataGenerator(AbstractDataGenerator):

    FIELDS = ["FIRST_NAME", "LAST_NAME", "ACCOUNT_NUMBER", "USERNAME", "DEPARTMENT", "HIRE_DATE", "ADDRESS", "ROLE"]

    def __init__(self):
        super().__init__(UserDataGenerator.FIELDS)

    def generate_data(self):
        pass