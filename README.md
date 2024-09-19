# Registration bot

Bu bot sizni Sifat o`quv markaziga ruyxatdan utkazadi. buning uchun ```/regist``` deb yozsangiz kifoya!!!

## Xususiyatlar
- ```/menu``` asosiy menuni chiqarib beradi.
- ```/regist``` ro`yxatdan utkazadi.

## Texnologiyalar
- Python 3.7 yoki undan yuqori versiya
- aiogram kutubxonasi

## O'rnatish
1. GitHub repozitoriyasini klonlang:
    ```bash
    git clone https://github.com/Rakhmatulloyev/registratsiya-boti.git
    ```

2. Zaruriy kutubxonalarni o'rnating:
    ```bash
    pip install -r requirements.txt
    ```
3. `.env` faylini yaratib, quyidagi ma'lumotlarni qo'shing:
    ```bash
    BOT_TOKEN=your-telegram-bot-token
    CHANNELS=your-channels-id
    ADMINS=your-id
    ```

## Filtrlar
- `admin.py`: Adminlar uchun maxsus funksiyalarni filtrlaydigan kodlar joylashgan.
- `check_sub_channel.py`: Foydalanuvchining kerakli kanalga obuna bo‘lganligini tekshiruvchi kodlar.

## Klaviatura tugmalari
- `admin_keyboard.py`: Bot interfeysida adminlar uchun klaviatura tugmalari sozlanadi.

## Menyu buyruqlari
- `set_bot_commands.py`: Telegram bot menyusidagi buyruqlarni o'rnatish uchun skript.

## Ishga tushurish
Botni quyidagi buyruq orqali ishga tushiring:
```bash
python bot.py
