from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


course_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="Django"),
        ],
        
        [   KeyboardButton(text="Manzilimiz"), ],

        [   KeyboardButton(text="Biz_haqimizda"), ],
       
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)