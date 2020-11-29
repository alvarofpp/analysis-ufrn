import pandas as pd
import altair as alt
import streamlit as st
from data.AppData import AppData
from .PageView import PageView
from ..components import TableTop


class BibliotecaPage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Biblioteca'

    def intro(self):
        # Explicação sobre o trabalho
        st.markdown("""
        # Introdução
        Bibliotecas fornecem o suporte informacional para o desenvolvimento intelectual dos integrantes de uma comunidade acadêmica, contribuindo para a produtividade através da disponibilização de diversos materiais. De acordo com um estudo divulgado pela revista acadêmica College & Research Libraries, sob autoria de Krista M. Soria, Jan Fransen, and Shane Nackerud, alunos que usam os recursos das bibliotecas acadêmicas, pelo menos uma vez no primeiro ano de ensino superior, possuem uma maior probabilidade de se formarem ou permanecerem na instituição acadêmica após 4 anos.
        
        Diante disso, tornou-se objetivo deste projeto analisar informações referentes ao acervo das bibliotecas da Universidade Federal do Rio Grande do Norte (UFRN), por meio de dados obtidos através do Portal de Dados Abertos da UFRN. O sistema de bibliotecas da UFRN é composto pela Biblioteca Central Zila Mamede (BCZM), a qual possui mais de 434.500 exemplares, e outras 21 bibliotecas setoriais.
        
        Para a realização deste trabalho foram utilizados 5 conjuntos de dados presentes na base de [Dados abertos da UFRN](http://dados.ufrn.br/):
        
        - [cursos](#http://dados.ufrn.br/dataset/cursos-ufrn): contêm os dados referentes aos cursos ofertados na UFRN;
        - [discentes](#http://dados.ufrn.br/dataset/discentes): contêm os dados dos alunos ingressantes na UFRN;
        - [exemplares](#http://dados.ufrn.br/dataset/acervo-biblioteca): contêm os dados referentes aos exemplares presentes na UFRN;
        - [acervo-exemplares](#http://dados.ufrn.br/dataset/acervo-biblioteca): contêm os dados acerca dos materiais presentes no acervo das bibliotecas da UFRN;
        - [emprestimos-acervos-das-bibliotecas](#http://dados.ufrn.br/dataset/emprestimos-acervos-das-bibliotecas): contêm os dados dos empréstimos feitos do acervo das bibliotecas da UFRN;

        As análises estão divididas em nas seguintes seções:
        - Acervo
        - Empréstimos
        - Recomendações
        """, unsafe_allow_html=True)

        st.markdown("""
        # Acervo
        Aqui consta as análises acerca do acervo das bibliotecas da UFRN.
        """)
        exemplares = pd.DataFrame(AppData.data_get('acervo-biblioteca.charts.quantidade_exemplares_por_tipo').items(),
                           columns=['Tipo', 'Quantidade de Exemplares'])

        st.write('Atualmente as bibliotecas da UFRN possuem um total de {} exemplares em seu acervo, categorizados em {} tipos.'.format(
            exemplares['Quantidade de Exemplares'].sum(),
            exemplares.shape[0]
        ))

    def section_01(self):
        st.markdown("""
        ## Qual biblioteca possui o maior acervo?
        Para responder essa pergunta, iremos realizar um processo simples de contagem dos exemplares nas bibliotecas.
        """)

        # Quantidade de exemplares por biblioteca
        qeb = pd.DataFrame(AppData.data_get('acervo-biblioteca.charts.quantidade_exemplares_por_biblioteca').items(),
                           columns=['Biblioteca', 'Quantidade de Exemplares'])
        st.bar_chart(
            pd.Series(
                qeb['Quantidade de Exemplares'].to_list(),
                qeb['Biblioteca'].to_list()
            ),
            height=500
        )

        # Biblioteca com maior acervo
        biblioteca_max = qeb.iloc[qeb['Quantidade de Exemplares'].idxmax()]
        msg_max = 'Algo interessante a observar é que uma única biblioteca ({}) possui {:.2f}% do total de exemplares.'
        st.write(msg_max.format(
            biblioteca_max.at['Biblioteca'],
            (biblioteca_max.at['Quantidade de Exemplares'] * 100) / qeb['Quantidade de Exemplares'].sum()
        ))

        # Top 5 bibliotecas por tamanho do acervo
        st.write('Top 5 bibliotecas com maior quantidade de exemplares:')
        TableTop.render(qeb, 'Quantidade de Exemplares', 5)

        # Exemplares por tipo
        st.markdown('## Distribuição dos exemplares por tipo:')
        qet = pd.DataFrame(AppData.data_get('acervo-biblioteca.charts.quantidade_exemplares_por_tipo').items(),
                           columns=['Tipo', 'Quantidade de Exemplares'])
        st.bar_chart(
            pd.Series(
                qet['Quantidade de Exemplares'].to_list(),
                qet['Tipo'].to_list()
            ),
            height=500
        )

        # Tipo com maior acervo
        tipo_max = qet.iloc[qet['Quantidade de Exemplares'].idxmax()]
        msg_max = 'Algo interessante a observar é que um único tipo ({}) possui {:.2f}% do total de exemplares.'
        st.write(msg_max.format(
            tipo_max.at['Tipo'],
            (tipo_max.at['Quantidade de Exemplares'] * 100) / qet['Quantidade de Exemplares'].sum()
        ))

        # Top 5 tipos por tamanho do acervo
        st.write('Top 5 tipos com maior quantidade de exemplares:')
        TableTop.render(qet, 'Quantidade de Exemplares', 5)

    def section_02(self):
        # st.bar_chart
        st.markdown("""
        # Empréstimos
        Aqui consta as análises acerca dos empréstimos de material das bibliotecas da UFRN.
        
        ## Quais são os livros mais e menos emprestados?
        
        """)
        # Exemplares perdidos
        # Quem mais perde exemplares?
        # Recomendações de exemplares para a biblioteca
        
        # Livros mais emprestados
        # Livros menos emprestados
        # Quais cursos pegam mais livros emprestados
        pass
