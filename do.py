import os
import digitalocean as do

#Getting toke from the environment variables
token = os.getenv('DO_API_TOKEN', '')

#Getting DO manager
man = do.Manager(token=token)

#Creating pool of vms
def createPool():
    for i in range( 0, 25 ):
        name = 'insanity.' + str(i)
        droplet = do.Droplet(token = token,
                             name  = name,
                             region = 'sfo1', # San Francisco 1
                             image = 'ubuntu-14-04-x64',
                             size_slug = '512mb', # Cheapest option
                             backups = False)
        droplet.create()
        print('Creating:', name)

#Getting pool status
def getDropletsStatus():
    for droplet in man.get_all_droplets():
        if 'insanity.' in droplet.name:
            print(droplet.name, droplet.status)

def destroyPool():
    for droplet in man.get_all_droplets():
        if 'insanity.' in droplet.name:
            droplet.destroy()
            print('Destroying: ' + droplet.name)