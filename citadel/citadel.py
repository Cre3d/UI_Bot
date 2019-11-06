# citadel.py
import discord
import pickle as pk
import datetime as dt
from citadel.embeds import refueling
from citadel.embeds import modification

structures = []


def citadel(name, fuelconsuption, timetooffline, alertday):
    structures.append(
        {
            'name': name,
            'fuelConsuption': fuelconsuption,
            'timeToOffline': timetooffline,
            'alertDays': alertday
        }
    )
    return modification('Dodawanie nowej cytadeli...%s' % name, '', discord.Colour.green(), 'https://media.discordapp.net/attachments/547070445468516403/636510390066479134/Reprocess.png')


def addfuel(id: int, fuel: int):
    citadel = structures[id]
    sum = fuel/citadel['fuelConsuption']
    date = citadel['timeToOffline']
    newdate = date+dt.timedelta(days=sum)
    citadel['timeToOffline'] = newdate
    save()
    return refueling(citadel, date, newdate)


def delete(id: int):
    temp = structures[id]
    del structures[id]
    print("Deleting " + str(temp))
    save()
    return modification(temp, 'Deleting ', 'Usuwanie cytadeli', discord.Colour.red(), 'https://media.discordapp.net/attachments/547070445468516403/636510390066479134/Reprocess.png')


def load():
    database = open('datafile.pk1', 'rb')
    print("Loading...")
    return pk.load(database)


def save():
    database = open('datafile.pk1', 'wb')
    pk.dump(structures, database)
    print("Saving...")
    database.close()


citadel('Athanor111', 288, dt.date(year=2019, month=10, day=20), 5)
citadel('Raitaru222', 432, dt.date(year=2019, month=10, day=30), 5)
citadel('astrahus333', 180,dt.date(year=2019, month=11, day=30), 5)
citadel('astrahus444', 180, dt.date(year=2019, month=11, day=30), 5)
save()

structures = load()
#------------------
# Test examples
#
# structures('Athanor111', 288, datetime.date(year=2019, month=10, day=20), 5)
# structures('Raitaru222', 432, datetime.date(year=2019, month=10, day=30), 5)
# structures('astrahus333', 180, datetime.date(year=2019, month=11, day=30), 5)
# structures('astrahus444', 180, datetime.date(year=2019, month=11, day=30), 5)
# save()
#
#
# def show(citadel):
#     print()
#     print('Name: '+citadel['name'].upper())
#     print('Fuel Consuption: ',citadel['fuelConsuption'])
#     print('Offline Time: ',citadel['timeToOffline'])
#     print('Alert: ', citadel['timeToOffline']-datetime.timedelta(days=citadel['alertDays']))
#
#
# for citadel in cytki:
#     show(citadel)