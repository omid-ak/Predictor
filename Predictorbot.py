from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# import telegram
# import requests
# import pprint
# Boturl = "https://api.telegram.org/bot634641815:AAFLp9QVqfPFbM32EFcoVpr4K70xk2JnzR0/getme"
# response = requests.get(Boturl)
# pprint.pprint(response.json())
token = "634641815:AAFLp9QVqfPFbM32EFcoVpr4K70xk2JnzR0"
# Bot = telegram.Bot(token=token)
# print(Bot.get_me())

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



# def sendmsg(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text="سلام دوست عزیز به بات پیش بینی قیمت خودرو و خانه خوش آمدید :)")
#
#
# msg_handler = MessageHandler(Filters.text, sendmsg)
# dispatcher.add_handler(msg_handler)



#create a new command handleer

#start_handler = CommandHandler("start", start)

#add the commadnhandler to dispatcher

#dispatcher.add_handler(start_handler)

#car handler
def car(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="پیش بینی قیمت خودرو")
car_handler = CommandHandler("car", car)
dispatcher.add_handler(car_handler)

# def sendmsg(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text="پیش بینی قیمت خودرو")
#
#
# msg_handler = MessageHandler(Filters.text, sendmsg)
# dispatcher.add_handler(msg_handler)



#Home Handler
def home(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="پیش بینی قیمت خانه")
home_handler = CommandHandler("home", home)
dispatcher.add_handler(home_handler)

# def sendmsg(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text="پیش بینی خونه")
#
#
# msg_handler = MessageHandler(Filters.text, sendmsg)
# dispatcher.add_handler(msg_handler)


# def choose(bot, update):
#     button = [
#         [InlineKeyboardButton("car", callback_data="ماشین")],
#         [InlineKeyboardButton("home", callback_data="خونه")]
#     ]
#     reply_markup = InlineKeyboardMarkup(button)
#
#     bot.send_message(chat_id=update.message.chat_id, text="قیمت کدومو برات پیش بینی کنم :) ؟؟", reply_markup=reply_markup)
# choose_handler = CommandHandler("Choose", choose)
# dispatcher.add_handler(choose_handler)
#
# def button(bot, update):
#     query = update.callback_query
#
#     bot.send_message(chat_id=update.message.chat_id, text="خب ! یرم برای پیش بینی قیمت {}".format(query.data))
#
# button_handler = CallbackQueryHandler(button)
# dispatcher.add_handler(button_handler)



#start polling

updater.start_polling()

