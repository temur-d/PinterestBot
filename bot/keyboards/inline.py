from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lang_buttons = InlineKeyboardMarkup(row_width=2)
lang_buttons.add(
    InlineKeyboardButton(
        text='Русский 🇷🇺',
        callback_data='ru'
    ),
    InlineKeyboardButton(
        text='English 🏴󠁧󠁢󠁥󠁮󠁧󠁿',
        callback_data='en'
    ),
    InlineKeyboardButton(
        text="O'zbek 🇺🇿",
        callback_data='uz',
    )
)