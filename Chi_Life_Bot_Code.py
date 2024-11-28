
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

# Установите свой токен, который вы получите от BotFather
API_TOKEN = 'YOUR_BOT_API_TOKEN'

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Команда start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я ЧілЛайф-бот. Как я могу помочь вам сегодня?")

# Команда help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Я могу отправить вам полезные советы, мемы и задания. Напишите /meme, чтобы получить мем!")

# Команда meme (для отправки случайного мема)
def send_meme(update: Update, context: CallbackContext) -> None:
    memes = [
        "https://i.pinimg.com/originals/6a/99/6d/6a996d232f3a5f8c7ef47eb632b699f1.jpg",
        "https://i.pinimg.com/originals/77/5f/4f/775f4fbb8b2ac0328282f8cc446fe598.jpg",
        "https://i.pinimg.com/originals/9b/44/d7/9b44d78079887976f2e29d2b003c7f11.jpg"
    ]
    update.message.reply_text(random.choice(memes))

# Команда для дыхательных практик
def breathing_practice(update: Update, context: CallbackContext) -> None:
    breathing_exercises = [
        "Вдохните на 4 счета, задержите дыхание на 4 счета, выдохните на 4 счета. Повторите 3 раза.",
        "Вдохните глубоко через нос, задержите дыхание на 5 секунд, выдохните через рот. Повторите 4 раза."
    ]
    update.message.reply_text(random.choice(breathing_exercises))

# Обработка текстовых сообщений
def text_message(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Напишите /help, чтобы узнать, что я могу сделать!")

# Главная функция для запуска бота
def main():
    # Создаем объект Updater и передаем в него API токен
    updater = Updater(API_TOKEN)

    # Получаем диспетчера для обработки команд
    dispatcher = updater.dispatcher

    # Команды
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("meme", send_meme))
    dispatcher.add_handler(CommandHandler("breathing", breathing_practice))

    # Обработка текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_message))

    # Запуск бота
    updater.start_polling()

    # Бот будет работать до тех пор, пока не будет остановлен
    updater.idle()

if __name__ == '__main__':
    main()
