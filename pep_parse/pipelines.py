import csv
import datetime as dt
import logging

from scrapy.exceptions import DropItem

from .settings import DATETIME_FORMAT, BASE_DIR, RESULTS


class PepParsePipeline:

    def open_spider(self, spider):
        self.results_vocabulary = {}

    def process_item(self, item, spider):
        try:
            status = item['status']
            self.results_vocabulary[
                status
            ] = self.results_vocabulary.get(status, 0) + 1
        except DropItem:
            numb = item['number']
            logging.error(f'PEP {numb} не содержит статуса')
        finally:
            return item

    def close_spider(self, spider):
        now_time = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = BASE_DIR / RESULTS / f"status_summary_{now_time}.csv"
        with open(file_name, encoding="utf-8", mode="w") as file:
            writer = csv.writer(file, dialect="unix")
            writer.writerows(
                (
                    ("Статус", "Колличество"),
                    *self.results_vocabulary.items(),
                    ("Total", sum(self.results_vocabulary.values()))
                )
            )
