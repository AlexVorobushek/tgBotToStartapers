# bot
from config.BotWrapper import BotWrapper

bot = BotWrapper.bot


class NotRecognizedMessageController:
    @staticmethod
    def SendBotNotUnderstandMessage(chat_id):
        bot.send_message(chat_id, 'Sorry? I don\'t understand you. It\'s not a command.')
