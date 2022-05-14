from os import path

from odufrn_downloader import ODUFRNDownloader

from .ExtractorAbstract import ExtractorAbstract


class DownloadExtractor(ExtractorAbstract):

    def run(self) -> bool:
        ufrn_data = ODUFRNDownloader()
        packages = [
            'cursos-ufrn',
            'turmas',
            'matriculas-componentes',
            'docentes',
            'discentes',
            'acervo-biblioteca',
            'emprestimos-acervos-das-bibliotecas',
            'componentes-curriculares',
        ]

        for package in packages:
            if not path.exists('data/{}'.format(package)):
                ufrn_data.download_package(package, 'data')

        return True
