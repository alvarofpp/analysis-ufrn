from odufrn_downloader import ODUFRNDownloader


ufrn_data = ODUFRNDownloader()
# packages = ['matriculas-componentes', 'turmas', 'docentes', 'cursos-ufrn']
packages = ['matriculas-componentes', 'cursos-ufrn']

ufrn_data.download_packages(packages, 'data')
