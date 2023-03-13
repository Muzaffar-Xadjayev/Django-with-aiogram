import requests
import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.data.config import ADMINS
from bot.loader import dp, db, bot

BASE_URL = "http://127.0.0.1:8000/"

@dp.message_handler(commands=["start"])
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    # data = requests.get(f"{BASE_URL}/users").json()
    # print(data)
    await message.answer("SALOM")
    # ADD USER IN DB
    # try:
    #
    #     # await db.add_user(
    #     #     telegram_id=message.from_user.id,
    #     #     full_name=name,
    #     #     username=message.from_user.username
    #     # )
    #     await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!")
    #     count = await db.select_all_user()
    #     msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {len(count)} ta foydalanuvchi bor."
    #     for user in ADMINS:
    #         await bot.send_message(user, msg)
    #
    # except asyncpg.exceptions.UniqueViolationError:
    #     await message.answer(f"Hurmatli Foydalanuvchi siz Bot ga a'zo bo'lgansiz bemalol foydalanishingiz mumkin.")


