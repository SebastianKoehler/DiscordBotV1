import os
import asyncio
from dotenv import load_dotenv
from logic import bot_login, on_ready

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


async def main() -> None:
    await bot_login(TOKEN)
    await on_ready()


if __name__ == '__main__':
    asyncio.run(main())
