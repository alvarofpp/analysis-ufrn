from .ModelBase import ModelAbstract


class AcervoExemplar(ModelAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'acervo-biblioteca'
        self.file_pattern = 'Acervo de Exemplares das Bibliotecas'
