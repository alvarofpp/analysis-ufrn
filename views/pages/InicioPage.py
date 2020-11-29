import streamlit as st
from .PageView import PageView


class InicioPage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Início'

    def intro(self):
        # Explicação sobre o trabalho
        st.markdown("""
        # Objetivo
        Esse aplicativo tem como objetivo facilitar a visualização dos dados abertos da
        Universidade Federal do Rio Grande do Norte (UFRN).
        O principal foco é sobre taxas de aprovação, sendo que outros tipos de analises
        serão postos aqui.
        
        - [Dados abertos da UFRN](http://dados.ufrn.br/)
        """, unsafe_allow_html=True)
