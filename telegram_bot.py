from telegram.ext import *
from currency import Currency

API_KEY = '1932174668:AAFGKPlBaPiXJDadfJB7i8xJIobDpmDNh-8'


class TelegramBot():
    def __init__(self):
        updater = Updater(API_KEY)
        d = updater.dispatcher
        d.add_handler(MessageHandler(Filters.text, self.handle_messages))
        updater.start_polling()
        updater.idle()

    def handle_messages(self, update, context):
        text = str(update.message.text)
        response = self.sample_responses(text)
        update.message.reply_text(response, parse_mode="html")

    def sample_responses(self, user_input):
        input_text = str(user_input).lower()
        return Currency().get_currency()


if __name__ == '__main__':
    TelegramBot()