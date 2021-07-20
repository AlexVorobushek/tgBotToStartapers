import telebot
import os

from router import text_messages_router, start_router_commands
import config.BotWrapper as BotWrapper

# decorators
from decorators.catch_exepts import catch_excepts

bot = BotWrapper.BotWrapper.bot
start_router_commands()


def daemon(func):
    def wrapper(*args, **kwargs):
        if os.fork():
            return
        func(*args, **kwargs)
        os._exit(os.EX_OK)
    return wrapper


@daemon
@catch_excepts
@bot.message_handler(content_types=['text'])
def main(message: telebot.types.Message):
    text_messages_router(
        message.chat.id,
        message.text,
    )


bot.polling(none_stop=True)
