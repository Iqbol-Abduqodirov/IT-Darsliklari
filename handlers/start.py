from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from keyboards.start_menu import menu, menu2, menu3, menu4, menu5


start_router: Router = Router()


@start_router.message(CommandStart())
async def  start_handler(msg: Message):
    await msg.answer(f'Assalomu aleykum{msg.from_user.full_name} xush kelibsiz!', reply_markup=menu)

@start_router.message(F. text=='Darslarni boshlash')
async def dars_handler(msg:Message):
    await msg.answer("Quyidagi bo'limlardan tanlang.",reply_markup=menu2)

@start_router.message(F. text=="Dasturlash")
async def dars_handler(msg:Message):
    await msg.answer("Kursni tanlang: ",reply_markup=menu3)

@start_router.message(F. text=="Front-end")
async def dars_handler(msg:Message):
    await msg.answer("Kursni tanlang: ",reply_markup=menu4)

@start_router.message(F. text=="HTML")
async def html(msg:Message):
    await msg.answer("Dars sonini tanlang ",reply_markup=menu5)
    
@start_router.message(F.text=='0-dars')
async def dars0(msg:Message):
    await msg.answer_video('BAACAgIAAxkBAAMXZp0ykj37xi28mtFLVpnI_ZLS6zkAAhYLAAJbWZlIinJ5QOu7xK01BA', caption='HTML Darslari | 0-dars | Kurs haqida')

@start_router.message(F.text=='1-dars')
async def dars0(msg:Message):
    await msg.answer_video('BAACAgIAAxkBAAMZZp00BOQiOjcD-Hbbfa1H_xGbx4QAAhcLAAJbWZlIRe0BQNZ7TD01BA', caption='HTML Darslari | 1-dars | WEB haqida ')

@start_router.message(F.text=='2-dars')
async def dars0(msg:Message):
    await msg.answer_video('BAACAgIAAxkBAAMbZp00KM8JqxogLnUYiEH5UZLiP70AAsoMAAJQv4FLVLvvmlxUEj41BA', caption='HTML Darslari | 2-dars | Kurs haqida')

@start_router.message(F.text=='3-dars')
async def dars0(msg:Message):
    await msg.answer_video('BAACAgIAAxkBAAMdZp00OaJUXIBUY0hw0rc3Jh6esG4AAhoLAAJbWZlIYXr3DZJM8f81BA', caption='HTML Darslari | 3-dars | Kurs haqida')

@start_router.message(F.text=='4-dars')
async def dars0(msg:Message):
    await msg.answer_video('BAACAgIAAxkBAAMfZp00Sce5-T3cI2ZLqejkbKHb72IAAhwLAAJbWZlIYFwYAu6UXZU1BA', caption='HTML Darslari | 4-dars | Kurs haqida')

@start_router.message(F.text=='5-dars')
async def dars0(msg:Message):
    await msg.answer_video('BAACAgIAAxkBAAMhZp00V3yIVY6fJ5CthFnudlgEEpgAAh0LAAJbWZlIC6-GQgmlmAE1BA', caption='HTML Darslari | 5-dars | Kurs haqida')

@start_router.message(F.text=='6-dars')
async def dars0(msg:Message):
    await msg.answer_video('BAACAgIAAxkBAAMjZp00Zkm7ybqxNVFvjzBDAhAEaj8AAppJAALFeClJ-otYswPovos1BA', caption='HTML Darslari | 6-dars | Kurs haqida')

@start_router.message(F.text=='7-dars')
async def dars0(msg:Message):
    await msg.answer_video('BAACAgIAAxkBAAMlZp00dP6RO9gUnzwZkBHIvofqi8wAAmEMAALYJaBLKEtx2AP6jfY1BA', caption='HTML Darslari | 7-dars | Kurs haqida')

@start_router.message(F.text=='8-dars')
async def dars0(msg:Message):
    await msg.answer_video('BAACAgIAAxkBAAMnZp00gj6sFgtUVC_L0bvK3Ai_jxUAAh8LAAJbWZlI4NO3OrPu4ZI1BA', caption='HTML Darslari | 8-dars | Kurs haqida')

@start_router.message(F.text=='9-dars')
async def dars0(msg:Message):
    await msg.answer_video('BAACAgIAAxkBAAMpZp00jxxK4j8RsV51RPQfmL9m91UAAmIMAALYJaBLy5dUGWWdHec1BA', caption='HTML Darslari | 9-dars | Kurs haqida')

@start_router.message(F.text=='10-dars')
async def dars0(msg:Message):
    await msg.answer_video('BAACAgIAAxkBAAMrZp00m03VzSta1Iyy4wABg-T7zI6xAAIgCwACW1mZSN1Sjz1mMnP-NQQ', caption='HTML Darslari | 10-dars | Kurs haqida')

