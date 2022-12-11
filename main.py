from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from func import *
from cons import *
upd = Updater(token=TOKEN, workers=4)
dis = upd.dispatcher
dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(CallbackQueryHandler(pattern='start', callback=start))
dis.add_handler(MessageHandler(Filters.voice, audio))
dis.add_handler(MessageHandler(Filters.photo, audio))
dis.add_handler(MessageHandler(Filters.sticker, audio))
dis.add_handler(MessageHandler(Filters.video, audio))
dis.add_handler(MessageHandler(Filters.video_note, audio))
dis.add_handler(MessageHandler(Filters.text, next_func))
# dis.add_handler(MessageHandler(Filters.location, get_location))
upd.start_polling(drop_pending_updates=True)