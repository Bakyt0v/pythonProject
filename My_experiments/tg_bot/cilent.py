from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
import buttonss


async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello i am the new bot from master {message.from_user.full_name}, if u wanna see all the commands just text /help ',
                           reply_markup=buttonss.keyboard_stat)

async def help(message: types.Message):
    await bot.send_message(message.chat.id, f'/help-- to see all commands \n'
                                            f'/start-- to see info about pythot \n'
                                            f'/quiz-- to see example quiz\n'
                                            f'/problem-- to se e class work tasks\n'
                                            f'/solve_task-- to see home work 1 from student {message.from_user.full_name}\n'
                                            f'/home_work_2-- to see home work 2 from student {message.from_user.full_name}',
                                            reply_markup=buttonss.keyboard_stat,)


async def poll(message: types.Message):
    question = 'By whom invented Python'
    answer = ['Harry Potter', 'Piter', 'Amantur', 'Aktan']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=10,
                        explanation='You are looser',
                        explanation_parse_mode=ParseMode.MARKDOWN_V2,
                        )



async def problem(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Next task', callback_data='button_call_1')
    markup.add(button_call_1)
    photo = open('../media/summfloatinteger.jpg', 'rb')
    answer1 = ['0.0', '4', '5', '8.0', 'Error']
    question1 = 'Output of this task in picture above'
    await bot.send_photo(
        message.chat.id,
        photo=photo)

    await bot.send_poll(
        message.chat.id,
        question = question1,
        options=answer1,
        correct_option_id=0,
        is_anonymous=False,
        type='quiz',
        open_period=20,
        reply_markup=markup,
        explanation = 'It is so easy so you have only 20 seconds',
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


markup0 = InlineKeyboardMarkup()
button1 = InlineKeyboardButton('It is easy to me', callback_data='button1')
button2 = InlineKeyboardButton('It is so hard to me', callback_data='button2')
button3 = InlineKeyboardButton('i am tired i just wanna see the result', callback_data='button3')
button4 = InlineKeyboardButton('Tasks for lazy HUMANs', callback_data='button4')

markup0.add(button1,button2,button3,button4)

async def process_start_command(message: types.Message):
    photo_1 = open('../media/home_work_solved/task1.png', 'rb')
    await bot.send_photo(
        message.chat.id,
        photo=photo_1
    )
    await bot.send_message(message.chat.id,'Could you solve the task above in picture?',
                           reply_markup=markup0)


async def home_work2(message: types.Message):
    photo_hw2 = open('../media/home_work2/hw2.png', 'rb')
    markup_hw = InlineKeyboardMarkup()
    button_home_work2 = InlineKeyboardButton('Я смог решить домашку', callback_data='button_home_work2')
    button_home_work2_2 = InlineKeyboardButton('Я не смог решить домашку', callback_data='button_home_work_2')
    markup_hw.add(button_home_work2, button_home_work2_2)
    await bot.send_photo(
        message.chat.id,
        photo=photo_hw2
    )
    await bot.send_message(message.chat.id, 'Домашнее задание 2',
                           reply_markup=markup_hw)




    # else:
    #     await message.answer(message.text)

def refister_handlers_cilent(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(poll, commands=['quiz'])
    dp.register_message_handler(problem, commands=['problem'])
    dp.register_message_handler(process_start_command, commands=['solve_task'])
    dp.register_message_handler(home_work2, commands=['home_work_2'])
