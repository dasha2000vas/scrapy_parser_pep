from pathlib import Path

SPIDER_NAME = 'pep'
ALLOWED_DOMAIN = ['peps.python.org']
START_URL = ['https://peps.python.org/']

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

BASE_DIR = Path(__file__).parents[1] / 'results'

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
