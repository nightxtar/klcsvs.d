import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "6213538")
    API_HASH = environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "ForwardBot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Forwardbot:yuvraj178@forwardbot.xnamt.mongodb.net/?retryWrites=true&w=majority&appName=Forwardbot")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Forward_Bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6471106079').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002311107123'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/forward_force_sub") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
