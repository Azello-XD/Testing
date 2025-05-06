import asyncio

from pyrogram import idle
import os
from userbot import *
from pyrogram.errors import (AuthKeyUnregistered, SessionRevoked,
                             UserAlreadyParticipant, UserDeactivated,
                             UserDeactivatedBan)

async def start_ubot(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await ubot_.start()
    except (AuthKeyUnregistered, SessionRevoked, UserAlreadyParticipant, UserDeactivated, UserDeactivatedBan):
        await remove_ubot(user_id)
        await rm_all(user_id)
        await remove_all_vars(user_id)
        await rem_pref(user_id)
        await rem_expired_date(user_id)
        for X in await get_chat(user_id):
            await remove_chat(user_id, X)
        print(f"✅ {user_id} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦")


async def main():
    tasks = [
        asyncio.create_task(start_ubot(int(_ubot["name"]), _ubot))
        for _ubot in await get_userbots()
    ]
    await asyncio.gather(*tasks, bot.start())
    await asyncio.gather(loadPlugins(), expiredUserbots(), idle())

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
