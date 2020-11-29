from .ModelAbstract import ModelAbstract


class Docente(ModelAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'docentes'
        self.file_pattern = 'Docentes'
