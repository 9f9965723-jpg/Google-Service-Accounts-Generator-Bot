# bot.py
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
from config import config
from pymongo import MongoClient

# --- Flask app ---
app = Flask(__name__)

# --- Telegram bot ---
bot = Bot(token=config.BOT_TOKEN)
dispatcher = Dispatcher(bot, None)

# --- MongoDB connection ---
client = MongoClient(config.DATABASE_URL)
db = client.get_database()
users_collection = db['users']

# --- /start command ---
def start(update, context):
    update.message.reply_text("بوت يعمل على Render!")

dispatcher.add_handler(CommandHandler("start", start))

# --- Webhook route ---
@app.route(f'/{config.BOT_TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# --- root route ---
@app.route("/")
def index():
    return "بوت تيليجرام يعمل!"
