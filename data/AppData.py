import json
from typing import Dict

import streamlit as st
from data import Data


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
        return json.load(open(Data.PATH))
