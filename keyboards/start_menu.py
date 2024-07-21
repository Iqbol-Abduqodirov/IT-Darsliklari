from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Darslarni boshlash')
        ]
    ],
    resize_keyboard=True
)

menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kompyuter savodxonligi")
        ],
        [
            KeyboardButton(text="Grafik dizayn"),
            KeyboardButton(text="Dasturlash")
        ],
        [
            KeyboardButton(text="Kerakli dasturlar"),
            KeyboardButton(text="Biz bilan bog'lanish")
        ],
        [
            KeyboardButton(text="Bot haqida")
        ],
        
    ],
    resize_keyboard=True
)

menu3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton (text="Front-end"),
            KeyboardButton (text="Back-end")
        ],
        [
            KeyboardButton (text="Orqaga")
        ]
    ],
    resize_keyboard=True
)

menu4 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton (text ='HTML'),
            KeyboardButton (text = "CCS")
        ],
        [
            KeyboardButton (text ='JavaScript'),
            KeyboardButton (text = "React js")
        ],
        [
            KeyboardButton (text ='Orqaga'),
            KeyboardButton (text = "Asosiy menu")
        ]
    ],
    resize_keyboard=True
)

menu5 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton (text = '0-dars'),
            KeyboardButton (text = '1-dars')
        ],
        [
            
            KeyboardButton (text = '2-dars'),
            KeyboardButton (text = '3-dars')
        ],
        [
            
            KeyboardButton (text = '4-dars'),
            KeyboardButton (text = '5-dars')
        ],
        [
            
            KeyboardButton (text = '6-dars'),
            KeyboardButton (text = '7-dars')
        ],
        [
            
            KeyboardButton (text = '8-dars'),
            KeyboardButton (text = '9-dars')
        ],
        [
            KeyboardButton (text = '10-dars')
        ],
        [
            KeyboardButton (text ='Orqaga'),
            KeyboardButton (text = "Asosiy menu")
        ]
    ],
    resize_keyboard=True
)