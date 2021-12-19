import os

import time

from pyrogram import Client

from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")



session_name = getenv(STRING_SESSION)
APP_ID = getenv(APP_ID)
API_HASH = getenv(API_HASH)
USER = getenv(USER)
DUMP_CHAT = getenv(DUMP_CHAT)
UPDATE_TIME = getenv(UPDATE_TIME)
UPDATE_TIME = int(UPDATE_TIME)
try:
    DUMP_CHAT = int(DUMP_CHAT)
except:
    pass


globonline = False


with Client(session_name,APP_ID,API_HASH) as app:
    
    print("Starting bot")

    while True:
      try:
          yeah = app.get_users(USER)
      except:
          pass
      
      if yeah.status=="online":
        online=True
        
      else:
        online=False
              
        
      
      if not globonline == online:
         
         if online == True:
            #print("User came online")
            app.send_message(DUMP_CHAT,"User came online")
         else:
            #print("User went offline")
            app.send_message(DUMP_CHAT,"User went offline")
         globonline = online
      time.sleep(UPDATE_TIME)
        
print("System Crashed with unknown reason")
