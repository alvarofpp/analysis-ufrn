import abc
from typing import Dict
from supports import Collection


class TreatmentAbstract(abc.ABC):

    def __init__(self, data_collection):
        self.app_data = {
            'charts': {},
            'data': {},
            'selects': {},
        }
        self.data_collection = Collection(data_collection)

    def get_data(self) -> Dict:
        return self.app_data

    def clear(self):
        for data in self.data_collection.get_all_data():
            del data
        self.data_collection = Collection({})

    @abc.abstractmethod
    def execute(self) -> Dict:
        self.data_collection.load()
        pass
