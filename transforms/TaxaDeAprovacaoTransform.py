from models import Curso, Docente, MatriculaComponente, Turma
from .TransformAbstract import TransformAbstract


class TaxaDeAprovacaoTransform(TransformAbstract):
    def __init__(self):
        super().__init__({
            'cursos': Curso(),
            #'docentes': Docente(),
            'matriculas_componente': MatriculaComponente(),
            #'turmas': Turma(),
        })

    def execute(self):
        super().execute()

        # Niveis de ensino da UFRN
        niveis_ensino = self.data_collection \
            .get_data_from('cursos')['nivel_ensino'] \
            .unique() \
            .sort_values() \
            .tolist()
        self.app_data['selects']['niveis_ensino'] = niveis_ensino

        # Cursos da UFRN
        cursos = self.data_collection \
            .get_data_from('cursos')[['id_curso', 'nome', 'nivel_ensino',]] \
            .to_dict('records')
        self.app_data['selects']['cursos_por_nivel'] = {
                nivel_ensino: [
                    curso['id_curso'] for curso in cursos
                    if curso['nivel_ensino'] == nivel_ensino
                ]
                for nivel_ensino in niveis_ensino
            }
        self.app_data['selects']['cursos_por_id'] = {
            curso['id_curso']: curso['nome'] for curso in cursos
        }
