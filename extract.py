from extractors import DownloadExtractor

if __name__ == '__main__':
    extractors = {
        'download': DownloadExtractor(),
    }

    for _, extractor in extractors.items():
        extractor.run()
