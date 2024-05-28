import os
import telebot
from telebot import types
import time 
from keep_alive import keep_alive
keep_alive()

Token = "7134860156:AAELTo-DKi17tB49Xd5Xrq-hi_ft-ocNY_s"
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=["start"])
def start(message):
    # Get the user's username
    username = message.from_user.username

    # Construct the welcome message including the username
    welcome_message = f"Hello @{username} 👋🏻,\nWelcome to Play & Earn Money Bot, produced by Dragos Complex 🇦🇱 \n\nLet's get started ✅"

    # Send the welcome message
    bot.send_message(message.chat.id, welcome_message)

    # Create the inline keyboard markup with the "Continue 💥" button
    markup = types.InlineKeyboardMarkup()
    continue_button = types.InlineKeyboardButton(text="Continue 💥", callback_data="continue")
    markup.add(continue_button)

    # Send the "Continue 💥" button after the welcome message
    bot.send_message(message.chat.id, "Would you like to Continue ?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "continue":
        # Send the "Rules" message
        rules_message = "Rules :\n\n1. Click on the button given below and go to the website.\n\n2. Make a simple registration, then you will get welcome bonus upto 550₹ 💵\n\n3. Now you are done ✅, you can start playing games and earn money daily"
        bot.send_message(call.message.chat.id, rules_message)
        
        # Add the "Click Here 🔗" button
        markup = types.InlineKeyboardMarkup()
        click_here_button = types.InlineKeyboardButton(text="Click Here 🔗", url="https://winzo.onelink.me/gu8K/e8953bb0")
        markup.add(click_here_button)
        
        # Send the "Click Here 🔗" button after the "Rules" message
        bot.send_message(call.message.chat.id, "Just go 📈", reply_markup=markup)

        # Send the contact message
        bot.send_message(call.message.chat.id, "Please contact us for your query: @Dragoscomplex")

@bot.message_handler(commands=["help"])
def help(message):
    # Send the contact message
    bot.send_message(message.chat.id, "Please contact us for your query: @Dragoscomplex")

# Handler for all messages except "/start" and "/help"
@bot.message_handler(func=lambda message: message.text and not message.text.startswith(('/start', '/help')))
def handle_all_messages(message):
    # Reply with the specified message
    bot.send_message(message.chat.id, "We reply within 24 hours....")
    # Schedule the message to disappear after 20 hours
    time.sleep(20 * 3600)  # 20 hours in seconds
    bot.delete_message(message.chat.id, message.message_id)

while True:
    try:
        bot.polling()
    except Exception as e:
        print(e)
        time.sleep(5)