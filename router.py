# CONTROLLERS
from tgBotToStartapers.controllers.ServiceSectorController import ServiceSectorController
from tgBotToStartapers.controllers.ProductSectorController import ProductSectorController
from tgBotToStartapers.controllers.ChoiceSectorController import ChoiceSectorController
from tgBotToStartapers.controllers.NotRecognizedMessageController import NotRecognizedMessageController

# COMMANDS
from tgBotToStartapers.controllers.commands.StartController import StartController

# # TELL_ABOUT
from tgBotToStartapers.controllers.commands.tellAbout.AdvertisingController import AdvertisingController
from tgBotToStartapers.controllers.commands.tellAbout.PatentsController import PatentsController

# BOT
from tgBotToStartapers.config.BotWrapper import BotWrapper

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
    def start(message):
        StartController.command_processing(message.chat.id)

    @bot.message_handler(commands=['tell_about_advertising'])
    def tell_about_advertising(message):
        AdvertisingController.tell(message.chat.id)

    @bot.message_handler(commands=['tell_about_patents'])
    def tell_about_patents(message):
        PatentsController.tell(message.chat.id)


def text_messages_router(chat_id, text):
    transform_text_to_func(text)(
        chat_id=chat_id,
        text=text,
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
        NotRecognizedMessageController.SendBotNotUnderstandMessage(kwargs['chat_id'])

    @staticmethod
    def sector_selection(**kwargs):
        ChoiceSectorController.ask_a_sector(kwargs['chat_id'])
