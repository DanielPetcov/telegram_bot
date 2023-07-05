import logging
import emoji

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print('Starting up bot...')

TOKEN = '6369792168:AAEXtJUeSV_uiFYYCfjiWWew2zSneqjAYxk'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Nice to meet you! ' + emoji.emojize(':beating_heart:'))
    await update.message.reply_text('Try to write something, then I will respond with the same message.')








if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    
    print('Polling...')
    app.run_polling()