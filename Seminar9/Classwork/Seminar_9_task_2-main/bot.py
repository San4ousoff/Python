from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands


app = ApplicationBuilder().token("5722795700:AAEctQ9HNTWEZ9y9cR-NzLXzg6HspH5gov0").build()
print('Сервер запустился')

app.add_handler(CommandHandler("g_1", bot_commands.g_1))


app.run_polling()
