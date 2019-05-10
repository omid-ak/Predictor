from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import Prediction
import Home
import Car


############### Data Base Part #########################
import mysql.connector

dbconnector = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      password="@Omid1377",
                                      )

my_cursor = dbconnector.cursor()

dbconnector.commit()
dbconnector.close()





############# Telegram Bot Part ##################################
# Boturl = "https://api.telegram.org/bot634641815:AAFLp9QVqfPFbM32EFcoVpr4K70xk2JnzR0/getme"
token = "634641815:AAFLp9QVqfPFbM32EFcoVpr4K70xk2JnzR0"

#check for new message
updater = Updater(token=token)

#allows to register handler --> all media

dispatcher = updater.dispatcher

#define a command call back function
def start(bot, update):
#     bot.sned_message(chat_id=update.message.chat_id, text="سلام دوست عزیز به بات پیش بینی قیمت خودرو و خانه خوش آمدید :)")
# start_handler = CommandHandler("start", start)
# dispatcher.add_handler(start_handler)

    button = [
        [InlineKeyboardButton("car", callback_data="ماشین")],
        [InlineKeyboardButton("home", callback_data="خونه")]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    bot.send_message(chat_id=update.message.chat_id, text="قیمت کدومو برات پیش بینی کنم :) ؟؟", reply_markup=reply_markup)
choose_handler = CommandHandler("start", start)
dispatcher.add_handler(choose_handler)

def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(chat_id=query.message.chat_id, text="خب ! بریم برای پیش بینی قیمت {}".format(query.data),message_id=query.message.message_id)

button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)


#car handler
def car(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="پیش بینی قیمت خودرو")
car_handler = CommandHandler("car", car)
dispatcher.add_handler(car_handler)




#Home Handler
def home(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="پیش بینی قیمت خانه")
home_handler = CommandHandler("home", home)
dispatcher.add_handler(home_handler)




#start polling

updater.start_polling()

