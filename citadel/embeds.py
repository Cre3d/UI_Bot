# embeds.py
import discord
import datetime


def show(citadel):
    embed = discord.Embed(
        title= citadel['name'].upper(),
        description='Fuel Consumption: '+str(citadel['fuelConsuption'])
        +'\nTime to offline: '+str(citadel['timeToOffline'])
        +'\nAlert: '+str(citadel['timeToOffline']-datetime.timedelta(days=citadel['alertDays'])),
        colour=discord.Colour.blue()
    )
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/547070445468516403/636336571741765670/unknown.png')
    return embed


def refueling(citadel, date, newdate):
    embed = discord.Embed(
        title='Refueling citadel %s' % citadel['name'].upper(),
        description='Old date: '+str(date)+'\nNew date: '+str(newdate),
        colour=discord.Colour.green()
    )
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/547070445468516403/636501655885447168/fuel.png')
    return embed

def modification(citadel, title, description, colour, url):
    embed = discord.Embed(
        title=title+str(citadel['name']),
        description=description,
        colour=colour
    )
    embed.set_thumbnail(url=url)
    return embed


def modification(title, description, colour, url):
    embed = discord.Embed(
        title=title,
        description=description,
        colour=colour
    )
    embed.set_thumbnail(url=url)
    return embed

