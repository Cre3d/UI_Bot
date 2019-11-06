cmdlist = []

def addcmd(name, arg):
    name = {
        'title' : name,
        'arg' : arg
    }
    cmdlist.append(name)

addcmd('lorem','It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout')
addcmd('ipsum','There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour')
addcmd('discord','The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33')

for cmd in cmdlist:
    if cmd['title'] == 'lorem':
        print(cmd['arg'])
