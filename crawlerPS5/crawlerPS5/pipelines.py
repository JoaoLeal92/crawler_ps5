# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import telegram_send
import os


class Crawlerps5Pipeline:

    def open_spider(self, spider):
        with open(os.path.abspath('../iter_number.txt'), 'r') as f:
            self.iter_number = int(f.read())

    def close_spider(self, spider):
        with open(os.path.abspath('../iter_number.txt'), 'w') as f:
            next_iter = self.iter_number + 1
            f.write(str(next_iter))

    def process_item(self, item, spider):
        if item['price']:
            telegram_send.send(messages=[f"Produto {item['name']} encontrado por {item['price']}"])
        else:
            # Checks if bot has run for 24h
            iter_div_result = self.iter_number % 1440
            if iter_div_result == 0:
                telegram_send.send(messages=["Bot ativo por 24h, produto ainda não encontrado"])

        if not item['name']:
            telegram_send.send(messages=["Ocorreu um erro ao buscar o produto, verificar no site"])
