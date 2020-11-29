import streamlit as st


class TableTop:

    @staticmethod
    def render(data, column: str, top: int):
        table_qet = data.sort_values(column, ascending=False)[:top].reset_index()
        table_qet.index = table_qet.index + 1
        table_qet.drop(columns=['index'], inplace=True)
        st.table(table_qet)
