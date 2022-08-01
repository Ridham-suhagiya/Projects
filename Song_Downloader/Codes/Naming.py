
def filter(name):
    
    name = name.strip().split('/')[0]
    
    return name

def nameReading():
    with open('songs.txt') as songs:
        names = songs.readlines()
    names = list(map(filter,names))
    return names
