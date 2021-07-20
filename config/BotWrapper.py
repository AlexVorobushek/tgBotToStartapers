import config.config as config
import telebot


class BotWrapper:
    bot = telebot.TeleBot(config.TOKEN)
