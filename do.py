import os
import digitalocean as do

#Getting toke from the environment variables
token = os.getenv('DO_API_TOKEN', '')

#Getting DO manager
man = do.Manager(token=token)

prefix = 'zergling'
#Creating pool of vms
def createPool(quantity=40, region='sfo1'):
    for i in range( 0, quantity ):
        name = prefix + '.' + region + '.' + str(i)
        droplet = do.Droplet(token = token,
                             name  = name,
                             region = region, # San Francisco 1
                             image = 13232378,
                             size_slug = '512mb', # Cheapest option
                             private_networking = True)
        droplet.create()
        print('Creating:', name)

#Getting pool status
def getDropletsStatus(region='sfo1'):
    for droplet in man.get_all_droplets():
        if prefix + '.' + region in droplet.name:
            print(droplet.name, droplet.status)

def destroyPool(region='sfo1'):
    for droplet in man.get_all_droplets():
        if prefix + '.' + region in droplet.name:
            try:
                droplet.destroy()
                print('Destroying: ' + droplet.name)
            except:
                print('Can not destroy', droplet.name, 'Busy!')
