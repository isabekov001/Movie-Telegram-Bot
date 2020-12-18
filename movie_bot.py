import telebot
from telebot import types

bot = telebot.TeleBot('1460821270:AAGs-X7Y4DKvHRN-hE3QN9TnhuRM0IOtpPw')

@bot.message_handler(commands=['website'])
def open_website(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://kinogo-net.org/v8/"))
	bot.send_message(message.chat.id,
			"Нажмите на кнопку ниже и начинай смотреть фильмы прямо сейчас",
			parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    sti = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Жанры')
    btn2 = types.KeyboardButton('Связь с разработчиком')
    markup.add(btn1, btn2)
    send_mess = f"<b>Привет {message.from_user.first_name}</b>!\nЧтобы смотреть фильмы бесплатно и в хорошем качестве нажми на кнопку ниже или напиши мне жанр фильма"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    if message.chat.type == 'private':  
        if message.text == 'Жанры':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Боевики')
            item2 = types.KeyboardButton('Детективы')
            item3 = types.KeyboardButton('Фантастика')
            item4 = types.KeyboardButton('Мультфильмы')
            item5 = types.KeyboardButton('Мелодрамы')
            item6 = types.KeyboardButton('Комедии')
            markup.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(message.chat.id, 'Выберите жанры', reply_markup=markup)
        elif message.text == 'Боевики':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            url_btn1 = types.InlineKeyboardButton(text="Звёздный путь: Дискавери", url="https://kinogo-net.org/v8/1861-zvezdnyy-put-diskaveri-2017.html")
            url_btn2 = types.InlineKeyboardButton(text="S. W. A. T.: Спецназ города ангелов", url="https://kinogo-net.org/v8/4337-s-w-a-t-specnaz-goroda-angelov-2017.html")
            url_btn3 = types.InlineKeyboardButton(text="Неудержимые 3", url="https://kinogo-net.org/v8/5118-neuderzhimye-3-2014.html")
            keyboard.add(url_btn1, url_btn2, url_btn3)
            bot.send_message(message.chat.id, "Боевики", reply_markup=keyboard)
        elif message.text == 'Детективы':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            url_btn1 = types.InlineKeyboardButton(text="Бортпроводница", url="https://kinogo-net.org/v8/4599-bortprovodnica-2020.html")
            url_btn2 = types.InlineKeyboardButton(text="Правда или действие", url="https://kinogo-net.org/v8/5130-pravda-ili-deystvie-2017.html")
            url_btn3 = types.InlineKeyboardButton(text="Волк", url="https://kinogo-net.org/v8/4942-volk-2020.html")
            keyboard.add(url_btn1, url_btn2, url_btn3)
            bot.send_message(message.chat.id, "Детективы", reply_markup=keyboard)
        elif message.text == 'Фантастика':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            url_btn1 = types.InlineKeyboardButton(text="Некст", url="https://kinogo-net.org/v8/2923-nekst-2020.html")
            url_btn2 = types.InlineKeyboardButton(text="Пространство", url="https://kinogo-net.org/v8/2922-prostranstvo-2015.html")
            url_btn3 = types.InlineKeyboardButton(text="Противостояние", url="https://kinogo-net.org/v8/3385-protivostoyanie-2020.html")
            keyboard.add(url_btn1, url_btn2, url_btn3)
            bot.send_message(message.chat.id, "Фантастика", reply_markup=keyboard)
        elif message.text == 'Мультфильмы':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            url_btn1 = types.InlineKeyboardButton(text="Хильда", url="https://kinogo-net.org/v8/5112-hilda-2018.html")
            url_btn2 = types.InlineKeyboardButton(text="Мадагаскар: Маленькие и дикие", url="https://kinogo-net.org/v8/5104-madagaskar-malenkie-i-dikie-2020.html")
            url_btn3 = types.InlineKeyboardButton(text="Гриффины", url="https://kinogo-net.org/v8/2575-griffiny-1999.html")
            keyboard.add(url_btn1, url_btn2, url_btn3)
            bot.send_message(message.chat.id, "Мультфильмы", reply_markup=keyboard)
        elif message.text == 'Мелодрамы':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            url_btn1 = types.InlineKeyboardButton(text="Птица в клетке", url="https://kinogo-net.org/v8/5076-ptica-v-kletke-2020.html")
            url_btn2 = types.InlineKeyboardButton(text="Четыре Рождества", url="https://kinogo-net.org/v8/4927-chetyre-rozhdestva-2008.html")
            url_btn3 = types.InlineKeyboardButton(text="Фабрика грёз", url="https://kinogo-net.org/v8/4696-fabrika-grez-2019.html")
            keyboard.add(url_btn1, url_btn2, url_btn3)
            bot.send_message(message.chat.id, "Мелодрамы", reply_markup=keyboard)
        elif message.text == 'Комедии':
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            url_btn1 = types.InlineKeyboardButton(text="Корпоратив", url="https://kinogo-net.org/v8/5129-korporativ-2014.html")
            url_btn2 = types.InlineKeyboardButton(text="Гранд", url="https://kinogo-net.org/v8/3257-grand-2018.html")
            url_btn3 = types.InlineKeyboardButton(text="Идеальная семья", url="https://kinogo-net.org/v8/4863-idealnaya-semya-2020-s.html")
            keyboard.add(url_btn1, url_btn2, url_btn3)
            bot.send_message(message.chat.id, "Комедии", reply_markup=keyboard)

        elif message.text == 'Связь с разработчиком':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Связь с разработчиком", url="https://github.com/isabekov001"))
            bot.send_message(message.chat.id, "Мой GitHub", parse_mode="html", reply_markup=markup)
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Боевики')
            item2 = types.KeyboardButton('Детективы')
            item3 = types.KeyboardButton('Фантастика')
            item4 = types.KeyboardButton('Мультфильмы')
            item5 = types.KeyboardButton('Мелодрамы')
            item6 = types.KeyboardButton('Комедии')
            markup.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(message.chat.id, 'Выберите жанры', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить...')

bot.polling(none_stop=True)