from keyboard import Keyboards

# bot
import config.BotWrapper as BotWrapper

bot = BotWrapper.BotWrapper.bot


class ServiceSectorController:
    @staticmethod
    def send_all_services_sector_questions(chat_id):
        bot.send_message(
            chat_id,
            '''
Хмм.. что у нас по сферам услуг📖🧐
Что именно тебя интересует?
/tell_about_rent - 🔑Аренда места, помещения, юридическая часть
/tell_about_services_law - ⚖Законодательные тонкости, расчет и выплата налогов
/tell_about_attraction_employees - 🧑🏻‍💻Привлечение сотрудников, как правильно это делать
/tell_about_advertising - 🗣Реклама, расположить к себе аудиторию
/tell_about_services_investors - 💰Инвесторы и бизнес ангелы. кто такие и как воспользоваться
/tell_about_purchase_equipment - 📽Закупка оборудования, связь с поставщиками
/tell_about_receiving_terminal - 💳Получение терминала и для чего это нужно
/tell_about_services_plan_development - 📈Разработка бизнес плана. зачем и как это делать
            ''',
            reply_markup=Keyboards.get_return_keyboard()
        )
