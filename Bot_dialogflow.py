# This is a bot for use on a server with DialogFlow. Very simple so far, but I will definitely update soon
# and add a lot more features.

from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import apiai
import json

TG_TOKEN = '976137769:AAFdHP6xhSyg3PCbDhUVAqoVXeVVNVGWrXg'

def do_start(bot: Bot,update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text= 'Send me anything!',
    )

def do_echo(bot: Bot,update: Update):
    text = update.message.text

    def send_message(message):
        request = apiai.ApiAI('7d6fe8b74eeb4205858b3c9a6314c665').text_request()
        request.lang = 'en'
        request.session_id = 'session_1'
        request.query = message
        response = json.loads(request.getresponse().read().decode('utf-8'))
        my_answer = response['result']['fulfillment']['speech']
        my_answer2 = response['result']['action']
        Answer = [my_answer,my_answer2]
        return Answer

    action = None
    action = send_message(text)
    if action[1] == 'smalltalk.greetings.bye':
        pass
    bot.send_message(chat_id=update.message.chat_id,text= action[0],)


def main():
    print("Start")
    bot = Bot(token=TG_TOKEN,)
    updater = Updater(bot=bot,)

    start_Handler = CommandHandler('start',do_start)
    message_Handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_Handler)
    updater.dispatcher.add_handler(message_Handler)

    updater.start_polling()
    updater.idle()
    print("Finish")
    return updater

if __name__ == '__main__':
    main()


