from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,  MessageHandler,filters,ConversationHandler
from bot_command import *




app = ApplicationBuilder().token("5166657423:AAGycm6m2r3OUsbNDSQBoGOifyvwIxkGrqU").build()

download = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states= {
        1:[MessageHandler(filters.TEXT,do_video)],
        2:[MessageHandler(filters.TEXT,download_video)],
        3:[MessageHandler(filters.TEXT,download_sound)]
    },
    fallbacks=[CommandHandler("stop", stop)]
)
app.add_handler(download)

app.add_handler(CommandHandler("start", hi_command))
app.add_handler(CommandHandler("stop", hi_command))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))


print('server start')
app.run_polling()