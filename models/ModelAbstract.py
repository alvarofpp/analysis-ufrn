from abc import ABC
from os import listdir
import re

import pandas as pd
import streamlit as st


class ModelAbstract(ABC):

    def __init__(self):
        self.__parent_dir = 'data'
        self.dir = ''
        self.file_pattern = ''
        self._data = None
        self._files = []
        self._extension = '.csv'
        self._sep = ';'

    def __get_dir(self) -> str:
        return '{}/{}/'.format(self.__parent_dir, self.dir)

    def __load_files(self) -> None:
        files_dir = listdir(self.__get_dir())
        files_filter = filter(
            lambda filename: filename.endswith(self._extension),
            filter(
                re.compile(self.file_pattern).search,
                files_dir,
            ),
        )
        self._files = list(files_filter)

    def load(self) -> None:
        self.__load_files()
        dfs = [
            pd.read_csv(
                self.__get_dir() + filename,
                sep=self._sep,
                low_memory=False,
            )
            for filename in self._files
        ]
        self._data = pd.concat(dfs, ignore_index=True)

    @st.cache(persist=True)
    def get_data(self):
        return self._data
