from aiogram import Dispatcher,types
from config import bot


async def echo_message(message: types.Message):
    ban_words = ['адахан', 'амантур', 'java', 'bitch','kotok','коток','Amantur', 'блять','билять','сука','хуесос','далбаеп','ебать','kot','кот','рукажоп','бля']
    for i in ban_words:
        if i in message.text.lower().replace(' ', ''):
            await message.delete()
            await bot.send_message(message.chat.id, 'Сам такой!')

    if message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id, emoji='🎲')

    elif message.text.lower().startswith('pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    # elif message.text.lower() in ban_words:
    #     await  message.reply('This is bad word')
    #     await bot.delete_message(message.chat.id, message.message_id)


def register_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo_message, content_types=['text'])