# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import telegram_send
from datetime import datetime


class Crawlerps5Pipeline:

    def process_item(self, item, spider):
        if item['price']:
            telegram_send.send(messages=[f"Produto {item['name']} encontrado por {item['price']}"])
        else:
            current_date = datetime.now()
            current_hour = current_date.hour
            current_minute = current_date.minute

            # Checks if bot has run for 24h (every 7 am)
            if current_hour == 7 and current_minute <= 2:
                telegram_send.send(messages=["Bot ativo por 24h, produto ainda não encontrado"])

        if not item['name']:
            telegram_send.send(messages=["Ocorreu um erro ao buscar o produto, verificar no site"])
