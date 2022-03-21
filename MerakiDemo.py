import meraki
import random
import sys

##################################################################################################
# Configrations
org_name='DevNet Sandbox'
my_org_key='????????????????????'

##################################################################################################
dashboard = meraki.DashboardAPI(my_org_key)
orgs = dashboard.organizations.getOrganizations()
org_names = [org['name'] for org in orgs]
index = org_names.index(org_name)
my_org = orgs[index]['id']
print('Org:\n')
print('Showing Details for Org {0} with ID {1} \n'.format(org_name, my_org))


##################################################################################################
print('Networks:\n')
# Get the current list of networks
current_networks = dashboard.organizations.getOrganizationNetworks(my_org)
# Get the current networks' names
network_names = [network['name'] for network in current_networks]
for name in network_names:
    netid = current_networks[network_names.index(name)]['id']
    print('The network {0} exists with ID {1}\n'.format(name, netid))


##################################################################################################

print('Unused devices:\n')
# show details of  unused device in inventory
# Return the inventory for an organization
inventory = dashboard.organizations.getOrganizationInventoryDevices(my_org)
# Filter out used devices already allocated to networks
unused = [device for device in inventory if device['networkId'] is None]
print('Found total of {0} unused devices in inventory\n'.format(len(unused)))
device_names = [device['name'] for device in unused]
for name in device_names:
    serial= unused[device_names.index(name)]['serial']
    print('The device {0} exists with serial {1}\n'.format(name, serial))