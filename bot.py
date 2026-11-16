import io
import pyautogui
import telebot

BOT_TOKEN = "ВАШ_ТОКЕН_БОТА"
ALLOWED_USER_ID = 123456789  # ваш ID

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
  if message.from_user.id != ALLOWED_USER_ID:
    return

  if message.text and message.text.lower().strip() == "скриншот":
    screenshot = pyautogui.screenshot()
    img_bytes = io.BytesIO()
    screenshot.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    bot.send_photo(message.chat.id, img_bytes)


bot.polling(none_stop=True)
