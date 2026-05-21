from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import os

BOT_TOKEN = os.getenv("8943722990:AAE0UdkJvSRUFwJDAiwIPW9PT2aAJPwpn6c") 
ADMIN_GROUP_ID = os.getenv("ID:-5207048723")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Заказингизни юборинг")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text

    msg = f"""
📦 Янги заказ

👤 {user.full_name}
🆔 {user.id}

📝 {text}
"""

    await context.bot.send_message(
        chat_id=ADMIN_GROUP_ID,
        text=msg
    )

    await update.message.reply_text("✅ Заказ админга юборилди")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot ishladi")
app.run_polling()
