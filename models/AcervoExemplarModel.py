from .DataAbstract import DataAbstract


class AcervoExemplarModel(DataAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'acervo-biblioteca'
        self.file_pattern = 'Acervo de Exemplares das Bibliotecas'
