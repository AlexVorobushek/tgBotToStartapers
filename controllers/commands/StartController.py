# bot
from tgBotToStartapers.config.BotWrapper import BotWrapper

bot = BotWrapper.bot


class StartController:
    @staticmethod
    def command_processing(chat_id):
        from tgBotToStartapers.controllers.ChoiceSectorController import ChoiceSectorController

        sti = open('images/hello_sticker.png', 'rb')
        bot.send_sticker(chat_id, sti)
        bot.send_message(
            chat_id,
            '''
<b>Воу! Привет!</b>👋 Мне кажется, ты заглянул сюда не случайно😉 Как ты уже наверняка знаешь, я служу для того, чтобы помочь тебе решить проблемы, связанные с начинанием нового бизнеса📈💸 Я могу рассказать тебе о той или иной "механике" стартапа, тебе следует лишь сказать, какой😋 Надеюсь, я смогу тебе помочь и твой стартап вырастет в огромный бизнес!📊

🤔<b>Интересный фактик:</b> Если обычная заработная плата облагается налогом 13%, то у самозанятых налог намного меньше: 4-6%. Так что ты правильно сделал, что встал на путь к бизнесу😎
            ''',
            parse_mode='HTML'
        )
        ChoiceSectorController.ask_a_sector(chat_id)
