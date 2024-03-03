from .ModelBase import ModelAbstract


class Curso(ModelAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'cursos-ufrn'
        self.file_pattern = 'Cursos da UFRN'
