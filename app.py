from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import config
from pymongo import MongoClient
import asyncio

# --- Flask app ---
app = Flask(__name__)

# --- Telegram bot ---
bot_token = config.BOT_TOKEN
application = ApplicationBuilder().token(bot_token).build()

# --- MongoDB ---
client = MongoClient(config.DATABASE_URL)
db = client["mydb"]
users_collection = db['users']

# --- /start command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("بوت يعمل على Render!")

application.add_handler(CommandHandler("start", start))

# --- Webhook route ---
@app.route(f'/{bot_token}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot=application.bot)
    asyncio.run(application.update_queue.put(update))  # أرسل update للـ queue
    return "ok"

# --- Root route ---
@app.route("/")
def index():
    return "بوت تيليجرام يعمل!"
