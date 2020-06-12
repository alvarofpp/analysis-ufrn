from .DataAbstract import DataAbstract


class Docente(DataAbstract):

    def __init__(self):
        super().__init__()
        self._dir = 'docentes'
        self.file_pattern = 'Docentes'
