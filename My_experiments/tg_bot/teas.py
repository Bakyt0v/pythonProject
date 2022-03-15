from aiogram import types, Dispatcher
from aiogram.dispatcher import  FSMContext
from aiogram.dispatcher.filters import  Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

from config import dp, bot

class FSMADMIN (StatesGroup):
    photo = State()
    title = State()
    description = State()

async  def is_admin_func(message: types.Message):
    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Admin, what u ll do')

async  def fsm_start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await FSMADMIN.photo.set()

async def load_title(message: types.Message,
                     state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async  with state.proxy() as data:
            data['title'] = message.text
        await FSMADMIN

def register_handler_fsmadmin(dp: Dispatcher):
    dp.register_message_handler()