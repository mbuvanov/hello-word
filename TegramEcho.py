import telebot

bot = telebot.TeleBot("TOKEN")
#instead 'TOKEN' you put your own API token

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.send_message (message.chat.id, message.text)

#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)

bot.polling( none_stop = True )

