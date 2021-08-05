"""
The Giant Penis License (GPL)
Copyright (c) 2021 @InukaAsith

<http://giant-penis-license.org/>

                ▄▄██▄██▄▄
              ▄█    █    █▄
             ▄█           █▄
             █             █
            █               █
            █               █
            █               █
            █               █
             █▄     █     ▄█
              █    ▄▄▄    █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
              █           █
        ▄████▄█           █▄████▄
      ▄█                         █▄
     █                             █
    █                               █
    █                               █
    █                               █
    █             ▄▄█▄▄             █
     █           █     █           █
      █▄       ▄█       █▄       ▄█
        █▄▄▄▄▄█           █▄▄▄▄▄█

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


🤣 NO SUCH PENIS LICENSE. DO WHATEVER YOU LIKE. UNLICENSED..
"""




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
