import os
from pyrogram import Client, filters
from pyrogram.types import Message
from RobinMusic.filters import command, other_filters
from RobinMusic.decorators import sudo_users_only, errors

downloads = os.path.realpath("NIXA/downloads")
raw = os.path.realpath(".")

@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **ᴅᴇʟᴇᴛᴇᴅ ᴀʟʟ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ғɪʟᴇs**")
    else:
        await message.reply_text("❌ **ɴᴏ ғɪʟᴇs ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ**")

        
@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw)
    if ls_dir:
        for file in os.listdir(raw):
            if file.endswith('.raw'):
                os.remove(os.path.join(raw, file))
        await message.reply_text("✅ **ᴅᴇʟᴇᴛᴇ ᴀʟʟ ʀᴀᴡ ғɪʟᴇs**")
    else:
        await message.reply_text("❌ **ɴᴏ ʀᴀᴡ ғɪʟᴇs ғᴏᴜɴᴅ**")


@Client.on_message(command(["cleanup"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.raw *.jpg")
        await message.reply_text("✅ **ᴄʟᴇᴀɴᴇᴅ**")
    else:
        await message.reply_text("✅ **ᴀʟʀᴇᴀᴅʏ ᴄʟᴇᴀɴᴇᴅ**")
