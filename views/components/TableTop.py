import streamlit as st


class TableTop:

    @staticmethod
    def render(data, column: str, top: int):
        table_data = data.sort_values(column, ascending=False)[:top].reset_index()
        table_data.index = table_data.index + 1
        table_data.drop(columns=['index'], inplace=True)
        st.table(table_data)
