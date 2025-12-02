from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, ContextTypes
from config import config
from pymongo import MongoClient

# --- Flask app ---
app = Flask(__name__)

# --- Telegram bot ---
bot = Bot(token=config.BOT_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

# --- MongoDB ---
client = MongoClient(config.DATABASE_URL)
db = client["mydb"]
users_collection = db['users']

# --- /start command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("بوت يعمل على Render!")

dispatcher.add_handler(CommandHandler("start", start))

# --- Webhook route ---
@app.route(f'/{config.BOT_TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# --- Root route ---
@app.route("/")
def index():
    return "بوت تيليجرام يعمل!"
