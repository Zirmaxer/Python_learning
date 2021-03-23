import sys

my_folder = [ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py']
my_file = 'not this'
way = []
folder = []

def listsearch (mylist, filename):   
    way.append(mylist[0])
    size = len(mylist)
    i = 1
    while i < size:
        if type(mylist[i]) == str:
            print (mylist[i])
            if mylist[i] == filename:
                way.append(mylist[i])
                print ('We find the file!!!!!!!!!!!!!!!')
                return (way)
            else:
                i += 1
        elif type(mylist[i]) == list:
            print ('we have list here')
            listsearch (mylist[i], filename)
            i += 1
    return (way)

folder = listsearch (my_folder, my_file)
print (folder)