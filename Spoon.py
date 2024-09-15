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


# Обработчик инлайн-запросов
@dp.inline_handler()
async def inline_query(inline_query: InlineQuery):

    text = inline_query.query or "0"
    text = " ".join(text.split())
    result = calculate(to_poland(text))

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

def to_poland(token: str)->str:
    tokenNumber= re.findall(r'\b\d+\.?\d*\b', token)
    tokenOperator = re.findall(r'\+|\*|\/|-', token)
    ans=[]
    stack=[]
    if len(tokenNumber) - len(tokenOperator) != 1:
        return "Error"
    ans.append(tokenNumber[0])
    for i in range(len(tokenOperator)):
      ans.append(tokenNumber[i+1])
      stack.append(tokenOperator[i]) 
      if tokenOperator[i] == '*' or tokenOperator[i] == '/':
        while stack:
            ans.append(stack.pop())
    while stack:
            ans.append(stack.pop())

    return " ".join(ans)






# 3 5 6 * - 2 + 3 2 * +
# 3 30 -2 + 3 2 * +
# - 27 2 + 3 2 * + 
# - 25 3 2 * +
# - 25 6 +
# - 19 
def is_number(s)-> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def calculate(example:str)-> int | float:
    stack = []
    for i in example.split():
        if is_number(i):
            stack.append(float(i))
        else:
            a1 = stack.pop()
            a2 = stack.pop()
            if i == "+":
                stack.append(a2 + a1)
            elif i == "-":
                stack.append(a2 - a1)
            elif i == "*":
                stack.append(a2 * a1)
            elif i == "/":
                if a1 == 0:
                    raise Exception("Деление на 0")
                stack.append(a2 / a1)

    return stack.pop()# todo добавить проверку на стек из 1 элемент

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
