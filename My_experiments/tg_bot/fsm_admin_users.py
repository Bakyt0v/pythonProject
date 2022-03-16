from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.dispatcher.filters import Text



class hw(StatesGroup):
    username = State()
    firstname = State()
    lastname = State()


async def is_admin_func(message: types.Message):
    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(message.from_user.id, "I can add to data some information just give me a command as /add")


async def fsm_start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await hw.username.set()
        await message.reply("Send your username")


async def load_username(message: types.Message,
                     state: FSMContext):
    # if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["username"] = message.text
        await hw.next()
        await message.reply("Send me a firstname")


async def load_firstname(message: types.Message,
                     state: FSMContext):
    # if message.from_user.id == ADMIN_ID:
    async with state.proxy() as data:
        data['fisrtname'] = message.text
    await hw.next()
    await message.reply("Admin, send me lastname, please")


async def load_lastname(message: types.Message,
                           state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["lastname"] = message.text
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()

def register_handler_fsm_admin_user(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['add'], state=None)
    dp.register_message_handler(load_username, state=hw.username)
    dp.register_message_handler(load_firstname, state=hw.firstname)
    dp.register_message_handler(load_lastname, state=hw.lastname)
    dp.register_message_handler(is_admin_func, commands=['user_register'], is_chat_admin=True)