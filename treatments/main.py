import json
from models import CursoModel
from models.DataCollection import DataCollection


# Variável que conterá os dados para o app
app_json = {
    'niveis_ensino': None,
    'cursos': None,
}

# Carrega os dados
data_collection = DataCollection({
            # 'docentes': Docente(),
            # 'matriculas': Matricula(),
            # 'turmas': Turma(),
            'cursos': CursoModel(),
        })
data_collection.load()

# Select dos níveis de ensino
niveis_ensino = sorted(data_collection.get_data_from('cursos')['nivel_ensino'].unique())
app_json['niveis_ensino'] = [nivel_ensino.title() for nivel_ensino in niveis_ensino]

# Cria o arquivo JSON
with open('data.json', 'w') as outfile:
    json.dump(app_json, outfile, indent=2, sort_keys=True)
