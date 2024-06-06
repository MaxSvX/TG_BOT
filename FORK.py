from uuid import uuid4

from aiogram import Bot, types, Dispatcher
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
from aiogram.utils.executor import Executor

import subprocess
import httpx, json

bot = Bot(token='6773330573:AAFIlZYa39KMGFtyJg_BJv4yvG-awTHCp_E')
dp = Dispatcher(bot)


# Функция-заглушка для получения списка валют

def translate(text):

    deeplx_api = "http://127.0.0.1:1188/translate"

    data = {
        "text": text,
        "source_lang": "EN",
        "target_lang": "RU"
    }

    post_data = json.dumps(data)
    r = httpx.post(url = deeplx_api, data = post_data).text
    return r

def create_inline_result(_title:str, text:str)->InlineQueryResultArticle:
    return InlineQueryResultArticle(
                id=str(uuid4()),
                title=_title,
                input_message_content=InputTextMessageContent(
                    message_text=text))

@dp.inline_handler()
async def inline_query_handler(inline_query: InlineQuery):
    query_text = inline_query.query
    print(query_text)
    if not query_text:
        # If no text is provided, display a list of currencies
        results = [
            create_inline_result("Введите текст", "Введите текст")
        ]
    else:
        results = [
            create_inline_result("Попугай", f'Попугай говорит: {query_text}: {translate(query_text)}')
        ]

    # else:
        # results = [
        #     create_inline_result("error", "error")
        # ]

    await bot.answer_inline_query(inline_query.id, results=results, cache_time=1)


if __name__ == '__main__':

    # p = subprocess.Popen(["deeplx_windows_amd64.exe"])

    executor = Executor(dp)
    executor.start_polling()
 
