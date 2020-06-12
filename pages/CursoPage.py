import json
import streamlit as st
from .PageView import PageView


class CursoPage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Cursos'

        # Dados para os filtros
        self.inputs_data = json.load(open('data.json'))
        self.filters = {
            'nivel_ensino': None,
            'curso': None,
            'materia': None,
            'turma': None,
            'professor': None,
        }

    def template(self):
        # Explicação sobre o trabalho
        st.write("""
        Aqui você pode realizar analises sobre os 
        """)

        # Filtros
        self.filters['nivel_ensino'] = st.selectbox(
            'Selecione o nível de ensino:',
            self.inputs_data['niveis_ensino']
        )

        # Json com os filtros selecionados
        st.write('Filtros selecionados:', {
            'Nível de ensino': self.filters['nivel_ensino'],
            'Curso': self.filters['curso'],
            'Matéria': self.filters['materia'],
            'Turma': self.filters['turma'],
            'Professor': self.filters['professor'],
        })

