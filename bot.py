import discord
from discord.ext import commands, tasks
import random

intents = discord.Intents.default()
intents.message_content = True
ID_CHANNEL = 1284169325518782519
bot = commands.Bot(command_prefix='!', intents=intents)

smieci_info = {
    "niebieski": "służą do składowania papieru. Do koszów w kolorze niebieskim można wrzucać czasopisma, gazety, książki, zeszyty, papierowe torby, opakowania papierowe, kartony.",
    "zielone": "do nich należy wrzucać szkło. Znajdziemy w nich szklane pojemniki po kosmetykach, słoiki, butelki. Pod żadnym pozorem nie wolno wrzucać do zielonych pojemników szkła żaroodpornego czy pojemników szklanych, które nierozerwalnie połączone są z innymi materiałami.",
    "żółte": "służą do składowania metalu i innych tworzyw sztucznych. Możemy do nich wrzucać plastikowe opakowania, foliowe torebki, opakowania wielomateriałowe, takie jak kartony po mleku. Co więcej, w takim pojemniku jest miejsce na plastikowe butelki wraz z nakrętkami, kapsle, puszki, folię aluminiową czy metalowe nakrętki.",
    "brązowe": "dedykowane są odpadom biodegradowalnym, biologicznym. W takich koszach znaleźć się powinny resztki jedzenia, ale także odpady zielone, czyli liście, kora, resztki roślin, niemalowane drewno i wiele więcej.",
    "czarne": "służą do składowania odpadów mieszanych. Do nich trzeba wrzucać odpady skórzane, ubrania, obuwie, odchody zwierząt, zepsute naczynia, zużyte chusteczki, ręczniki papierowe, waciki, patyczki do uszu czy podpaski."
}
porady = [
    "Zakręć kran podczas mycia zębów, aby oszczędzać wodę.",
    "Używaj toreb wielokrotnego użytku zamiast plastikowych.",
    "Zrezygnuj z jednorazowych produktów i zastąp je trwałymi alternatywami.",
    "Zgaś światło, kiedy wychodzisz z pokoju.",
    "Przełącz się na energooszczędne żarówki LED.",
    "Kupuj lokalne produkty, aby zmniejszyć ślad węglowy transportu.",
    "Oszczędzaj energię, odłączając urządzenia, gdy ich nie używasz.",
    "Kompostuj resztki jedzenia, aby zmniejszyć ilość odpadów.",
    "Przejedź rowerem lub chodź pieszo, zamiast korzystać z samochodu na krótkich dystansach.",
    "Używaj bidonu zamiast kupować butelki z wodą jednorazowego użytku.",
    "Uprawiaj rośliny w domu, aby poprawić jakość powietrza."
]

kolory = smieci_info.keys()

def random_kolor():
    return random.choice(list(kolory))

@bot.command()
async def segregacja(ctx, wybrany_kolor=''):
    if wybrany_kolor == '':
        wybrany_kolor = random_kolor()
    if wybrany_kolor in smieci_info:
        await ctx.send(f'Do koszy o kolorze {wybrany_kolor} wrzucamy: {smieci_info[wybrany_kolor]}')
    else:
        await ctx.send("Nieznany kolor kosza. Dostępne kolory to: niebieski, zielone, żółte, brązowe, czarne.")

@tasks.loop(seconds=30)
async def wysylaj_porady():
    kanal = bot.get_channel(ID_CHANNEL)
    if kanal is not None:
        porada = random.choice(porady)
        await kanal.send(f'Porada dotycząca pomocy planecie: {porada}')

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')
    wysylaj_porady.start()
    
bot.run("TOKEN")
