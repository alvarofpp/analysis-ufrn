from extractors import DownloadExtractor


if __name__ == '__main__':
    extractors = {
        'download': DownloadExtractor(),
    }

    # Extração
    for key, extractor in extractors.items():
        extractor.run()
