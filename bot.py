# bot.py
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
import datetime
import asyncio
import discord
import citadel.citadel
import citadel.embeds
import order

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
id = 547070445468516403


# channel = bot.get_channel(id)


class MyCog(commands.Cog):
    def __init__(self):
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(self.index)
        self.index += 1
    # asyncio.create_task(discord.User.send('Zapisywanie...'))


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name='Radczu to pedał'))


@bot.command(name='test', help='Test help')
async def test(ctx, *args):
    desc = ''
    for arg in args:
        desc = desc +' '+ arg
    await ctx.send(desc)


@bot.command(name='save', help='Zapis wszystkich cytadel do bazydanych.')
async def save(ctx):
    citadel.save()
    await ctx.send('Save Completed!')




def saveprocess(ctx, name, fuelConsuption, timeToOffline, alertDays):
    citadel.structures(name, fuelConsuption, timeToOffline, alertDays)
    asyncio.create_task(ctx.send('Zapisywanie...'))
    citadel.save(citadel.structures)


## ok
@bot.command(name='cmd', help='Wyswietl komende')
async def cmd(ctx, name):
    embed = discord.Embed()
    for cmd in order.cmdlist:
        if cmd['title'] == name:
            embed = cmd['embed']
        else:
            embed = discord.Embed(
                title='Nie znaleziono komendy',
                description= 'Komendy nie znaleziono w bazie danych, sprawdź czy poprawnie wpisałeś komendę. Jeśli tak - skontaktuj się z administratorem.',
                colour=discord.Colour.red(),
                url='https://cdn.discordapp.com/attachments/547070445468516403/640965524179779624/aggression.png')
    await ctx.send(embed=embed)


@bot.command(name='addinfo', help='Dodaj nową komendę tekstową')
async def addinfo(ctx, name, colour, url, *args):
    name = name
    description = ''
    for arg in args:
        description = description + ' ' + arg
    if colour == 'zielony':
        colour = discord.Colour.green()
    else:
        colour = discord.Colour.red()
    url = url
    embed = citadel.embeds.modification(title='Dodano nową komendę %2s' % name,
                                        description=description, colour=colour, url=url)
    await ctx.send(embed=embed)



@bot.command(name='addcitadel', help='Dodaj nową cytadelę (year month day - data offline) ')
async def addcitadel(ctx, name, fuel: int, year: int, month: int, day: int):
    timeToOffline = datetime.date(year=year, month=month, day=day)
    alertDays = 5
    embed = citadel.citadel.citadel(name, fuel, timeToOffline, alertDays)
    await ctx.send(embed=embed)


@bot.command(name='delete', help='Usuń cytadelę !del ID')
async def delete(ctx, id: int):
    embed = citadel.citadel.delete(id)
    await ctx.send(embed=embed)


@bot.command(name='refuel', help='Refueling citadel')
async def refuel(ctx, id: int, volume: int):
    embed = citadel.citadel.addfuel(id, volume)
    await ctx.send(embed=embed)


@bot.command(name='show', help='Show all citadel')
async def show(ctx):
    i = 0
    for x in citadel.citadel.structures:
        embed = citadel.embeds.show(x)
        embed.set_footer(text='Citadel ID: %2d' % i)
        i += 1
        await ctx.send(embed=embed)


bot.add_cog(MyCog())
bot.run(token)
