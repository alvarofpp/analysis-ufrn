from models import AcervoExemplar, Exemplar

from .TransformerAbstract import TransformerAbstract


class BibliotecaTransformer(TransformerAbstract):
    def __init__(self):
        super().__init__({
            'acervo_exemplares': AcervoExemplar(),
            'exemplares': Exemplar(),
            # 'cursos': CursoModel(),
            # 'emprestimos': EmprestimoABModel(),
        })

    def execute(self):
        super().execute()

        # Quantidade de exemplares por biblioteca
        self.app_data['charts']['quantidade_exemplares_por_biblioteca'] =  \
            self.data_collection \
            .get_data_from('exemplares')['biblioteca'] \
            .value_counts() \
            .to_dict()

        # Quantidade de exemplares por tipo
        self.app_data['charts']['quantidade_exemplares_por_tipo'] =  \
            self.data_collection \
            .get_data_from('acervo_exemplares')['tipo_material'] \
            .value_counts() \
            .to_dict()
