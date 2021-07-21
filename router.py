import telebot

# CONTROLLERS
from controllers.ServiceSectorController import ServiceSectorController
from controllers.ProductSectorController import ProductSectorController
from controllers.ChoiceSectorController import ChoiceSectorController
from controllers.NotRecognizedMessageController import NotRecognizedMessageController

# COMMANDS
from controllers.commands.StartController import StartController

# # TELL_ABOUT
from controllers.commands.tellAbout.AdvertisingController import AdvertisingController
from controllers.commands.tellAbout.PatentsController import PatentsController


from config import config

# BOT
from config.BotWrapper import BotWrapper

bot = BotWrapper.bot


def transform_text_to_func(text: str):
    commands = {
        'О сфере услуг💈': Router.get_message_for_services_sector,
        'Вернуться': Router.sector_selection,
        'О сфере товаров📦': Router.get_message_for_product_sector
    }
    if text in commands:
        return commands[text]
    return Router.not_recognized_command


def start_router_commands():
    @bot.message_handler(commands=['start'])
    def start(message: telebot.types.Message):
        bot.send_message(config.admin_chat_id,
                         f'<i><b>for admin</b></i> new_user: {message.chat.id=}, {message.from_user.id=}, {message.from_user.username=}',
                         parse_mode='HTML')
        StartController.command_processing(message.chat.id)

    @bot.message_handler(commands=['tell_about_advertising'])
    def tell_about_advertising(message: telebot.types.Message):
        bot.send_message(config.admin_chat_id,
                         f'<i><b>for admin</b></i> {message.from_user.id=}, tell_about_advertising',
                         parse_mode='HTML'
                         )
        AdvertisingController.tell(message.chat.id)

    @bot.message_handler(commands=['tell_about_patents'])
    def tell_about_patents(message: telebot.types.Message):
        bot.send_message(config.admin_chat_id,
                         f'<i><b>for admin</b></i> {message.from_user.id=}, tell_about_patents',
                         parse_mode='HTML')
        PatentsController.tell(message.chat.id)


def text_messages_router(chat_id, text, user_id):
    transform_text_to_func(text)(
        chat_id=chat_id,
        text=text,
        user_id=user_id
    )


class Router:
    @staticmethod
    def get_message_for_services_sector(**kwargs):
        ServiceSectorController.send_all_services_sector_questions(kwargs['chat_id'])

    @staticmethod
    def get_message_for_product_sector(**kwargs):
        ProductSectorController.send_all_services_sector_questions(kwargs['chat_id'])

    @staticmethod
    def not_recognized_command(**kwargs):
        bot.send_message(config.admin_chat_id,
                         f"<i><b>for admin</b></i> {kwargs['user_id']}, not_recognized_command, {kwargs['text']=}",
                         parse_mode='HTML'
                         )
        NotRecognizedMessageController.SendBotNotUnderstandMessage(kwargs['chat_id'])

    @staticmethod
    def sector_selection(**kwargs):
        ChoiceSectorController.ask_a_sector(kwargs['chat_id'])
