#ʀᴏʙɪɴ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴠᴄ ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ ɴᴏ ʟᴀɢ

#ᴅᴇᴠᴇʟᴏᴘᴇʀs :- @SIXTH_H0KAGE & @GodlyDemxn
#sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
#ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates

import asyncio
from pytgcalls import idle
from RobinMusic.main import call_py, bot, BOT

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STARTING PYTGCALLSS CLIENT")
    await call_py.start()
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
BOT.run_until_disconnected()
