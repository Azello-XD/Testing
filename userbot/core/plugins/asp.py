import random

from pyrogram.enums import MessagesFilter
from userbot.core.function.emoji import emoji
from userbot import *


async def video_asupan(client, message):
    y = await message.reply_text(emoji("proses") + f"**mencari video asupan**...", quote=True)
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@asupanNyaSaiki", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)

async def photo_cewek(client, message):
    y = await message.reply_text(emoji("proses") + f"**mencari ayang...**", quote=True)
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            "@ayangSaiki", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


async def photo_cowok(client, message):
    y = await message.reply_text(emoji("proses") + f"**mencari ayang...**", quote=True)
    try:
        ayang2nya = []
        async for ayang2 in client.search_messages(
            "@ayang2Saiki", filter=MessagesFilter.PHOTO
        ):
            ayang2nya.append(ayang2)
        photo = random.choice(ayang2nya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


async def photo_anime(client, message):
    y = await message.reply_text(emoji("proses") + f"**mencari anime...**", quote=True)
    anime_channel = random.choice(["@animehikarixa", "@anime_WallpapersHD"])
    try:
        animenya = []
        async for anime in client.search_messages(
            anime_channel, filter=MessagesFilter.PHOTO
        ):
            animenya.append(anime)
        photo = random.choice(animenya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
