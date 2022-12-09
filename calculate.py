from telegram import Bot
from telegram.ext import Updater, CommandHandler
import math
from operation import *

bot = Bot(token='ВВЕДИТЕ ВАШ ТОКЕН')
updater = Updater(token='ВВЕДИТЕ ВАШ ТОКЕН')
dispatcher = updater.dispatcher

help_handler = CommandHandler("help", help)
sum_handler = CommandHandler("sum", sum)
mod_handler = CommandHandler("mod", mod)
div_handler = CommandHandler("div", div)
mult_handler = CommandHandler("mult", mult)
sub_handler = CommandHandler("sub", sub)
sqrt_handler = CommandHandler("sqrt", sqrt)
pow_handler = CommandHandler("pow", pow)

dispatcher.add_handler(help_handler)
dispatcher.add_handler(sum_handler)
dispatcher.add_handler(mod_handler)
dispatcher.add_handler(div_handler)
dispatcher.add_handler(mult_handler)
dispatcher.add_handler(sub_handler)
dispatcher.add_handler(sqrt_handler)
dispatcher.add_handler(pow_handler)


updater.start_polling()

updater.idle()
