from extractors import DownloadExtractor


extractors = {
    'download': DownloadExtractor(),
}

# Extração
for key, extractor in extractors.items():
    extractor.run()
