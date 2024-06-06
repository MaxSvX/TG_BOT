from uuid import uuid4

from aiogram import Bot, types, Dispatcher
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
from aiogram.utils.executor import Executor




bot = Bot(token='6773330573:AAFIlZYa39KMGFtyJg_BJv4yvG-awTHCp_E')
dp = Dispatcher(bot)


# Функция-заглушка для получения списка валют



@dp.inline_handler()
async def inline_query_handler(inline_query: InlineQuery):
    query_text = inline_query.query
    print(query_text)
    if not query_text:
        # If no text is provided, display a list of currencies
        results = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title='бла блa бла бла бла бла',
                input_message_content=InputTextMessageContent(
                    message_text='Бла бла бла')
                                     )
        ]

    else:
        results = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title='ERROR',
                input_message_content=InputTextMessageContent(
                    message_text='ERROR')
                                     )
        ]

    await bot.answer_inline_query(inline_query.id, results=results, cache_time=1)


if __name__ == '__main__':
    executor = Executor(dp)
    executor.start_polling()
 
