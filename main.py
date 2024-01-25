import asyncio
import logging
import sys
from bot.handlers.registration_handlers import command_reg
from bot.handlers.handlers import cmd_start, echo_handler
from loader import dp, bot


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
