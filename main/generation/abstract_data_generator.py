import abc

class AbstractDataGenerator:

    def __init__(self, field_names):
        self.field_names = field_names
        self.data = self._populate_data_header(field_names)

    def _populate_data_header(self, field_names):
        pass

    def write_file(self, file_name):
        pass

    @abc.abstractmethod
    def generate_data(self, num_records):
        pass

