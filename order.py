# commands.py
import discord
import pickle as pk
import datetime as dt
from citadel.embeds import modification

cmdlist = []


def addcmd(name, colour, url, description):
    embed = discord.Embed(
        title=name,
        colour=colour,
        url=url,
        description=description
    )
    name = {
        'title': name,
        'embed': embed
    }
    cmdlist.append(name)
    return modification('Dodawanie nowej komendy...%s' % name, '', discord.Colour.green(),
                        'https://media.discordapp.net/attachments/547070445468516403/636510390066479134/Reprocess.png')


def cmd(name):
    for cmd in cmdlist:
        if cmd['title'] == name:
            embed = cmd['embed']
        else:
            embed = modification('Nie znaleziono komendy', ' Komendy nie znaleziono w bazie danych, '
                                                           'sprawdź czy poprawnie wpisałeś komendę. Jeśli tak - skontaktuj się z administratorem.',
                                 discord.Colour.red(),
                                 'https://cdn.discordapp.com/attachments/547070445468516403/640965524179779624/aggression.png')
    return embed


def load():
    database = open('commandfile.pk1', 'rb')
    print("Loading commands...")
    return pk.load(database)


def save():
    database = open('commandfile.pk1', 'wb')
    pk.dump(cmdlist, database)
    print("Saving commands...")
    database.close()


addcmd(name='funkcja', colour=discord.Colour.blue(),
       url='https://res.cloudinary.com/lmn/image/upload/c_limit,h_360,w_640/e_sharpen:100/f_auto,fl_lossy,q_auto/v1/gameskinnyc/e/v/e/eve-alpha-omega-clone-icons-1500x844-d3793.jpg',
       description='Pierwsza przykladowa funkcja testowa')

addcmd(name='lorem', colour=discord.Colour.blue(),
       url='https://res.cloudinary.com/lmn/image/upload/c_limit,h_360,w_640/e_sharpen:100/f_auto,fl_lossy,q_auto/v1/gameskinnyc/e/v/e/eve-alpha-omega-clone-icons-1500x844-d3793.jpg',
       description='''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.''')

addcmd(name='test2', colour=discord.Colour.blue(),
       url='https://imageserver.eveonline.com/Render/22464_512.png',
       description=''' Opis statku
        
```[Flycatcher,Asana Akachi's Flycatcher]
Ballistic Control System II

5MN Quad LiF Restrained Microwarpdrive
1MN Monopropellant Enduring Afterburner
Fleeting Compact Stasis Webifier
Caldari Navy Medium Shield Extender
Faint Epsilon Scoped Warp Scrambler

Rocket Launcher II
Rocket Launcher II
Rocket Launcher II
Rocket Launcher II
Interdiction Sphere Launcher I
Rocket Launcher II
Rocket Launcher II
Rocket Launcher II

Small Anti-EM Screen Reinforcer II
Small Bay Loading Accelerator II

```''')

save()

cmdlist = load()

for cmd in cmdlist:
    if cmd == 'test0':
        print(cmd)
