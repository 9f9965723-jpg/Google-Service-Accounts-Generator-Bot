import os

class Config:
    # توكن بوت تيليجرام
    BOT_TOKEN = os.environ.get('BOT_TOKEN')

    # بيانات Pyrogram
    APP_ID = os.environ.get('APP_ID')
    API_HASH = os.environ.get('API_HASH')

    # رابط قاعدة البيانات MongoDB
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    # اسم قاعدة البيانات (مطلوب إذا لم يكن موجود ضمن URI)
    DATABASE_NAME = os.environ.get('DATABASE_NAME', 'mydb')

    # المستخدمين المصرح لهم بالبوت (مفصولين بفواصل)
    SUDO_USERS = list(map(int, os.environ.get('SUDO_USERS', '').split(','))) if os.environ.get('SUDO_USERS') else []

    # روابط وأماكن التخزين
    SUPPORT_CHAT_LINK = "t.me/moedyiu"
    DOWNLOAD_DIRECTORY = "./downloads/"

# نسخة جاهزة للاستدعاء
config = Config()


class BotCommands:
  Authorize = ['auth', 'start']
  Revoke = ['revoke']
  EmptyTrash = ['emptyTrash']
  Proj = ['projects']
  Cproj = ['newproject']
  Delsas = ['delsas']
  Sas = ['sas']
class Messages:
    
    DOWNLOAD_TG_FILE  = "🔒 **DOWNLOADING CREDENIAL FILE.**"

    DOWNLOADED_SUCCESSFULLY = "🔒 **SUCCESSFULLY DOWNLOADED CREDENIAL FILE.**\n__Send /auth to authenticate.__"

    NOT_AUTH = f"🔑 **No credentials found. Please enable the Drive API in:\nhttps://developers.google.com/drive/api/v3/quickstart/python\nand upload the json file as credentials.json**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    ALREADY_AUTH = "🔒 **Already authorized your Google Drive Account.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Authorized Google Drive account Successfully.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'
    
    AUTH_TEXT = "⛓️ **To Authorize your Google Drive account visit this [URL]({}) and send the generated code here.**\n__Visit the URL > Allow permissions > you will get a code > copy it > Send it here__"
    
    REVOKED = f"🔓 **Revoked current logged account successfully.**\n__Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.__"
    
