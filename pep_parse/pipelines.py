from datetime import datetime

from pep_parse.settings import DATETIME_FORMAT, BASE_DIR

status_count = {
    'Active': 0,
    'Accepted': 0,
    'Deferred': 0,
    'Draft': 0,
    'Final': 0,
    'Provisional': 0,
    'Rejected': 0,
    'Superseded': 0,
    'Withdrawn': 0,
    'Total': 0
}


class PepParsePipeline:
    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        try:
            status_count[item['status']] += 1
        except KeyError:
            pass
        status_count['Total'] += 1
        return item

    def close_spider(self, spider):
        date = datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{date}.csv'
        file_path = BASE_DIR / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in status_count.items():
                f.write(f'{status},{count}\n')
