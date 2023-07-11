import csv
import datetime as dt

from constants import BASE_DIR, DATETIME_FORMAT, TABLE


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_sum = {}
        self.total_peps = 0
        self.results = TABLE

    def process_item(self, item, spider):
        self.total_peps += 1
        status = item['status']
        self.status_sum[status] = self.status_sum.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.utcnow().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now}.csv'
        file_path = results_dir / file_name

        self.results.extend((status, self.status_sum[status])
                            for status in self.status_sum)
        self.results.append(('Total', self.total_peps))

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(self.results)
