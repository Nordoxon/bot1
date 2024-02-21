import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem
import datetime
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)
def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def planet_ephem(update, context):
    user_text = update.message.text
    planet_name = user_text.split()
    current_date = datetime.date.today().isoformat()
    new_planet = ephem.planet_name[2](current_date)
    try:
        update.message.reply_text(new_planet)
    except:
        update.message.reply_text('Введите название реальной планеты на английском с помощью команды /planet "название планеты"')



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