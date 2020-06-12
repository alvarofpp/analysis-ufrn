from .DataAbstract import DataAbstract


class DocenteModel(DataAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'docentes'
        self.file_pattern = 'Docentes'
