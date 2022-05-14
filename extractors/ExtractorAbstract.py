import abc


class ExtractorAbstract(abc.ABC):

    @abc.abstractmethod
    def run(self) -> bool:
        raise NotImplementedError('You must implement the "run" method.')
