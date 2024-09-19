from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from data import config
import asyncio
import logging
import sys
from menucommands.set_bot_commands  import set_default_commands
from baza.sqlite import Database
from filters.admin import IsBotAdminFilter
from filters.check_sub_channel import IsCheckSubChannels
from keyboard_buttons import admin_keyboard
import courses_button
from aiogram.fsm.context import FSMContext
from middlewares.throttling import ThrottlingMiddleware #new
from reklama import Adverts
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from states import Form
import time 
import re
ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id)
        await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz. \n /Menu deb yolzing va menudan birini tanlang!")
    except:
        await message.answer(text="Assalomu alaykum. /regist deb yozing")


@dp.message(IsCheckSubChannels())
async def kanalga_obuna(message:Message):
    text = ""
    inline_channel = InlineKeyboardBuilder()
    for index,channel in enumerate(CHANNELS):
        ChatInviteLink = await bot.create_chat_invite_link(channel)
        inline_channel.add(InlineKeyboardButton(text=f"{index+1}-kanal",url=ChatInviteLink.invite_link))
    inline_channel.adjust(1,repeat=True)
    button = inline_channel.as_markup()
    await message.answer(f"{text} kanallarga azo bo'ling",reply_markup=button)





#Admin panel uchun
@dp.message(Command("menu"))
async def is_admin(message:Message):
    await message.answer(text="menu",reply_markup=courses_button.course_button)

@dp.message(F.text=="Python")
async def users_count(message:Message):
    text = f"""Python kursimiz 1 oy bo`lib o`tadi.
dars rejalari:
🏁ILK QADAMLAR
#01 KERAKLI DASTURLAR
#02 HELLO WORLD!
#03 PRINT(), SINTEKS VA ARIFMETIK AMALLAR

🗂️ O'ZGARUVCHILAR VA MA'LUMOT TURLARI
#04 O'ZGARUVCHILAR
#05 STRING (MATN)
#06 SONLAR
#07 LIST (RO'YXAT)
#08 RO'YXATLAR BILAN ISHLASH
#09 FOR TAKRORLASH OPERATORI

🚦SHARTLAR VA TARMOQLANISH
#10 IF-ELSE
#11 BIR NECHTA SHARTLARNI TEKSHIRISH
LIRIK CHEKINISH #1
#12 XATOLAR BILAN ISHLASH
#13 GitHub PORTFOLIO

📔LUG'AT (DICTIONARY)
#14 LUG'AT BILAN TANISHUV
#15 LUG'AT ELEMENTLARI BILAN ISHLASH
#16 NESTING

🔁WHILE
#17 WHILE TSIKLI
#18 WHILE, RO'YXATLAR VA LUG'ATLAR

📜FUNKSIYALAR (FUNCTIONS)
#19 FUNKSIYA
#20 QIYMAT QAYTARUVCHI FUNKSIYA
#21 FUNKSIYA VA RO'YXAT
#22 MOSLASHUVCHAN FUNKSIYA (*args, **kwargs)
#23 MODULLAR
#24 FUNKSIYALAR. SON'GSO'Z.

🛠️ AMALIY MASHG'ULOTLAR
#25 "SON TOPISH" O'YINI
#26 "SO'Z TOPISH" O'YINI
#27 KIRILL-LOTIN TELEGRAM BOT

👨‍💻 OBJECT ORIENTED PROGRAMMING
OOP NIMA?
#28 KLASSLAR
#29 OBYKETLAR BILAN ISHLASH
#30 VORISLIK VA POLIMORFIZM
#31 INKAPSULYATSIA, KLASSNING XUSUSIYAT VA METODLARI
#32 DUNDER METODLAR

Ro`yxatdan o`tmoqchi bo`lsangiz /regist deb yozing!!!
"""
    await message.answer(text=text)

@dp.message(F.text=="Django")
async def users_count(message:Message):
    text = f"""Django kurslarimiz 2 oy bo`lib o`tadi
    #00 Python Django | Django nima?
    #01 Python Django | Command Prompt
    #02 Python Django | Python va PyCharm o'rnatamiz
    #03 Python Django | pipenv va Django
    #04 Python Django | Project va App
    #05 Python Django | MVT Model-View-Template
    #06 Python Django | "Hello, World!"
    #07 Python Django | Template yaratish
    #08 Python Django | Tayanch Template
    #09 Python Django | Loyihani Heroku Serverga Yuklash
    #10 Python Django | Birinchi Modelimiz
    va hokazolar
    Ro`yxatdan o`tmoqchi bo`lsangiz /regist deb yozing!!!
"""
    await message.answer(text=text)
   
@dp.message(F.text=="Manzilimiz")
async def users_count(message:Message):
    text = f"""📌 <b>Bizning manzilimiz: </b>Sifat IT Akademiyasi\n
    Navoiy sh. G'alabashox ko'chasi 77 | 7 uy, 
    Ro`yxatdan o`tmoqchi bo`lsangiz /regist deb yozing!!!
"""
    await message.answer(text=text)

@dp.message(F.text == "Biz_haqimizda")
async def users_count(message:Message):
    text = """<b>Biz haqimizda</b>

Sifatedu – bu dasturlash va IT sohasida ta'lim beruvchi yetakchi o'quv markazi. Bizning maqsadimiz – sizga eng so'nggi texnologiyalar va dasturlash tillari bo'yicha chuqur bilim va ko'nikmalar berishdir.

🌐 <b>Nimalarni taklif qilamiz:</b>
- Python dasturlash kurslari
- Django va boshqa web dasturlash framework-lari
- Ma'lumotlar tahlili va Data Science
- IT sohasida malaka oshirish kurslari

🔗 <b>Biz bilan bog'lanish:</b>
📞 Telefon: +998 88 378 08 08
📞 Telefon: +998 99 750 17 17

Ilim harbir yaxshilikning boshidir!
Ro`yxatdan o`tmoqchi bo`lsangiz /regist deb yozing!!!
"""
    await message.answer(text=text)

@dp.message(F.text=="Foydalanuvchilar soni")
async def users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

@dp.message(F.text=="Reklama yuborish")
async def advert_dp(message:Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")

@dp.message(Adverts.adverts)
async def send_advert(message:Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = await db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.5)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()

@dp.message(Command("admin"))
async def is_admin(message:Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)



@dp.message(Command("help"))
async def is_admin(message:Message):
    await message.answer(text="/start - botni ishga tushurish \n/help - botdan yorddam so`rash\n/admin - admin panelni chiqaradi \n/menu - menyuni chiqaradi \n/xabar - adminga xabar yuborish")


@dp.message(Command("regist"))
async def command_start_handler(message: Message,state:FSMContext) -> None:
    await state.set_state(Form.first_name)
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum,{full_name}\nRo'yhatdan o'tish uchun ismingizni kiriting!"
    await message.reply(text=text)

@dp.message(Form.first_name,F.text)
async def get_first_name(message:Message,state:FSMContext): 
     first_name = message.text
     await state.update_data(first_name=first_name)

     await state.set_state(Form.last_name)
     text = f"Familyangizni kiriting!"
     await message.reply(text=text)

@dp.message(Form.first_name)
async def not_get_first_name(message:Message,state:FSMContext):
    text = f"Iltimos ismingizni kiriting!"
    await message.reply(text=text)  

        
@dp.message(Form.last_name,F.text)
async def get_last_name(message:Message,state:FSMContext):
     
     last_name = message.text
     await state.update_data(last_name=last_name)

     await state.set_state(Form.email)
     text = f"Emailingizni kiriting!"
     await message.reply(text=text) 

@dp.message(Form.last_name)
async def not_get_last_name(message:Message,state:FSMContext):
    text = f"Iltimos familiyangizni yuboring!"
    await message.reply(text=text)    

@dp.message(Form.email)
async def get_email(message:Message,state:FSMContext):
    pattern = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    if re.match(pattern,message.text):

        email = message.text
        await state.update_data(email=email)

        await state.set_state(Form.photo)
        text = f"Rasmingizni yuboring!"
        await message.reply(text=text)
    
    else:
        await message.reply(text="Emailingizni noto'g'ri kiritdingiz")

@dp.message(Form.photo,F.photo)
async def get_photo(message:Message,state:FSMContext):

    photo = message.photo[-1].file_id 
    await state.update_data(photo=photo)
    await state.set_state(Form.phone_number)
    text = f"Telefon nomeringizni kiriting! +998 bilan yozing"
    await message.reply(text=text)

@dp.message(Form.photo)
async def not_get_photo(message:Message,state:FSMContext):
    text = f"Iltimos rasm yuboring!"
    await message.reply(text=text)




@dp.message(Form.phone_number)
async def get_phone_number(message:Message,state:FSMContext):
    pattern = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    if re.match(pattern,message.text):

        phone_number = message.text
        await state.update_data(phone_number=phone_number)

        await state.set_state(Form.address)
        text = f"Addressingizni kiriting!"
        await message.reply(text=text)
    
    else:
        await message.reply(text="telefon nomeringizni noto'g'ri kiritdingiz. +998 bilan yozing")     

      
@dp.message(Form.address)
async def get_address(message:Message,state:FSMContext):
    address = message.text
    await state.update_data(address=address)

    data = await state.get_data()    
    my_photo = data.get("photo")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    phone_number = data.get("phone_number")
    address = data.get("address")
    email = data.get("email")
    photo = data.get("photo")
    
    text = f"<b>Ariza</b>\nIsmi: {first_name}\nFamilyasi: {last_name}\nTel: {phone_number}\nManzil: {address}\nGmail: {email}"
    
    
    for admin in ADMINS:
        await bot.send_photo(admin,photo=my_photo,caption=text)
        # print(first_name,last_name,phone_number,address,email,photo)
    

    await state.clear()
    text = f"Siz muvaffaqiyatli tarzda ro'yhatdan o'tdingiz🎉"
    await message.reply(text=text)



from help_stt import Help




# Xabar yuborish komandasi
@dp.message(Command("xabar"))
async def help_commands(message: Message, state: FSMContext):
    await message.answer("Xabaringizni yozib ✍🏻 \nMurojatingiz 👤 adminga boradi !")
    await state.set_state(Help.help)
    

# Foydalanuvchining adminga yozgan xabarini jo'natish
@dp.message(Help.help)
async def send_advert(message: Message, state: FSMContext):
    try:
        # await bot.send_message(ADMINS[0],"📌 Yangi xabar")
        msg = f"{message.from_user.id} 📌 \n\nYangi xabar\n\n"
        msg += f"{message.text}"
        await bot.send_message(ADMINS[0], msg,parse_mode="html")
        await message.answer("Xabaringiz adminga yetkazildi")
        await state.clear()
        
    except:
        
        await message.answer("Faqat matn ko'rinishidagi xabarlarni yubora olasiz.")
        await message.answer("Marhamat adminga xabaringizni qoldiring.")


@dp.message(F.reply_to_message, IsBotAdminFilter(ADMINS))
async def is_admin(message: Message):
    try:    
            u_id = message.reply_to_message.text.split()[0]
            print(u_id, "*************")
            text = message.text
            await bot.send_message(int(u_id), text)
            await message.answer("xabaringiz yetkazildi. ")
    except:
        await message.answer("Nimadir xato bo'ldi")

def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    from middlewares.throttling import ThrottlingMiddleware
    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))

async def main() -> None:
    global bot, db
    bot = Bot(TOKEN)
    db = Database(path_to_db="main.db")
    await set_default_commands(bot)
    setup_middlewares(dispatcher=dp, bot=bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())\




@dp.startup()
async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)

#bot ishga tushganini xabarini yuborish
@dp.shutdown()
async def off_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishdan to'xtadi!")
        except Exception as err:
            logging.exception(err)




async def main() -> None:
    global bot,db
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    db = Database(path_to_db="main.db")
    db.create_table_users()
    await set_default_commands(bot)
    dp.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))
    await dp.start_polling(bot)
    




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    asyncio.run(main())
