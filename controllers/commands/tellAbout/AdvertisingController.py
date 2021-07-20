# bot
import config.BotWrapper as BotWrapper

bot = BotWrapper.BotWrapper.bot


class AdvertisingController:
    @staticmethod
    def tell(chat_id):
        bot.send_message(
            chat_id,
            '''
🗣Главная функция рекламы - убедить потенциального клиента в необходимости его приобретения. Реклама влияет на спрос, может управлять им. Конечно же, это невероятно важно!
какой может быть реклама?
            ''',
            parse_mode='HTML'
        )

        bot.send_message(
            chat_id,
            '''
🚌<b>Реклама в транспорте</b>
Часто реклама располагается внутри автобусов, метро, маршруток либо в виде наклеек, либо на экранах внутри транспорта.
✅ <b>Преимущества</b>:
        ➕ Широкий охват аудитории
        ➕ Низкая стоимость
        ➕Длительность контакта с рекламным сообщением в течение всей поездки
❌ <b>Недостатки</b>:
        ➖ Нецелевой трафик. Рекламу видят все, включая, по большей части, людей, не относящихся к целевой аудитории
            ''',
            parse_mode='HTML'
        )

        bot.send_message(
            chat_id,
            '''
📱<b>Реклама на сайтах и в соц. сетях</b>\
Социальным сетям за последние годы удалось завоевать огромную аудиторию пользователей сетевого пространства. Самые востребованные и популярные социальные площадки Рунета – Фейсбук, Одноклассники, Вконтакте.
✅ <b>Преимущества</b>:
        ➕ Охват большой аудитории
        ➕ Целевой трафик: Ты можешь самостоятельно выбрать, на каких сайтах, в каких пабликах показывать рекламу, выбирая только подходящие под аудиторию твоего бизнеса
        ➕ Социальная реклама дает возможность приобрести всю необходимую информацию о будущих покупателях и клиентах, то есть, со временем целевая аудитория может меняться и ты сможешь это отслеживать
        ➕ Эффективность такой рекламы уже доказана, растет узнаваемость бренда
❌ <b>Недостатки</b>:
        ➖ Прогноз результата практически невозможен
        ➖ Большие затраты на раскрутку
        ➖ Если твой проект направлен на очень малую специализированную аудиторию, то ее поиск будет производить трудности
            ''',
            parse_mode='HTML'
        )

        bot.send_message(
            chat_id,
            '''
🏙<b>Баннеры в городе</b>
Хорошую рекламу видно издалека. А лучше всего видно баннеры.
✅ <b>Преимущества</b>:
        ➕ Разнообразие размеров и мест. Можно выбрать подходящий размер и расположение баннера
        ➕ Широкий охват аудитории, по улицам гуляют все
        ➕ Долговременность рекламы (чаще всего несколько месяцев или лет)
❌ <b>Недостатки</b>:
        ➖ Мало информации. На баннере не может быть много текста.
        ➖ Нецелевой трафик. Рекламу видят все, включая, по большей части, людей, не относящихся к целевой аудитории
            ''',
            parse_mode='HTML'
        )
