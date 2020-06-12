from .DataAbstract import DataAbstract


class Curso(DataAbstract):

    def __init__(self):
        super().__init__()
        self._dir = 'cursos-ufrn'
        self.file_pattern = 'Cursos da UFRN'
