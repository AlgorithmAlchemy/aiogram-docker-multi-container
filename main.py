import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio

logging.basicConfig(level=logging.INFO)


class BotApp:
    def __init__(self, token):
        self.bot = Bot(token=token)
        self.dp = Dispatcher()

        self.reply_keyboard = self.create_reply_keyboard()
        self.inline_kb = self.create_inline_keyboard()

        self.register_handlers()

    def create_reply_keyboard(self):
        button_how_are_you = KeyboardButton(text='How are you?')
        button_inline_example = KeyboardButton(text='Inline buttons')
        keyboard = [[button_how_are_you, button_inline_example]]
        return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    def create_inline_keyboard(self):
        inline_btn_1 = InlineKeyboardButton(text='Good', callback_data='good')
        inline_btn_2 = InlineKeyboardButton(text='Not so good', callback_data='bad')
        inline_btn_url = InlineKeyboardButton(text='Open Google', url='https://www.google.com')

        inline_kb = InlineKeyboardMarkup(inline_keyboard=[
            [inline_btn_1, inline_btn_2],
            [inline_btn_url]
        ])

        return inline_kb

    async def on_message(self, message: types.Message):
        if message.text == 'How are you?':
            await message.answer("I'm doing great, thank you! How about you?")
        elif message.text == 'Inline buttons':
            await message.answer("Choose one of the options:", reply_markup=self.inline_kb)
        else:
            await message.answer("Hello! How are you doing?", reply_markup=self.reply_keyboard)

    async def on_callback_query(self, callback_query: types.CallbackQuery):
        if callback_query.data == 'good':
            await callback_query.answer(text="Glad you're doing well!")
        elif callback_query.data == 'bad':
            await callback_query.answer(text="Hope everything gets better soon!")

    def register_handlers(self):
        self.dp.message.register(self.on_message)
        self.dp.callback_query.register(self.on_callback_query, lambda c: c.data in ['good', 'bad'])

    async def run(self):
        await self.dp.start_polling(self.bot)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py <API_TOKEN>")
        sys.exit(1)

    API_TOKEN = sys.argv[1]
    bot_app = BotApp(token=API_TOKEN)
    asyncio.run(bot_app.run())