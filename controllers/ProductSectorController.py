from keyboard import Keyboards

# bot
import config.BotWrapper as BotWrapper

bot = BotWrapper.BotWrapper.bot


class ProductSectorController:
    @staticmethod
    def send_all_services_sector_questions(chat_id):
        bot.send_message(
            chat_id,
            '''
Хмм.. что у нас по создания собственного товара📖🧐
Что именно тебя интересует?
/tell_about_products_law - ⚖Законодательные тонкости, расчет и выплата налогов
/tell_about_advertising - 🗣Реклама, расположить к себе аудиторию
/tell_about_products_investors - 💰Инвесторы и бизнес ангелы. кто такие и как воспользоваться
/tell_about_purchase_equipment - 📦Доставка товара, связь с поставщиками
/tell_about_patents - 💡Патенты, как регестрировать, где искать существующие
/tell_about_product_plan_development - 📈Разработка бизнес плана. зачем и как это делать
            ''',
            reply_markup=Keyboards.get_return_keyboard()
        )
