import os
import telebot
import google.generativeai as genai

# 
TELEGRAM_TOKEN = "8603084758:AAFHkOrWjjj82oWEBFVCr6U-TB-C157ycdc"
GEMINI_API_KEY = 
"AQ.Ab8RN6L0QW-BUIPjORdl_VqB1sUhKjka1D1WPrUVv_NlswXRnQ"

# Conexión con Google AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Conexión con Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        # Pregunta a Gemini
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Ups, tuve un problema. Intenta de nuevo.")

# Arrancar el bot
print("Bot en marcha...")
bot.infinity_polling()
