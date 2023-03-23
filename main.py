import logging
from aiogram import executor
from globals import dp
from handlers import user
from utils.database_users import db1

db1.create_table_users_id()
logging.basicConfig(level=logging.INFO)
user.register_client_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
