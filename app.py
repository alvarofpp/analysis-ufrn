import streamlit as st
import pages

PAGES = {
    "Início": pages.InicioPage(),
    "Biblioteca": pages.BibliotecaPage(),
    #"Cursos": pages.CursoPage(),
    "Professores": pages.ProfessorPage(),
}


def main():
    st.sidebar.title("Menu de Navegação")
    selection = st.sidebar.radio("Ir para", list(PAGES.keys()))
    page = PAGES[selection]

    with st.spinner(f"Carregando {selection} ..."):
        page.render()


if __name__ == "__main__":
    main()
