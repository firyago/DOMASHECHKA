import config
import telebot
import utils
from telebot import types

lib = dict()

url = {'Ужасы':'https://knigopoisk.org/ratings/luchshie_knigi_uzhasov',
       'Антиутопия':'https://knigopoisk.org/ratings/knigi_antiutopiya',
       'Реализм':'https://knigopoisk.org/ratings/knigi_realizm',
       'Фантастика':'https://knigopoisk.org/ratings/knigi_fantastika_luchshee',
       'Детективы':'https://knigopoisk.org/ratings/knigi_detektivy',
       'Сказки/притчи':'https://knigopoisk.org/ratings/knigi_skazki',
       'Новеллы':'https://knigopoisk.org/ratings/knigi_novella',
       'Исторические романы':'https://knigopoisk.org/ratings/knigi_istoricheskie_romany' }

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands = ['start'])
def Hello(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Топ книг по жанрам')
    markup.row('Поиск')
    bot.send_message(message.chat.id,'Выбирайте: ', reply_markup=markup)

@bot.message_handler(regexp='Топ книг по жанрам')
def Buttons(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('назад')
    markup.row('Ужасы')
    markup.row('Антиутопия')
    markup.row('Реализм')
    markup.row('Фантастика')
    markup.row('Детективы')
    markup.row('Сказки/притчи')
    markup.row('Новеллы')
    markup.row('Исторические романы')
    bot.send_message(message.chat.id, "Выберите жанр:", reply_markup=markup)


@bot.message_handler(regexp='Ужасы')
def Horror(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(name, callback_data=str(message.chat.id) + ' ' + str(name) + ' ' + 'Ужасы') for name in ['3', '5', '10']])
    bot.send_message(message.chat.id, "Выберите кол-во в топе:", reply_markup=keyboard)


@bot.message_handler(regexp='Антиутопия')
def Antiut(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(name, callback_data=str(message.chat.id) + ' ' + str(name) + ' ' + 'Антиутопия') for name in ['3', '5', '10']])
    bot.send_message(message.chat.id, "Выберите кол-во в топе:", reply_markup=keyboard)


@bot.message_handler(regexp='Реализм')
def Real(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(name, callback_data=str(message.chat.id) + ' ' + str(name) + ' ' + 'Реализм') for name in ['3', '5', '10']])
    bot.send_message(message.chat.id, "Выберите кол-во в топе:", reply_markup=keyboard)


@bot.message_handler(regexp='Фантастика')
def Fantasy(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(name, callback_data=str(message.chat.id) + ' ' + str(name) + ' ' + 'Фантастика') for name in ['3', '5', '10']])
    bot.send_message(message.chat.id, "Выберите кол-во в топе:", reply_markup=keyboard)


@bot.message_handler(regexp='Детективы')
def Detect(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(name, callback_data=str(message.chat.id) + ' ' + str(name) + ' ' + 'Детективы') for name in ['3', '5', '10']])
    bot.send_message(message.chat.id, "Выберите кол-во в топе:", reply_markup=keyboard)


@bot.message_handler(regexp='Сказки/притчи')
def Fairytail(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(name, callback_data=str(message.chat.id) + ' ' + str(name) + ' ' + 'Сказки/притчи') for name in ['3', '5', '10']])
    bot.send_message(message.chat.id, "Выберите кол-во в топе:", reply_markup=keyboard)


@bot.message_handler(regexp='Новеллы')
def Novel(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(name, callback_data=str(message.chat.id) + ' ' + str(name) + ' ' + 'Новеллы') for name in ['3', '5', '10']])
    bot.send_message(message.chat.id, "Выберите кол-во в топе:", reply_markup=keyboard)


@bot.message_handler(regexp='Исторические романы')
def HistRoman(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(name, callback_data=str(message.chat.id) + ' ' + str(name) + ' ' + 'Исторические романы') for name in ['3', '5', '10']])
    bot.send_message(message.chat.id, "Выберите кол-во в топе:", reply_markup=keyboard)


@bot.message_handler(regexp='назад')
def Hello(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Топ книг по жанрам')
    markup.row('Поиск автора по названию книги')
    markup.row('Поиск книг по автору')
    bot.send_message(message.chat.id,'Выбирайте: ', reply_markup=markup)


@bot.message_handler(regexp='Поиск')
def SearchBooksAndAuthors(message):
    bot.send_message(message.chat.id, 'Введите имя и фамилию автора или название книги:', None)
    @bot.message_handler(content_types=["text"])
    def Polling(message):
        global lib
        lib = utils.ReturnLib()
        x = max(utils.FindingOut(utils.CorrectMistakes(message.text, lib)),utils.FindingOut(utils.CorrectMistakesAuth(message.text, lib)))
        if x == 0:
            bot.send_message(message.chat.id, utils.ReturnForBook(message.text), None)
        elif x == 1:
            bot.send_message(message.chat.id, utils.ReturnForAuthor(message.text), None)
        elif x == -1:
            bot.send_message(message.chat.id, 'Ну что это такое??? Я вот ума не приложу. Ты хоть знаешь, кто такой Хан Замай? А "Солнце мертвых" слушал? Да что с тобой разговаривать, иди учись... Антихайп', None)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    global lib
    a = c.data.split(' ')
    f = utils.GetCode(url[a[2]])
    local_authors, local_names = utils.AuthorAndName(f)
    s = utils.MakeTop(local_authors, local_names, a[1])
    bot.send_message(a[0], s, None)



if __name__ == '__main__':
    bot.polling(none_stop=True)



