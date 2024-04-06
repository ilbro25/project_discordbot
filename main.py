import random
import discord 
from discord.ext import commands
from funcions import *
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def pass_gen(lenpassword):
    elements = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,/_-=+?!@#$%^&*()"
    password = ""
    for i in range(lenpassword):
        password += random.choice(elements)
    return password


def coinflip():
    flip = random.randint(0,1)
    if flip == 0:
        return "Решка"
    else:
        return "Орёл"


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Пока')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def password(ctx, count = 10):
    await ctx.send(f'Ваш пароль - {pass_gen(count)}')

@bot.command()
async def coin(ctx):
    await ctx.send(f'{coinflip()}')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def helpme(ctx):
    await ctx.send(f'''
                   Все команды вводятся без скобок!!!
/hello
/bye
/coin - подбрасывает монетку
/heh (n) - выводит 'he' n-ое количество раз
/add (число1) (число2) - складывает 2 числа
/repeat (n) (текст) - повторяет текст n-ое количество раз
/password (n) - генерация пароля с n-ым количеством символов
/roll (n)d(b) - выводит рандомные числа 1-b количество раз n
                   ''')
    
@bot.command()
async def news(ctx, count = 3):
    for i in range(count):
        await ctx.send(f'''
{DataFrame()['news'][i]}
Ссылка: {DataFrame()['links'][i]}
Дата публикации: {DataFrame()['date'][i]}. Просмотры: {DataFrame()['views'][i]}

''')

    

bot.run("TOKEN")
