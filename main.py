import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Загружаем токен из .env
load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    # Создаём клавиатуру с кнопками
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🍔 Меню")],
            [types.KeyboardButton(text="🛒 Корзина")],
            [types.KeyboardButton(text="💳 Оплатитьasd")],
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Добро пожаловать в **Wilco Food**! Выберите действие:",
        reply_markup=keyboard
    )

# Обработчик кнопки "Меню"
@dp.message(lambda msg: msg.text == "🍔 Меню")
async def show_menu(message: types.Message):
    # Инлайн-кнопки с категориями
    menu_keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Завтраки", callback_data="breakfast")],
            [types.InlineKeyboardButton(text="Напитки", callback_data="drinks")],
        ]
    )
    await message.answer("Выберите категорию:", reply_markup=menu_keyboard)

@dp.callback_query(lambda cb: cb.data == "breakfast")
async def show_breakfast(callback: types.CallbackQuery):
    items_keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Омлет с беконом (350 руб.)", callback_data="item_1")],
            [types.InlineKeyboardButton(text="Панкейки (290 руб.)", callback_data="item_2")],
        ]
    )
    await callback.message.edit_text("Завтраки:", reply_markup=items_keyboard)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())