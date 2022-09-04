# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                 #
#   Created by Matteo Tramontina                  #
#   Date: 4 September 2022                        #
#   Version: 1.0                                  #
#   Github: https://github.com/tr4mo              #
#   Email: matteo.tramontina@outlook.com          #
#                                                 #
#   You can use this program for free, just       #
#   credit me if you use it for public purposes   #
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # #


# externals just for telegram bot, other ext are already in 'download_script.py'
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import download_script

import os


# this is the unique bot token (do not share!)
TOKEN = "PASTE_YOUR_TOKEN_RIGHT_HERE"

# this function starts when you type /start 
def start(update, context):
	update.message.reply_text("Hello! Start downloading music by sending me a YouTube link!")

def reply(update, context):
	
	text = update.effective_message.text


	if "youtu" in text:
		update.message.reply_text("Let me verify if the link exists.")
		try:
			update.message.reply_text("Ok I'm downloading the song...")
			song_name = download_script.downloadSong(text)
			update.message.reply_text("I successfully downloaded \"" + song_name + "\"!")
			file = open(song_name + ".mp3", "rb")
			update.message.reply_audio(file)
			file.close()
			print(song_name + " has been successfully downloaded.")
			#os.remove(song_name + ".mp3")
		except:
			update.message.reply_text("Apparently this link isn't working...\nTry a different one.")
	
	
	else:
		update.message.reply_text("Are you sure \"" + text + "\" is a YouTube link?\nTry to paste it on any browser search bar and verify it's integrity.")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
print("bot listening ...")
updater.start_polling()
