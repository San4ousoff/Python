from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)    
    await update.message.reply_text(f'/hi\n/time\n/help')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)    
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

app = ApplicationBuilder().token("5985032540:AAG9mYScW-pA_aqh8hvlGpHerdJfG4L9y2g").build()

app.add_handler(CommandHandler("hi", hi))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("time", time))
print('server start')
app.run_polling()