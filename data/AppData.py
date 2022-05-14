import json
from typing import Dict

from data.Data import DATA_PATH
import streamlit as st


class AppData:

    @staticmethod
    def data_get(key: str) -> Dict:
        data = AppData.__data()

        if '.' in key:
            keys = key.split('.')

            for k in keys:
                data = data[k]

        return data

    @staticmethod
    @st.cache
    def __data() -> Dict:
        return json.load(open(DATA_PATH))
