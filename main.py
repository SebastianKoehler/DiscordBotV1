import os
from dotenv import load_dotenv
from discord import Intents, Client


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
