import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.config import OWNER_USERNAME, SUPPORT_GROUP, SUPPORT_CHANNEL

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   
    
@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b93274f340d94dac0c1ef.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💫🙈🙈 𝙔𝙚 𝙩𝙜 𝙠𝙖 𝙗𝙚𝙨𝙩 𝙢𝙪𝙨𝙞𝙘 𝙗𝙤𝙩 𝗵𝙖𝙞 𝙟𝙤 𝙡𝙖𝙜 𝙛𝙧𝙚𝙚 𝙢𝙪𝙨𝙞𝙘 𝙗𝙖𝙟𝙖𝙮𝙚𝙜𝙖
𝙖𝙥𝙠𝙚 𝙫𝙘 𝙢𝙚𝙞𝙣🙄.𝙊𝙬𝙣𝙚𝙧:- 𝙬𝙖𝙧𝙧𝙞𝙤𝙧 𝐑𝐢𝐃𝐄𝐑  ...
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁: [𝐖𝐀𝐑𝐑𝐈𝐎𝐑](https://t.me/Blue_warrior_riders)
┣★ 𝐎𝐖𝐍𝐄𝐑: [@Masoom_banda]
┣★ 𝗚𝗿𝗼𝘂𝗽 : [𝐖𝐀𝐑𝐑𝐈𝐎𝐑](https://t.me/Blue_warrior_riders)
┗━━━━━━━━━━━━━━━━━┛
𝗔𝗴𝗮𝗿 𝗮𝗽𝗸𝗼 𝗸𝗼𝗶 𝗱𝗶𝗸𝗸𝗮𝘁 𝗮𝗿𝗶 𝘁𝗼𝗵 𝗶𝗱𝗵𝗮𝗿 𝗷𝗮𝗸𝗲 𝗼𝘄𝗻𝗲𝗿 𝘀𝗲
𝗰𝗼𝗻𝘁𝗮𝗰𝘁 𝗸𝗮𝗿𝗲😍 [𝐑𝐢𝐃𝐄𝐑](@masoom_banda)(https://t.me/Blue_warrior_riders)...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥳𝙊𝙬𝙣𝙚𝙧 𝙞𝙙𝙝𝙖𝙧 𝙢𝙞𝙡𝙚𝙣𝙜𝙚🤩", url=f"https://t.me/Blue_warrior_riders")
                ]
                
           ]
        ),
    )
    
