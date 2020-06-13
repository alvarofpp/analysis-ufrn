from models import DataCollection, AcervoExemplarModel, CursoModel, EmprestimoABModel, ExemplarModel
from .TreatmentAbstract import TreatmentAbstract


class BibliotecaTreatment(TreatmentAbstract):
    def __init__(self):
        super().__init__({
            # 'acervo_exemplares': AcervoExemplarModel(),
            # 'cursos': CursoModel(),
            # 'emprestimos': EmprestimoABModel(),
            'exemplares': ExemplarModel(),
        })

    def execute(self):
        super().execute()
        qeb = self.data_collection \
            .get_data_from('exemplares')[
            "biblioteca"] \
            .value_counts() \
            .to_dict()

        self.app_data['charts']['quantidade_exemplares_por_biblioteca'] = qeb #sorted(qeb.items(), key = lambda x: x[1])
