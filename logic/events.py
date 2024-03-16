from discord import Intents, Client

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


async def bot_login(token: str) -> None:
    await client.start(token=token)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')
