# -*- coding: utf-8 -*-
import os
from telethon import TelegramClient, events, utils

api_id = 123456789 # CHANGE THIS
api_hash = "12131321" # CHANGE THIS
bot_token = "TOKEN" # CHANGE THIS 

bot = TelegramClient("52345", api_id, api_hash).start(bot_token=bot_token)
dir_images = os.path.join("input","img")
dir_document = os.path.join("input","doc")
file_cats = os.path.join("img","cats.jpg")
if not os.path.isdir(dir_images):
    os.makedirs(dir_images)
if not os.path.isdir(dir_document):
    os.makedirs(dir_document)
    
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    #print("start. Sender",name,"say",event.text)
    #await event.respond('Hi!')
    await event.reply('Howdy, how are you doing?')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='(^cat[s]?$|puss)'))
async def cats(event):
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    #print("NewMessage cats. Sender",name,"say",event.text)
    await event.reply('Cats', file=file_cats,force_document=True)
    raise events.StopPropagation

@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message."""
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    text = str(event.text)
    #print("NewMessage. Sender",name,"say",text)
    #print(event)
    if event.photo:
        await event.reply('Start download file')
        path = await event.download_media(file=dir_images)
        print('File saved to', path)  # printed after download is done        
        await event.respond('File saved to ' + path)
    if event.document:
        await event.reply('Start download file')
        path = await event.download_media(file=dir_document)
        print('File saved to', path)  # printed after download is done        
        await event.respond('File saved to ' + path)
    if len(text)>0:
        await event.respond(event.text)

def main():
    """Start the bot."""
    try:
        print('(Press Ctrl+C to stop this)')
        bot.run_until_disconnected()
    finally:
        bot.disconnect()
        

if __name__ == '__main__':
    main()
