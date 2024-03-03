from .ModelBase import ModelAbstract


class MatriculaComponente(ModelAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'matriculas-componentes'
        self.file_pattern = 'Matrículas de 20[0-9]{2}\\.[0-9]{1}'
