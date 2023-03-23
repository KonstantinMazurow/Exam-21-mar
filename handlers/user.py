from aiogram import Dispatcher, types
from utils.parser_cat_img import get_pictures_cat
from utils.parser_btc import get_info_btc
from utils.get_time_now import get_time
from utils.parser_course_bank import get_exchange_rate
from utils.parser_top_films import get_top_movies
from utils.parser_joke import get_joke
from utils.parser_recept_food import get_random_recept_food
from utils.database_users import db1
from utils.get_random_stickers import get_random_sticker
from states.states import Game
from aiogram.dispatcher import FSMContext
import random


async def send_help(message: types.Message):
    await message.answer("""
        Command List:
        /time - Shows the current time
        /course - Shows the exchange rate
        /movies - Show top 10 movies
        /cat - Sends a random photo of a cat
        /sticker - Sends a random sticker
        /btc - Shows the cost of 1 bitcoin
        /game - Guess the number game
        /joke - Show random joke
        /sw - Developer details
        /registration - Register
        /food - Sends a random recipe
    """)


async def send_welcome(message: types.Message):
    await message.answer("""
        Hello. Enter a command. To display a list of commands, type /help
    """)


async def send_cat(message: types.Message):
    await message.answer(get_pictures_cat())


async def send_info_btc(message: types.Message):
    await message.answer(f'1 BTC = {get_info_btc()} USD')


async def send_time_now(message: types.Message):
    await message.answer(get_time()[0:8])


async def send_course(message: types.Message):
    await message.answer(get_exchange_rate())


async def send_top_movies(message: types.Message):
    for row in get_top_movies():
        await message.answer(row)


async def send_random_joke(message: types.Message):
    await message.answer(get_joke())


async def send_random_recept_food(message: types.Message):
    await message.answer(get_random_recept_food())


async def send_registration(message: types.Message):
    await message.answer("Congratulations, you are registered")
    db1.insert_user_id([message.from_user.id])


async def send_dev_info(message: types.Message):
    await message.answer("https://github.com/KonstantinMazurow")


async def send_random_sticker(message: types.Message):
    await message.answer_sticker(r'{0}'.format(get_random_sticker()))


async def start_message_game(message: types.Message):
    await Game.END.set()
    await message.answer('''
        Welcome to the game "Guess the number". I guessed a number from 0 to 10. You have 3 attempts. Good luck
    ''')
    global num, lives
    num = random.randint(1, 9)
    lives = 3
    await Game.END.set()


async def handle_game_end(message: types.Message, state: FSMContext):
    global num, lives
    answer = message.text
    if answer.isnumeric():
        if lives >= 1:
            if int(answer) == num:
                await message.answer("""
                🎉 Congratulations, you win!!! To play again, type /game
                """)
                await state.finish()
            else:
                lives -= 1
                await message.answer(f"""
                Sorry, think better You have {lives} lives
                """)
                await Game.END.set()
        elif lives == 0:
            await message.answer("Sorry, Yoy Loose! To play again, type /game")
            await state.finish()
    else:
        await message.answer("Sorry, type erorr")
        await Game.END.set()


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(send_help, commands=['help'])
    dp.register_message_handler(send_cat, commands=['cat'])
    dp.register_message_handler(send_info_btc, commands=['btc'])
    dp.register_message_handler(send_time_now, commands=['time'])
    dp.register_message_handler(send_course, commands=['course'])
    dp.register_message_handler(send_top_movies, commands=['movies'])
    dp.register_message_handler(send_random_joke, commands=['joke'])
    dp.register_message_handler(send_random_recept_food, commands=['food'])
    dp.register_message_handler(send_registration, commands=['registration'])
    dp.register_message_handler(send_dev_info, commands=['sw'])
    dp.register_message_handler(send_random_sticker, commands=['sticker'])
    dp.register_message_handler(start_message_game, commands=['game'])
    dp.register_message_handler(handle_game_end, state=Game.END)
