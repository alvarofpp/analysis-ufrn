import streamlit as st
from views import pages


#@st.cache(allow_output_mutation=True)
def get_page():
    return {
        "Início": pages.InicioPage(),
        "Biblioteca": pages.BibliotecaPage(),
        "Taxa de Aprovação": pages.TaxaDeAprovacaoPage(),
    }


def main():
    st.sidebar.title("Menu de Navegação")
    selection = st.sidebar.radio("Ir para", list(get_page().keys()))
    page = get_page()[selection]

    with st.spinner(f"Carregando {selection} ..."):
        page.render()


if __name__ == "__main__":
    main()
