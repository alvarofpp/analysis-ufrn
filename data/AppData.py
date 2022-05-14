import json
from typing import Dict

import streamlit as st


class AppData:

    @staticmethod
    def save(data: Dict) -> None:
        with open('data/app_data.json', 'w') as outfile:
            json.dump(data, outfile, indent=2, sort_keys=True)

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
        return json.load(open('data/app_data.json'))
