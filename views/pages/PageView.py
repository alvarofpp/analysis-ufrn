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
        raise NotImplemented('You must implement the "intro" method.')

    def horizontal_rule(self):
        st.markdown('----------')

    def __get_sections(self):
        return sorted([dir for dir in self.__dir__() if dir.startswith('section_')])
