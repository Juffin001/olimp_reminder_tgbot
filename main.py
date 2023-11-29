from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from main_parser import phys, inf, math

TOKEN: Final = '6432377248:AAECZuT-fF1KeXKiCTYA2PJiArUH4a2z6kk'
BOT_USERNAME: Final = '@olimp_reminder'


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ок, все будет")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("потом добавлю")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(*inf)

# Responses

def Handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if "test" in processed:
        return "all working well"
    return "я не понял"

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"ошибка {update} {context.error}")


if __name__ == "__main__":
    print('start')
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_error_handler(error)

    print('pooling')

    app.run_polling(poll_interval=3)