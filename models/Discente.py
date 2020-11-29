from .ModelAbstract import ModelAbstract


class Discente(ModelAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'discentes'
        self.file_pattern = 'Ingressantes em 20[0-9]{2}\\.[0-9]{1}'
