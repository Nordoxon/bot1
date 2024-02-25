import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem
import datetime
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)
def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

current_date = datetime.date.today().isoformat()
planet_dict = {'mars': ephem.Mars(current_date), 'venus': ephem.Venus(current_date), 'saturn': ephem.Saturn(current_date), 'jupiter': ephem.Jupiter(current_date),
               'neptune': ephem.Neptune(current_date), 'uranus': ephem.Uranus(current_date), 'mercury': ephem.Mercury(current_date), 'pluto': ephem.Pluto(current_date)}

def planet_ephem(update, context):
    user_text_lower = update.message.text.lower()
    user_text_splitted = user_text_lower.split()
    user_text_sliced = user_text_splitted[1:]
    for item_user_text_sliced in user_text_sliced:
        if item_user_text_sliced in planet_dict:
            planet_output = item_user_text_sliced
            planet_name = planet_dict.get(item_user_text_sliced)
            const = ephem.constellation(planet_name)
            update.message.reply_text(f"{planet_output} : {const}")
        else:
            update.message.reply_text('Название планеты отсутствует. Введите название реальной планеты на английском с помощью команды /planet "название планеты"')




def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
def main():
    mybot = Updater(settings.API_KEY)


    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_ephem))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()