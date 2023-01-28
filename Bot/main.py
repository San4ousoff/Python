# from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *
from bot_commands import *
# import token

app = ApplicationBuilder().token("5722795700:AAEctQ9HNTWEZ9y9cR-NzLXzg6HspH5gov0").build()

app.add_handler(CommandHandler('hi', hi_command))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))

print('"Сервер запущен"')
app.run_polling()