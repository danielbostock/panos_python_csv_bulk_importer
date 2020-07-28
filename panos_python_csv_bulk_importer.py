import csv
import warnings
import contextlib
import json
import panos_obj_importer, panos_pol_importer, panos_net_importer, import_builder
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




# Gather Device Info

location = import_builder.location()
hostname = import_builder.hostname()
key = import_builder.key()

# Define CSV File Importing
file = import_builder.selector()


######## 1.0 Tag Objects Importer ########
## update CSV 

print('''Palo Alto Tag Object Importer

Beginning the import...

        ''')

## Tag Object Importer

panos_obj_importer.tags(file, location, hostname, key)

print(''' 
Importing complete... 
''')

############


######## 2.0 Address Object Importer #######

print('''Palo Alto Address Object Importer

Beginning the import...
        ''')

## Open CSV
file = import_builder.selector()

## Tag Object Importer

panos_obj_importer.addrobj(file, location, hostname, key)

print(''' 
Importing complete... 
''')

######## 3.0 Address Groups Object Importer ######

print('''Palo Alto Address Group Object Importer
Beginning the import...
        ''')

## Open CSV
file = import_builder.selector()

## Tag Object Importer

panos_obj_importer.addrgrpobj(file, location, hostname, key)

print(''' 
Importing complete... 
''')

##### 3.1 Address Groups Object Importer Round 2 #####

print(''' Palo Alto Address Group Object Importer
Beginning the 2nd round import...
        ''')


## Open CSV
file = import_builder.selector()

## Tag Object Importer

panos_obj_importer.addrgrpobj(file, location, hostname, key)

print(''' 
2nd round of importing is complete... 
''')

##### 4.0 Service Object Importer #####

print(''' Palo Alto Service Object Importer
Beginning the import...
        ''')

## Open CSV
file = import_builder.selector()

## Tag Object Importer

panos_obj_importer.svcobj(file, location, hostname, key)

print(''' 
Importing complete... 
''')

##### 5.0 Service Object Group Importer #####

print(''' Palo Alto Service Group Object Importer
Beginning the import...
        ''')

## Open CSV
file = import_builder.selector()

## Tag Object Importer

panos_obj_importer.svcgrpobj(file, location, hostname, key)

print(''' 
Importing complete... 
''')

##### 5.1 Service Object Group Importer Round 2 #####

print(''' Palo Alto Service Group Object Importer
Beginning the 2nd round import...
        ''')

## Open CSV
file = import_builder.selector()

## Tag Object Importer

panos_obj_importer.svcgrpobj(file, location, hostname, key)

print(''' 
2nd round of importing is complete... 
''')