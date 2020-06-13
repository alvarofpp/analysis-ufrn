import abc
from typing import Dict
from models import DataCollection


class TreatmentAbstract(abc.ABC):

    def __init__(self, data_collection):
        self.app_data = {
            'selects': {},
            'charts': {},
        }
        self.data_collection = DataCollection(data_collection)

    def get_data(self) -> Dict:
        return self.app_data

    def clear(self):
        for data in self.data_collection.get_all_data():
            del data
        self.data_collection = DataCollection({})

    @abc.abstractmethod
    def execute(self) -> Dict:
        self.data_collection.load()
        pass
