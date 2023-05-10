from pathlib import Path

BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"
ROBOTSTXT_OBEY = True
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'overwrite': True,
        'fields': ['number', 'name', 'status']
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
