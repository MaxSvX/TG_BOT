import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
import re
import os
API_TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TG BOT")
logger.setLevel(logging.INFO)
# Инициализация бота и диспетчера
bot = Bot(token='6773330573:AAFIlZYa39KMGFtyJg_BJv4yvG-awTHCp_E')
dp = Dispatcher(bot)

# Функция для вычисления результата
def calculate(expression:str):
    spisok = [f'{i}'for i in range(10)]
    spisok += [' ', '.', '/', '*', '!', '=', '+', '-', '(', ')']
    try:
        for i in expression:
            if i not in spisok:
                return "!!!Ошибка: в примере не должно быть букв!!!"

        return str(eval(expression))
    except:
        return "Ошибка"

# Обработчик инлайн-запросов
@dp.inline_handler()
async def inline_query(inline_query: InlineQuery):

    text = inline_query.query or "0"
    text = " ".join(text.split())
    result = calculate(text)
    logger.debug(f"Запрос:{text} Результат:{result}")

    item = InlineQueryResultArticle(
        id='1',
        title=f'Результат: {result}',
        input_message_content=InputTextMessageContent(f"{text} = {result}"),
        description=f'{text} = {result}'
    )
    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)

# Обработчик обычных сообщений
# @dp.message_handler(regexp=r'^[\d\+\-\*/\(\)\.\s]+$')
# async def handle_message(message: types.Message):
#     expression = message.text
#     result = calculate(expression)
#     await message.reply(f"{expression} = {result}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)