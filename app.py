import streamlit as st
import pages


@st.cache
def get_page():
    print('CHAMOU get_page')
    return {
        "Início": pages.InicioPage(),
        "Biblioteca": pages.BibliotecaPage(),
        # "Cursos": pages.CursoPage(),
        "Professores": pages.ProfessorPage(),
    }


def main():
    st.sidebar.title("Menu de Navegação")
    selection = st.sidebar.radio("Ir para", list(get_page().keys()))
    page = get_page()[selection]

    with st.spinner(f"Carregando {selection} ..."):
        page.render()

    print('----------')
    print('app')


if __name__ == "__main__":
    main()
