from collections import defaultdict
import csv
from datetime import datetime

from pep_parse.settings import DATETIME_FORMAT, BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.status_count['Total'] = sum(self.status_count.values())
        data = [
            {'Статус': key, 'Количество': value}
            for key, value in self.status_count.items()
        ]
        date = datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{date}.csv'
        file_path = BASE_DIR / file_name
        with open(
            file_path, mode='w', encoding='utf-8', newline=''
        ) as csvfile:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
