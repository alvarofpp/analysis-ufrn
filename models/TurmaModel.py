from .DataAbstract import DataAbstract


class TurmaModel(DataAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'turmas'
        self.file_pattern = 'Turmas de 20[0-9]{2}\\.[0-9]{1}'
