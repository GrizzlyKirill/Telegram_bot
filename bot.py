import telebot as tl
token = '685325034:AAGfsnfoMdwTY9A-pj3VrIb9_1Sc7zttAdM'
bot = tl.TeleBot(token)


@bot.message_handler(commands=['start', 'go'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')


@bot.message_handler(content_types=["text"])
def answer(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == 'привет':
        bot.send_message(chat_id, 'Братан, как дела?')
        print('Привет')
    elif text in 'splash':
        print('Splash')
        bot.send_message(chat_id, 'Твоя сука смотрит на меня! УЙДИ НАХУЙ vcobe ЕБАНЫЙ!\n Это Ванина песня, если что!'
                                  'Подождите немного)')
        bot.send_audio(chat_id, audio=open('files/vcobe - SPLASH.mp3', 'rb'))
        print('Музыка отправленна')


print('connect')
bot.polling()

