from telebot import types


class Keyboards:
    @staticmethod
    def get_business_area_keyboard():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            'О сфере услуг💈',
            'О сфере товаров📦'
        )
        return markup

    @staticmethod
    def get_return_keyboard():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            'Вернуться'
        )
        return markup
