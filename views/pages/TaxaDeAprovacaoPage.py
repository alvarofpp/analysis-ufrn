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
            'cursos': AppData.data_get('taxa-aprovacao.selects.cursos'),
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
            'curso': st.selectbox('Curso', options=list(self.data['cursos'].keys()), format_func=self.format_func_curso),
        }

    def format_func_curso(self, option):
        return self.data['cursos'][str(option)]
