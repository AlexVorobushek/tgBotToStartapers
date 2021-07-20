import telebot

from tgBotToStartapers.router import text_messages_router, start_router_commands
import tgBotToStartapers.config.BotWrapper as BotWrapper

# decorators
from tgBotToStartapers.decorators.catch_exepts import catch_excepts

bot = BotWrapper.BotWrapper.bot


start_router_commands()


@catch_excepts
@bot.message_handler(content_types=['text'])
def main(message: telebot.types.Message):
    text_messages_router(
        message.chat.id,
        message.text,
    )


bot.polling(none_stop=True)
