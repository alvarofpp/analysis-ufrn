import pandas as pd
from .data.Curso import Curso
from .data.Turma import Turma
from .data.Docente import Docente
from .data.Matricula import Matricula


class DataCollection:
    def __init__(self):
        self._data = {
            'docentes': Docente(),
            'matriculas': Matricula(),
            'turmas': Turma(),
            'cursos': Curso(),
        }

    def load(self):
        for key in self._data.keys():
            self._data[key].load()

    def get_data_from(self, from_key=None) -> 'pd.DataFrame':
        return self._data[from_key].get_data()
