from telegram import Update
from telegram.ext import CallbackContext
from datetime import *

def log(update: Update, context: CallbackContext):
    time_log = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    file = open('Bot/db.csv', 'a', encoding='utf=8')
    file.write(f'{time_log}, {update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    # file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()    

