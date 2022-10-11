
from asyncio import streams
from operator import concat
from pytube import YouTube
import logging
logging.basicConfig(filename='bot.log', level=logging.INFO)


from telegram import Update
from telegram.ext import  ContextTypes, ConversationHandler


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   
    await update.message.reply_text(f'/hi\n/help\n/start\n/stop')



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text('Привет друг, ты хотел бы скачать видео с ютуба?')
    return 1

async def do_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    answer = update.message.text
    if answer.lower() =='да' or answer.lower() =='yes':
        await update.message.reply_text('Тогда напиши URL файла, который будем скачивать')
        return 2
    elif answer.lower() =='нет' or answer.lower() =='no':
        await update.message.reply_text('Тогда будем качать только звук.Напиши URL файла, который будем скачивать')
        return 3
    else:
        await update.message.reply_text('Ну как хочешь')
        return ConversationHandler.END


   
async def download_video (update: Update, context: ContextTypes.DEFAULT_TYPE):
    url= update.message.text
    video480  = YouTube(url).streams.filter(res='480p').desc().first()
    video480.download()

    sound = YouTube(url).streams.filter(only_audio=True,mime_type="audio/webm").first()
    sound.download() 
   
    await update.message.reply_text('Файл видео успешно скачано в Вашу папку')
    return ConversationHandler.END

async def download_sound (update: Update, context: ContextTypes.DEFAULT_TYPE):
    url= update.message.text

    sound = YouTube(url).streams.filter(only_audio=True,mime_type="audio/webm").first()
    sound.download() 
   
    await update.message.reply_text('Файл звука успешно скачано в Вашу папку')
    return ConversationHandler.END

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text('Жаль.Заходи еще')
    return ConversationHandler.END




