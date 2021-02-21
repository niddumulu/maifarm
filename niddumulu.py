import time
import os

from telethon import TelegramClient, sync, events, utils
api_id = 682610
api_hash = '030132b51d598e464419ccee7f20212d'
client = TelegramClient('niddumulu', api_id, api_hash).start()

seconds = int(0)
minutes = int(0)

run = "dia"
while run.lower() == "dia":
    if seconds == 1:
           varilkan = "/tanamGuild_Wortel_1400" 
           client.send_message('KampungMaifamBot', varilkan)

    if seconds == 4:
           varilkan = "/KebunGuild_Siram"
           client.send_message('KampungMaifamBot', varilkan)

    if seconds == 9:
           varilkan = "/tanam_Wortel_500" 
           client.send_message('KampungMaifamBot', varilkan)

    if seconds == 15:
           varilkan = "/siram"
           client.send_message('KampungMaifamBot', varilkan)

    if seconds == 195:
           varilkan = "/kebunGuild_AmbilPanen"
           client.send_message('KampungMaifamBot', varilkan)

    if seconds == 205:
           varilkan = "/ambilPanen"
           client.send_message('KampungMaifamBot', varilkan)
    
    if seconds == 215:
          varilkan = "levelup"
          client.send_message('KampungMaifamBot', varilkan)

    if seconds == 220:
        
       run = "diaa"
    os.system('clear')
    seconds = (seconds + 1)
    print(seconds)
    time.sleep(1)
