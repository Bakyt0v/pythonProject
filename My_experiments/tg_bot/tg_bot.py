from aiogram import executor
from config import dp
import cilent, callback, extra

cilent.refister_handlers_cilent(dp)
callback.register_handlers_callback(dp)
extra.register_handler_extra(dp)











if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)