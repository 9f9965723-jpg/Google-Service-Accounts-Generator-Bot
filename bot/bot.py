from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
from config import config
from pymongo import MongoClient

# --- إعداد Flask ---
app = Flask(__name__)

# --- إعداد البوت ---
bot = Bot(token=config.BOT_TOKEN)
dispatcher = Dispatcher(bot, None)

# --- إعداد MongoDB ---
client = MongoClient(config.DATABASE_URL)
db = client.get_database()  # يمكنك تحديد اسم قاعدة البيانات هنا
users_collection = db['users']  # مثال على مجموعة المستخدمين

# --- أمر /start ---
def start(update, context):
    update.message.reply_text("بوت يعمل على Render!")

dispatcher.add_handler(CommandHandler("start", start))

# --- Webhook route ---
@app.route(f'/{config.BOT_TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# --- صفحة رئيسية للتأكد من أن السيرفر يعمل ---
@app.route("/")
def index():
    return "بوت تيليجرام يعمل!"
