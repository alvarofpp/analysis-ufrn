import json
from typing import Dict

import streamlit as st

from data.Data import DATA_PATH


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
    @st.cache_data
    def __data() -> Dict:
        data = None
        with open(DATA_PATH) as file_data:
            data = json.load(file_data)
        return data
