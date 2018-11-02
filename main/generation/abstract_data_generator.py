import abc


class AbstractDataGenerator:

    def __init__(self, field_names):
        self.field_names = field_names
        self.data = self._populate_data_header(field_names)

    def _populate_data_header(self, field_names):
        if type(field_names) == list:
            data = field_names
            return data
        else:
            raise ValueError("field_names must be list")

    @abc.abstractmethod
    def generate_data(self, num_records):
        pass
