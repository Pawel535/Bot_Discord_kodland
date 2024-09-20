import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

questions_answers = {
    "jakie jest najpopularniejsze język programowania?": "Python",
    "ile jest 2 + 2?": "4",
    "jak masz na imię?": "Jestem botem i nie mam imienia :)"
}

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pytanie(ctx, *, question):
    question_lower = question.lower()
    if question_lower in questions_answers:
        answer = questions_answers[question_lower]
        await ctx.send(f'Odpowiedź: {answer}')
    else:
        await ctx.send("Nie znam odpowiedzi na to pytanie. Jak powinna brzmieć odpowiedź?")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            response = await bot.wait_for('message', check=check, timeout=30.0)
            questions_answers[question_lower] = response.content
            await ctx.send(f"Dziękuję! Zapisano odpowiedź: {response.content}")
        except discord.errors.TimeoutError:
            await ctx.send("Nie otrzymałem odpowiedzi. Pytanie nie zostało zapisane.")

bot.run("Token")
