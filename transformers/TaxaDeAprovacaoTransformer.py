import numpy as np
import pandas as pd
from tqdm import tqdm

from models import ComponenteCurricular, Docente, MatriculaComponente, Turma

from .TransformerAbstract import TransformerAbstract


class TaxaDeAprovacaoTransformer(TransformerAbstract):
    def __init__(self):
        super().__init__({
            'docentes': Docente(),
            'matriculas_componente': MatriculaComponente(),
            'componentes_curriculares': ComponenteCurricular(),
            'turmas': Turma(),
        })

    def execute(self):
        super().execute()

        # Taxa de aprovação
        # Dataframe das turmas
        df_turmas = self.data_collection.get_data_from('turmas')
        df_turmas = df_turmas[df_turmas['situacao_turma'] == 'CONSOLIDADA']
        df_turmas = df_turmas[['id_turma', 'id_componente_curricular', 'siape']]

        # Dataframe dos docentes
        df_docentes = self.data_collection.get_data_from('docentes')
        df_docentes = df_docentes[['siape', 'nome']]

        # Dataframe das turmas com os docentes
        df_dt = pd.merge(df_turmas, df_docentes, on='siape', how='inner')

        # Dataframe dos componentes curriculares
        df_componentes = self.data_collection \
            .get_data_from('componentes_curriculares')
        df_componentes = df_componentes[['id_componente', 'codigo', 'nome']]
        df_componentes['nome'] = df_componentes['codigo'] + ' - '  \
                                 + df_componentes['nome']
        df_componentes.drop(columns=['codigo'], inplace=True)

        # Dataframe das turmas com os docentes e os componentes curriculares
        df_dtc = pd.merge(
            df_dt,
            df_componentes,
            left_on='id_componente_curricular',
            right_on='id_componente',
            how='inner',
            suffixes=('_docente', '_componente'),
        )
        df_dtc.drop(columns=['id_componente'], inplace=True)
        df_dtc['taxa_aprovacao'] = np.nan

        # Dataframe das matriculas dos componentes
        df_matriculas_componente = self.data_collection \
            .get_data_from('matriculas_componente')

        # Calculando a taxa de aprovação de cada turma
        for index, row in tqdm(df_dtc.iterrows(), total=df_dtc.shape[0]):
            # Matriculas daquela turma
            matriculas_turma = df_matriculas_componente[
                df_matriculas_componente['id_turma'] == row['id_turma']
            ]

            if matriculas_turma['discente'].count() == 0:
                continue

            # Matriculas aprovadas
            matriculas_turma_aprovadas = matriculas_turma[
                matriculas_turma['descricao'].isin([
                    'APROVADO',
                    'APROVADO POR NOTA',
                ])
            ]

            # Todas as matriculas válidas
            matriculas_turma_totais = matriculas_turma[
                matriculas_turma['descricao'].isin([
                    'APROVADO',
                    'APROVADO POR NOTA',
                    'REPROVADO',
                    'REPROVADO POR NOTA',
                    'REPROVADO POR FALTAS',
                    'REPROVADO POR NOTA E FALTA',
                    'REPROVADO POR MÉDIA E POR FALTAS',
                    'REPROVADO EM TODO PERÍODO LETIVO',
                ])
            ]

            count_aprovados = matriculas_turma_aprovadas['discente'].count()
            count_total = matriculas_turma_totais['discente'].count()

            if count_total == 0:
                continue

            if count_aprovados == 0:
                df_dtc.loc[index, 'taxa_aprovacao'] = 0.0

            # Calculando a taxa de aprovação e salvando
            df_dtc.loc[index, 'taxa_aprovacao'] = (
                    matriculas_turma_aprovadas['discente'].count() * 100 /
                    matriculas_turma_totais['discente'].count()
            )

        # Ajustes
        df_dtc.dropna(inplace=True)
        df_dtc['taxa_aprovacao'] = df_dtc['taxa_aprovacao'].astype(float)

        # Dataframe final
        df_mean = df_dtc.groupby(
            ['id_componente_curricular', 'siape']
        )['taxa_aprovacao'].mean()
        df_mean = df_mean.reset_index()
        df_mean = pd.merge(df_mean, df_docentes, on='siape', how='inner')
        df_mean = pd.merge(
            df_mean,
            df_componentes,
            left_on='id_componente_curricular',
            right_on='id_componente',
            suffixes=('_docente', '_componente'),
            how='inner',
        )
        df_mean.drop(columns=['id_componente'], inplace=True)
        df_mean.to_csv('data/taxas_aprovacao.csv', index=False)
