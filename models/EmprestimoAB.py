from .ModelBase import ModelAbstract


class EmprestimoAB(ModelAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'emprestimos-acervos-das-bibliotecas'
        self.file_pattern = 'Empréstimos de 20[0-9]{2}\\.[0-9]{1}'
