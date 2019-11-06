import datetime
import asyncio

cytki = []


def addfuel(ctx, id, fuel):
    citadel = cytki[id]
    temp = fuel / citadel['fuelConsuption']
    date = citadel['timeToOffline']
    citadel['timeToOffline'] = datetime.timedelta(days=temp)+date
    asyncio.create_task(ctx.send('Refueling citadel'))
    asyncio.create_task(ctx.send('Name: '+cytki[id]['name']))

def delete(id: int):
     del cytki[id]
     save(cytki)


# def show(citadel):
#     print()
#     print('Name: '+citadel['name'].upper())
#     print('Fuel Consuption: ',citadel['fuelConsuption'])
#     print('Offline Time: ',citadel['timeToOffline'])
#     print('Alert: ', citadel['timeToOffline']-datetime.timedelta(days=citadel['alertDays']))


def structures(name, fuelConsuption, timeToOffline, alertDays):
    cytki.append({'name': name, 'fuelConsuption': fuelConsuption,
                   'timeToOffline': timeToOffline, 'alertDays': alertDays})


def save(cytki):
    myfile = open('datafile.pk1', 'wb')
    import pickle
    pickle.dump(cytki, myfile)
    myfile.close()
    print("Wykonano Poprawnie")

# structures('Athanor111', 288, datetime.date(year=2019, month=10, day=20), 5)
# structures('Raitaru222', 432, datetime.date(year=2019, month=10, day=30), 5)
# structures('astrahus333', 180, datetime.date(year=2019, month=11, day=30), 5)
# structures('astrahus444', 180, datetime.date(year=2019, month=11, day=30), 5)
# save(cytki)

def load():
    myfile = open('datafile.pk1', 'rb')
    import pickle
    return pickle.load(myfile)

cytki = load()

#
# for citadel in cytki:
#     show(citadel)
