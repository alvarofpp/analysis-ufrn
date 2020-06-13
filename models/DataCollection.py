import pandas as pd
from .CursoModel import CursoModel
from .TurmaModel import TurmaModel
from .DocenteModel import DocenteModel
from .MatriculaModel import MatriculaModel


class DataCollection:
    def __init__(self, data):
        self._data = data

    def load(self):
        for key in self._data.keys():
            self._data[key].load()

    def get_all_data(self):
        return self._data

    def get_data_from(self, from_key=None) -> 'pd.DataFrame':
        return self._data[from_key].get_data()
