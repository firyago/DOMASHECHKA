import config
import telebot
import utils
from telebot import types

lib = dict()

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def Hello(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Топ книг по жанрам')
    markup.row('Поиск автора по названию книги')
    markup.row('Поиск книг по автору')
    bot.send_message(message.chat.id,'Выбирайте: ', reply_markup=markup)

@bot.message_handler(regexp='Топ книг по жанрам')
def Buttons(message):
    markup = types.ReplyKeyboardMarkup()
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
    bot.send_message(message.chat.id, 'Введите число: сколько лучших книг вы хотите увидеть (от 1 до 100)', None)
    @bot.message_handler(content_types=["text"])
    def Horrorer(message):
        global lib
        f = utils.GetCode('https://knigopoisk.org/ratings/luchshie_knigi_uzhasov')
        local_authors, local_names = utils.AuthorAndName(f)
        s = utils.MakeTop(local_authors, local_names, message.text)
        bot.send_message(message.chat.id, s)
        

@bot.message_handler(regexp='Антиутопия')
def Antiut(message):
    bot.send_message(message.chat.id, 'Введите число: сколько лучших книг вы хотите увидеть (от 1 до 100)', None)
    @bot.message_handler(content_types=["text"])
    def Antiutopier(message):
        global lib
        f = utils.GetCode('https://knigopoisk.org/ratings/knigi_antiutopiya')
        local_authors, local_names = utils.AuthorAndName(f)
        s = utils.MakeTop(local_authors, local_names, message.text)
        bot.send_message(message.chat.id, s, None)

@bot.message_handler(regexp='Реализм')
def Real(message):
    bot.send_message(message.chat.id, 'Введите число: сколько лучших книг вы хотите увидеть (от 1 до 100)', None)
    @bot.message_handler(content_types=["text"])
    def Realer(message):
        global lib
        f = utils.GetCode('https://knigopoisk.org/ratings/knigi_realizm')
        local_authors, local_names = utils.AuthorAndName(f)
        s = utils.MakeTop(local_authors, local_names, message.text)
        bot.send_message(message.chat.id, s, None)

@bot.message_handler(regexp='Фантастика')
def Fantasy(message):
    bot.send_message(message.chat.id, 'Введите число: сколько лучших книг вы хотите увидеть (от 1 до 100)', None)
    @bot.message_handler(content_types=["text"])
    def Fantesier(message):
        global lib
        f = utils.GetCode('https://knigopoisk.org/ratings/knigi_fantastika_luchshee')
        local_authors, local_names = utils.AuthorAndName(f)
        s = utils.MakeTop(local_authors, local_names, message.text)
        bot.send_message(message.chat.id, s, None)

@bot.message_handler(regexp='Детективы')
def Detect(message):
    bot.send_message(message.chat.id, 'Введите число: сколько лучших книг вы хотите увидеть (от 1 до 100)', None)
    @bot.message_handler(content_types=["text"])
    def Detecter(message):
        global lib
        f = utils.GetCode('https://knigopoisk.org/ratings/knigi_detektivy')
        local_authors, local_names = utils.AuthorAndName(f)
        s = utils.MakeTop(local_authors, local_names, message.text)
        bot.send_message(message.chat.id, s, None)

@bot.message_handler(regexp='Сказки/притчи')
def Fairytail(message):
    bot.send_message(message.chat.id, 'Введите число: сколько лучших книг вы хотите увидеть (от 1 до 100)', None)
    @bot.message_handler(content_types=["text"])
    def Fairytailer(message):
        global lib
        f = utils.GetCode('https://knigopoisk.org/ratings/knigi_skazki')
        local_authors, local_names = utils.AuthorAndName(f)
        s = utils.MakeTop(local_authors, local_names, message.text)
        bot.send_message(message.chat.id, s, None)

@bot.message_handler(regexp='Новеллы')
def Novel(message):
    bot.send_message(message.chat.id, 'Введите число: сколько лучших книг вы хотите увидеть (от 1 до 100)', None)
    @bot.message_handler(content_types=["text"])
    def Noveler(message):
        global lib
        f = utils.GetCode('https://knigopoisk.org/ratings/knigi_novella')
        local_authors, local_names = utils.AuthorAndName(f)
        s = utils.MakeTop(local_authors, local_names, message.text)
        bot.send_message(message.chat.id, s, None)

@bot.message_handler(regexp='Исторические романы')
def HistRoman(message):
    bot.send_message(message.chat.id, 'Введите число: сколько лучших книг вы хотите увидеть (от 1 до 100)', None)
    @bot.message_handler(content_types=["text"])
    def Romaner(message):
        global lib
        f = utils.GetCode('https://knigopoisk.org/ratings/knigi_istoricheskie_romany')
        local_authors, local_names = utils.AuthorAndName(f)
        s = utils.MakeTop(local_authors, local_names, message.text)
        bot.send_message(message.chat.id, s, None)

@bot.message_handler(regexp='Поиск автора по названию книги')
def SearchAuthor(message):
    bot.send_message(message.chat.id, 'Введите название книги:', None)
    @bot.message_handler(content_types=["text"])
    def Polling(message):
        global lib
        lib = utils.ReturnLib()
        s = utils.CorrectMistakes(message.text, lib)
        if s == message.text:
            if s in lib.keys():
                bot.send_message(message.chat.id, lib[s], None)
            else:
                bot.send_message(message.chat.id, 'К сожалению, не знаю такой книги. Антихайп.' , None)
        else:
            if s in lib.keys():
                bot.send_message(message.chat.id,'Вы ошиблись: ' + s + '\n' + lib[s], None)
            else:
                bot.send_message(message.chat.id, 'К сожалению, не знаю такой книги. Антихайп.' , None)

@bot.message_handler(regexp='Поиск книг по автору')
def SearchBooks(message):
    bot.send_message(message.chat.id, 'Введите имя и фамилию автора:', None)
    @bot.message_handler(content_types=["text"])
    def Molodec(message):
        global lib
        lib = utils.ReturnLib()
        s = utils.CorrectMistakesAuth(message.text, lib)
        out = ''
        if s in lib.values():
            for x in lib.keys():
                if lib[x] == s:
                    out += x + '\n'
        if out != '':
            if s == message.text:
                bot.send_message(message.chat.id, out, None)
            else:
                bot.send_message(message.chat.id, 'Вы ошиблись, его/ее зовут ' + s + '\n' + out, None)
        else:
            bot.send_message(message.chat.id, 'Кто это? Он из антихайпа вообще?', None)



if __name__ == '__main__':
    bot.polling(none_stop=True)


