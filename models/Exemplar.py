from .ModelAbstract import ModelAbstract


class Exemplar(ModelAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'acervo-biblioteca'
        self.file_pattern = 'Exemplares - Versão 2'
