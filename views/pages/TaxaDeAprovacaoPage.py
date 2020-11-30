import pandas as pd
import altair as alt
import streamlit as st
from data.AppData import AppData
from .PageView import PageView


class TaxaDeAprovacaoPage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Taxa de Aprovação'
        self.data = {
            'cursos_por_nivel': AppData.data_get('taxa-aprovacao.selects.cursos_por_nivel'),
            'cursos_por_id': AppData.data_get('taxa-aprovacao.selects.cursos_por_id'),
        }
        self.selects = {}

    def intro(self):
        # Explicação sobre o trabalho
        st.markdown('''
        Aqui você conseguirá ver a taxa de aprovação das disciplinas. Para isso, selecione corretamente os campos de seleção.
        
        Para a realização deste trabalho foram utilizados 5 conjuntos de dados presentes na base de [Dados abertos da UFRN](http://dados.ufrn.br/):
        
        - [cursos](#http://dados.ufrn.br/dataset/cursos-ufrn): contêm os dados referentes aos cursos ofertados na UFRN;
        ''', unsafe_allow_html=True)

        self.selects = {
            'nivel_ensino': st.selectbox('Nível de Ensino', AppData.data_get('taxa-aprovacao.selects.niveis_ensino')),
        }
        # st.json(test)
        self.selects['curso'] = st.selectbox('Cursos',
                                        options=self.data['cursos_por_nivel'][self.selects['nivel_ensino']],
                                        format_func=self.format_func_curso)

    def format_func_curso(self, option):
        return self.data['cursos_por_id'][option]