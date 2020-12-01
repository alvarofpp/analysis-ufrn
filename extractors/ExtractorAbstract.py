import abc


class ExtractorAbstract(abc.ABC):

    @abc.abstractmethod
    def run(self) -> bool:
        raise NotImplemented('You must implement the "run" method.')
