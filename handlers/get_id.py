from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember

get_id_router: Router = Router()

@get_id_router.message()
async def get_id(msg:Message):
    try:
        file_id = msg.video.file_id
        await msg.reply(file_id)
    except:
        await msg.answer('Kechirasiz bunday malumot yuq')