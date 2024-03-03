import pandas as pd


class Collection:
    def __init__(self, data):
        self._data = data

    def load(self):
        for key in self._data:
            self._data[key].load()

    def get_all_data(self):
        return self._data

    def get_data_from(self, from_key=None) -> 'pd.DataFrame':
        return self._data[from_key].get_data()
