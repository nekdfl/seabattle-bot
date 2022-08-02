import os.path

import telebot
from dotenv import load_dotenv

dotenv_path = "bot.env"

if not os.path.exists(dotenv_path):
    raise RuntimeError(f"{dotenv_path} with secret not exists!")

load_dotenv(dotenv_path)
BOT_SECRET = os.environ.get("BOT_SECRET")
if not BOT_SECRET:
    raise RuntimeError(f"You have to declare BOT_SECRET in {dotenv_path} with telegram api token!")


def main():

    bot = telebot.TeleBot(BOT_SECRET, parse_mode=None)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        # bot.reply_to(message, message.text)
        bot.send_message(message.chat.id, text=message.text)

    bot.infinity_polling()


if __name__ == '__main__':
    main()
