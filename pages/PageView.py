import abc
import streamlit as st


class PageView(abc.ABC):

    def __init__(self):
        self.title = None

    def render(self):
        st.title(self.title.upper())
        self.horizontal_rule()
        self.template()

    @abc.abstractmethod
    def template(self):
        raise NotImplemented('You must implement the "template" method.')

    def horizontal_rule(self):
        st.markdown('----------')
