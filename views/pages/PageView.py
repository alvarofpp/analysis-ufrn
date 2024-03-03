import abc

import streamlit as st


class PageView(abc.ABC):

    def __init__(self):
        self.title = ''

    def render(self):
        st.title(self.title.upper())
        self.horizontal_rule()
        self.intro()
        for section in self.__get_sections():
            getattr(self, section)()

    @abc.abstractmethod
    def intro(self):
        raise NotImplementedError('You must implement the "intro" method.')

    def horizontal_rule(self):
        st.markdown('----------')

    def __get_sections(self):
        return sorted([
            directory for directory in self.__dir__()
            if directory.startswith('section_')
        ])
