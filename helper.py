# def choose_lang, choose_type, choose_NOwords
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import string
import random

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def choose_lang():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("English", callback_data="en"),
               InlineKeyboardButton("عربي", callback_data="ar"),
               InlineKeyboardButton("كوردى", callback_data="kr"))
    return markup


def no_words():
    # num_of_words=[10, 50, 100,250, 350, 500]
    markup = InlineKeyboardMarkup()
    markup.row_width = 4
    markup.add(InlineKeyboardButton("10", callback_data="10"),
               InlineKeyboardButton("50", callback_data="50"),
               InlineKeyboardButton("100", callback_data="100"),
               InlineKeyboardButton("250", callback_data="250"),
               InlineKeyboardButton("350", callback_data="350"),
               InlineKeyboardButton("500", callback_data="500"))

    return markup


def send_type():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("file", callback_data="file"),
               InlineKeyboardButton("Text message", callback_data="text"))
    return markup
