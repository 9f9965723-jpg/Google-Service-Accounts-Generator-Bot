# bot.py
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import config
from pymongo import MongoClient
import asyncio

from flask import Flask

app = Flask(__name__)


# --- MongoDB connection ---
client = MongoClient(config.DATABASE_URL)
db = client.get_database()
users_collection = db['users']

# --- Telegram bot using Application (v20+) ---
application = ApplicationBuilder().token(config.BOT_TOKEN).build()

# --- /start command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("بوت يعمل على Render!")

application.add_handler(CommandHandler("start", start))

# --- Webhook route ---
@app.route(f'/{config.BOT_TOKEN}', methods=['POST'])
def webhook():
    json_update = request.get_json(force=True)
    update = Update.de_json(json_update, application.bot)
    asyncio.get_event_loop().create_task(application.process_update(update))
    return "ok"

# --- root route ---
@app.route("/")
def index():
    return "بوت تيليجرام يعمل على Render!"
