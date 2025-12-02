# app.py
import os
import asyncio
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pymongo import MongoClient
from config import config

# --- Flask app ---
app = Flask(__name__)

# --- Telegram bot ---
bot_token = config.BOT_TOKEN
application = ApplicationBuilder().token(bot_token).build()

# --- MongoDB connection ---
client = MongoClient(config.DATABASE_URL)
db = client["mydb"]  # اسم قاعدة البيانات
users_collection = db['users']

# --- /start command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("بوت يعمل على Render!")

application.add_handler(CommandHandler("start", start))

# --- Webhook route ---
@app.route(f'/{bot_token}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot=application.bot)
    asyncio.run(application.update_queue.put(update))
    return "ok"

# --- root route ---
@app.route("/")
def index():
    return "بوت تيليجرام يعمل!"

# --- تشغيل Flask لوحده لو في debug ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
