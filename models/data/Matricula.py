from .DataAbstract import DataAbstract


class Matricula(DataAbstract):

    def __init__(self):
        super().__init__()
        self._dir = 'matriculas-componentes'
        self.file_pattern = 'Matrículas de 20[0-9]{2}\\.[0-9]{1}'
