import asyncio
import logging
import sys
from bot.handlers.handlers import cmd_start, echo_handler
from loader import dp, bot


async def main() -> None:
    dp.message.register(cmd_start)
    dp.message.register(echo_handler)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
