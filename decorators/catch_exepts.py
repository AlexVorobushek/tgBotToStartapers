import config.BotWrapper as BotWrapper

bot = BotWrapper.BotWrapper.bot


def catch_excepts(function):
    def function_with_catch_excepts(message):
        try:
            return function(message)
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, '😭')
            bot.send_message(message.chat.id, 'Прошу прощения, на моем сервере произошла ошибка.')

    return function_with_catch_excepts
