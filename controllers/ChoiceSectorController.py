from tgBotToStartapers.keyboard import Keyboards
from tgBotToStartapers.config.BotWrapper import BotWrapper

bot = BotWrapper.bot


class ChoiceSectorController:
    @staticmethod
    def ask_a_sector(chat_id):
        bot.send_message(
            chat_id,
            'О какой сфере ты хочешь узнать чуть больше?',
            reply_markup=Keyboards.get_business_area_keyboard()
        )
