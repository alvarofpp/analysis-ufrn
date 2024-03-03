from .ModelBase import ModelAbstract


class ComponenteCurricular(ModelAbstract):

    def __init__(self):
        super().__init__()
        self.dir = 'componentes-curriculares'
        self.file_pattern = '^Componentes Curriculares [a-zA-Z\\s\\-]*'
