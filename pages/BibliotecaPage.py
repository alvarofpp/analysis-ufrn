import streamlit as st
import pandas as pd
from AppJson import AppJson
from .PageView import PageView


class BibliotecaPage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Biblioteca'
        self.app_data = AppJson.get_data_by_key('acervo-biblioteca')

    def template(self):
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

        As análises estão divididas em duas seções:
        - Acervo
        - Empréstimos
        """, unsafe_allow_html=True)

    def section_01(self):
        st.markdown("""
        # Acervo
        Aqui consta as análises acerca do acervo das bibliotecas da UFRN.
        
        ## Qual biblioteca possui o maior acervo?
        Para responder essa pergunta, iremos realizar um processo simples de contagem dos exemplares nas bibliotecas.
        """)
        qeb = pd.DataFrame(self.app_data['charts']['quantidade_exemplares_por_biblioteca'].items(),
                           columns=['Biblioteca', 'Quantidade de Exemplares'])

        # Gráfico com a quantidade de exemplares por biblioteca
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

        # Top 5
        st.write('Top 5 bibliotecas com maior quantidade de exemplares:')
        table_qeb = qeb.sort_values('Quantidade de Exemplares', ascending=False)[:5].reset_index()
        table_qeb.index = table_qeb.index + 1
        table_qeb.drop(columns=['index'], inplace=True)
        st.table(table_qeb)

        # Livros mais emprestados
        # Livros menos emprestados

    def section_02(self):
        # st.bar_chart
        st.markdown("""
        # Acervo
        
        ## Quais são os livros mais e menos emprestados?
        
        """)
        pass
