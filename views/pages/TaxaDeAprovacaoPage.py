import pandas as pd
import streamlit as st

from .PageView import PageView


class TaxaDeAprovacaoPage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Taxa de Aprovação'
        self.data = pd.read_csv('data/taxas_aprovacao.csv')

    def intro(self):
        # Explicação sobre o trabalho
        st.markdown("""
        Aqui você conseguirá ver a taxa de aprovação das disciplinas. Foram disponibilizados dois
        tipos de visualizações: por docente e por componente curricular.

        Para a realização deste trabalho foram utilizados 4 conjuntos de dados presentes na base de
        [Dados abertos da UFRN](http://dados.ufrn.br/):

        - [docentes](#http://dados.ufrn.br/dataset/docentes);
        - [matrículas em componentes](#http://dados.ufrn.br/dataset/matriculas_componente);
        - [componentes curriculares](#http://dados.ufrn.br/dataset/componentes_curriculares);
        - [turmas](#http://dados.ufrn.br/dataset/turmas).

        Foram usados apenas dados de turmas consolidadas e as matrículas com status de aprovado ou
        reprovado.
        A ordem apresentada é da maior taxa de aprovação até a menor.
        """, unsafe_allow_html=True)

    def section_01(self):
        st.markdown("""
        ## Docente

        Aqui você poderá buscar por um docente e visualizar a sua taxa de aprovação para cada
        disciplina lecionada por ele.
        """, unsafe_allow_html=True)
        option_docente = st.selectbox(
            'Docente',
            options=self.data['siape'].unique().tolist(),
            format_func=self.format_func_docentes,
        )

        taxa_aprovacao_docente = self.data[self.data['siape'] == option_docente]
        taxa_aprovacao_docente = taxa_aprovacao_docente[['nome_componente', 'taxa_aprovacao']]
        taxa_aprovacao_docente = taxa_aprovacao_docente.sort_values(
            'taxa_aprovacao',
            ascending=False,
        ).reset_index(drop=True)
        taxa_aprovacao_docente.index = taxa_aprovacao_docente.index + 1
        taxa_aprovacao_docente = taxa_aprovacao_docente.rename(columns={
            'nome_componente': 'Nome do componente curricular',
            'taxa_aprovacao': 'Taxa de aprovação',
        })
        st.table(taxa_aprovacao_docente)

    def section_02(self):
        st.markdown("""
        ## Componente curricular

        Aqui você poderá buscar pelo componente curricular e visualizar a taxa de aprovação por
        docente que já lecionou esse componente.
        """, unsafe_allow_html=True)
        option_docente = st.selectbox(
            'Componente Curricular',
            options=self.data['id_componente_curricular'].unique().tolist(),
            format_func=self.format_func_componentes_curriculares,
        )

        taxa_aprovacao_componente = self.data[
            self.data['id_componente_curricular'] == option_docente
            ][['nome_docente', 'taxa_aprovacao']]
        taxa_aprovacao_componente = taxa_aprovacao_componente.sort_values(
            'taxa_aprovacao',
            ascending=False).reset_index(drop=True)
        taxa_aprovacao_componente.index = taxa_aprovacao_componente.index + 1
        taxa_aprovacao_componente = taxa_aprovacao_componente.rename(columns={
            'nome_docente': 'Nome do docente',
            'taxa_aprovacao': 'Taxa de aprovação',
        })
        st.table(taxa_aprovacao_componente)

    def format_func_componentes_curriculares(self, option):
        return self.data[self.data['id_componente_curricular'] == option]['nome_componente'].iloc[0]

    def format_func_docentes(self, option):
        return self.data[self.data['siape'] == option]['nome_docente'].iloc[0]
