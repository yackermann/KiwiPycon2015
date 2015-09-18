import os
import digitalocean as do

#Getting toke from the environment variables
token = os.getenv('DO_API_TOKEN', '')

#Getting DO manager
man = do.Manager(token=token)

# Pool Prefix
prefix = 'zergling'

droplets = {droplet.name: droplet for droplet in man.get_all_droplets()}
regions  = sorted([region.slug for region in man.get_all_regions()])
images   = { image.name : {
                'id': image.id, 
                'image': image 
            } for image in man.get_all_images() }

#Creating pool of vms
def createPool(quantity=47, region='sfo1'):
    for i in range( 0, quantity ):
        name = prefix + '.' + region + '.' + str(i)
        droplet = do.Droplet(token = token,
                             name  = name,
                             region = region, # def San Francisco 1
                             image = '13236931',
                             size_slug = '512mb', # Cheapest option
                             private_networking = True)
        droplet.create()
        print('Creating:', name)

#Getting pool status
def getPoolStatus(region='sfo1'):
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

def restartPool(region='sfo1'):
    for droplet in man.get_all_droplets():
        if prefix + '.' + region in droplet.name:
            try:
                droplet.reboot()
                print('restarting: ' + droplet.name)
            except:
                print('Can not destroy', droplet.name, 'Busy!')