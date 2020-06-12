from .DataAbstract import DataAbstract


class EmprestimoABModel(DataAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'emprestimos-acervos-das-bibliotecas'
        self.file_pattern = 'Empréstimos em 20[0-9]{2}\\.[0-9]{1}'
