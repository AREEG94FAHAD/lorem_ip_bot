import telebot
from telebot import types
import json
from helper import choose_lang, no_words, send_type, get_random_string
import os

APITOKENTLOREM = os.environ.get('APITOKENTLOREM')
bot = telebot.TeleBot(APITOKENTLOREM)

details = {}
details['lang'] = ''
details['no_of_words'] = ''


@bot.message_handler(commands=['start'])
def send_welcome(message):
    details['lang'] = ''
    details['no_of_words'] = ''

    msg = bot.send_message(
        message.chat.id, "Select the Language", reply_markup=choose_lang())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    langs = ['en', 'ar', 'kr']
    words = ['10', '50', '100', '250', '350', '500']
    sendas = ['file', 'text']

    try:
        if call.data in langs:

            details['lang'] = call.data
            bot.send_message(call.from_user.id,
                             "Select the number of words", reply_markup=no_words())

        if call.data in words and details['lang'] != '':
            details['no_of_words'] = int(call.data)
            bot.send_message(call.from_user.id, "send it as",
                             reply_markup=send_type())

        elif call.data in words and details['lang'] == '':

            bot.send_message(call.from_user.id, "Select the Language",
                             reply_markup=choose_lang())

        elif call.data in sendas and details['lang'] != '' and details['no_of_words'] != '':

            lorem_file = open('lorem_'+details['lang']+'.json',)
            lorem_text = json.load(lorem_file)
            lorem_arr = lorem_text['text'].split(' ', 500)

            text = [lorem_arr[i] for i in range(int(details['no_of_words']))]

            jointext = ' '.join(text)
            lorem_file.close()

            if call.data == 'text' and details['lang'] != '' and details['no_of_words'] != '':

                bot.send_message(call.from_user.id, jointext)
                details['lang'] = ''
                details['no_of_words'] = ''

            elif call.data == 'file' and details['lang'] != '' and details['no_of_words'] != '':

                filename = get_random_string(8)

                with open(filename+".txt", 'w') as writelorem:
                    for i in jointext:
                        writelorem.write(i)

                sendingFile = open(filename+".txt", 'r')
                bot.send_document(call.from_user.id, sendingFile)
                sendingFile.close()

                os.remove(filename+".txt")

                details['lang'] = ''
                details['no_of_words'] = ''

        elif call.data in sendas or (details['lang'] == '' and details['no_of_words'] == ''):
            bot.send_message(call.from_user.id,
                             "Select the Language", reply_markup=choose_lang())
    except:
        bot.send_message(call.from_user.id, 'Something went wrong !')


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Select the Language",
                     reply_markup=choose_lang())


bot.polling()
