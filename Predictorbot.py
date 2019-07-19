from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup




############# Telegram Bot Part ##################################
# Boturl = "https://api.telegram.org/bot634641815:AAFLp9QVqfPFbM32EFcoVpr4K70xk2JnzR0/getme"
token = "634641815:AAFLp9QVqfPFbM32EFcoVpr4K70xk2JnzR0"

#check for new message



#allows to register handler --> all media

#

flag = False

#define a command call back function
def start(bot, update):
    bot.sned_message(chat_id=update.message.chat_id, text="سلام دوست عزیز به بات پیش بینی قیمت خودرو و خانه خوش آمدید :) کدومو برات پیش بینی کنم ؟؟ /car یا /home ؟")


    return

#car handler
def car(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="لطفا نام شهر خود را به فارسی وارد کنید")
    flag = True
    if flag:
        print(update.message.text)
        flag = False
    #TODO: Enter details of car
    return





# #Home Handler
#


def home(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='لطفا مشخصات خانه خود را به ترتیب و با یک فاصله وارد کنید مکان خواب متراژ')
    bot.send_message(chat_id=update.message.chat_id, text="لطفا مکان خود را به فارسی وارد کنید")
    if update.message.text == "لطفا مکان خود را به فارسی وارد کنید":
        location = recieve_location(bot, update)
        print('location is %s' % location)
    bot.send_message(chat_id=update.message.chat_id, text="لطفا تعداد خواب را به فارسی وارد کنید")
    if update.message.text == "لطفا تعداد خواب را به فارسی وارد کنید":
        rooms = recieve_rooms(bot, update)
        print('rooms are %s' % rooms)
    bot.send_message(chat_id=update.message.chat_id, text="لطفا متراژ خانه را وارد کنید")
    if update.message.text == "لطفا متراژ خانه را وارد کنید":
        meterix = recieve_meterix(bot, update)
        print('meterix is %s' % meterix)

#
def recieve_location(bot, update):

    home_location = update.message.text
    # bot.send_message(chat_id=update.message.chat_id, text=('your location is %s') % (home_location))
    return home_location


def recieve_rooms(bot, update):

    home_rooms = update.message.text
    # bot.send_message(chat_id=update.message.chat_id, text=('number of your rooms are/is  %s') % (home_rooms))
    return home_rooms



def recieve_meterix(bot, update):

    home_meterix = update.message.text
    # bot.send_message(chat_id=update.message.chat_id, text=('meterix is %s') % (home_meterix))
    return home_meterix





#
#
# def onmessage(bot, update):
#     if update.message.text:
#         print(update.message.text)
#         if update.message.text == '/start':
#             bot.send_message(chat_id=update.message.chat_id, text='جیو میخوای برات پیش  بینی کنم؟؟')
#             print(update.message.text)
#         elif update.message.text == '/car':
#             bot.send_message(chat_id=update.message.chat_id, text='لطفا مدل ماشینتو وارد کن')
#             model = update.message.text
#             print(model)
#
#         elif update.message.text == '/home':
#             bot.send_message(chat_id=update.message.chat_id, text='home')
#             model = update.message.text
#             print(model)
#
#         else:
#             bot.send_message.text("wrong command")
# onmessage_handler = MessageHandler(Filters.text, onmessage)
# dispatcher.add_handler(onmessage_handler)
#start polling

#

def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("home", home))
    dispatcher.add_handler(CommandHandler("car", car))
    dispatcher.add_handler(MessageHandler(Filters.text, recieve_location))
    dispatcher.add_handler(MessageHandler(Filters.text, recieve_rooms))
    dispatcher.add_handler(MessageHandler(Filters.text, recieve_meterix))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
#TODO:complete the bot interface
