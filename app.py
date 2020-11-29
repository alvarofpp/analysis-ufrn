import streamlit as st
from views import pages


@st.cache
def get_page():
    return {
        "Início": pages.InicioPage(),
        "Biblioteca": pages.BibliotecaPage(),
        # "Cursos": pages.CursoPage(),
    }


def main():
    st.sidebar.title("Menu de Navegação")
    selection = st.sidebar.radio("Ir para", list(get_page().keys()))
    page = get_page()[selection]

    with st.spinner(f"Carregando {selection} ..."):
        page.render()


if __name__ == "__main__":
    main()
