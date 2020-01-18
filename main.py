from telebot import TeleBot
import requests
from telebot import types
import re

bot = TeleBot("1007314497:AAHvjuAFIIN0GpUOevA3HturouG_tyS2hQ0")


@bot.message_handler()
def handle_massage(message):

    result = requests.get(f"http://api.urbandictionary.com/v0/define?term={message.text}").json()
    total = "\n".join(n["definition"] for n in result["list"])
    # bot.send_message(message.chat.id, f'{total}')

    words = re.findall(r"[^[]*\[([^]]*)\]", total)


    markup = types.ReplyKeyboardMarkup()
    listy = []
    for a in words:
        listy.append(types.KeyboardButton(a))

    for a in range(len(listy)):
        if a % 3 == 0:
            try:
                markup.row(listy[a], listy[a + 1], listy[a + 2])
            except IndexError:
                try:
                    markup.row(listy[a], listy[a + 1])
                except IndexError:
                    markup.row(listy[a])
        continue


    bot.send_message(message.chat.id, f"{total} \n Choose one word:", reply_markup=markup)




if __name__=="__main__":
    bot.polling()
