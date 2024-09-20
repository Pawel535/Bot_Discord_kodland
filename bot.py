import discord
from bot_logic import gen_pass, coin_toss, random_emoji

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$haslo'):
        await message.channel.send(f"{gen_pass(10)}")
    elif message.content.startswith('$coin'):
        await message.channel.send(f"{coin_toss()}")
    elif message.content.startswith('$random_emoji'):
        await message.channel.send(f"{random_emoji()}")
    else:
        await message.channel.send(message.content)

client.run("TOKEN")