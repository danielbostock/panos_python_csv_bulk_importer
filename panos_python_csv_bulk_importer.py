import csv
import warnings
import contextlib
import json
import panos_obj_importer
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

################# PanOS Objects Bulk Importer ##################
## This script will POST all the following object groups to the
## the respective Palo. This script is not designed to deploy
## interface and network changes but simply for the purpose of
## getting bulk amount of objects from an exported CSV.
## 
## Refer to my website and GIT repo for further documentation
## and any further discussion on its respective purpose

## GitHub Repo: 



## Location & Input - Default is vsys1 and JSON input
api_loc = str(panos_obj_importer.panos_location())
api_input = str(panos_obj_importer.panos_inputformat())


## Gather Hostname & API Key
api_device_info = (panos_obj_importer.panos_device_info())
api_hostname= str(api_device_info[0])
api_key = str(api_device_info[1])

######## 1.0 Tag Objects Importer ########
## update CSV 

print(''' Palo Alto Tag Object Importer
Beginning the import...
        ''')

## Define CSV File Importing
csvfile = '/media/daniel/data/nextcloud/GIT/neverland-infrastructure/python/dev-panos/nvfw1_tagobj.csv'

## Open CSV
tags = csv.DictReader(open(csvfile))

## Tag Object Importer

panos_obj_importer.tagobject_importer(tags, api_hostname, api_key, api_loc, api_input)

print(''' 
Importing complete... 
''')

############


######## 2.0 Address Object Importer #######

print(''' Palo Alto Address Object Importer
Beginning the import...
        ''')

## Define CSV File Importing
csvfile = '/media/daniel/data/nextcloud/GIT/neverland-infrastructure/python/dev-panos/nvfw1_addrobj3.csv'

## Open CSV
addr = csv.DictReader(open(csvfile))

## Tag Object Importer

panos_obj_importer.addrobjects_importer(addr, api_hostname, api_key, api_loc, api_input)

print(''' 
Importing complete... 
''')



######## 3.0 Address Groups Object Importer ######

print(''' Palo Alto Address Group Object Importer
Beginning the import...
        ''')

## Define CSV File Importing
csvfile = '/media/daniel/data/nextcloud/GIT/neverland-infrastructure/python/dev-panos/nvfw1_addrobjgrp.csv'

## Open CSV
addrgrp = csv.DictReader(open(csvfile))

## Tag Object Importer

panos_obj_importer.addrgrpobjects_importer(addrgrp, api_hostname, api_key, api_loc, api_input)

print(''' 
Importing complete... 
''')

##### 3.1 Address Groups Object Importer Round 2 #####

print(''' Palo Alto Address Group Object Importer
Beginning the 2nd round import...
        ''')

## Define CSV File Importing
csvfile = '/media/daniel/data/nextcloud/GIT/neverland-infrastructure/python/dev-panos/nvfw1_addrobjgrp.csv'

## Open CSV
addrgrp = csv.DictReader(open(csvfile))

## Tag Object Importer

panos_obj_importer.addrgrpobjects_importer(addrgrp, api_hostname, api_key, api_loc, api_input)

print(''' 
2nd round importing complete... 
''')

##### 4.0 Service Object Importer #####

print(''' Palo Alto Service Object Importer
Beginning the import...
        ''')

## Define CSV File Importing
csvfile = '/media/daniel/data/nextcloud/GIT/neverland-infrastructure/python/dev-panos/nvfw1_svcobj.csv'

## Open CSV
svc = csv.DictReader(open(csvfile))

## Tag Object Importer

panos_obj_importer.svcobjects_importer(svc, api_hostname, api_key, api_loc, api_input)

print(''' 
Importing complete... 
''')

##### 5.0 Service Object Importer #####

print(''' Palo Alto Service Group Object Importer
Beginning the import...
        ''')

## Define CSV File Importing
csvfile = '/media/daniel/data/nextcloud/GIT/neverland-infrastructure/python/dev-panos/nvfw1_svcgrpobj.csv'

## Open CSV
svcgrp = csv.DictReader(open(csvfile))

## Tag Object Importer

panos_obj_importer.svcgrpobjects_importer(svcgrp, api_hostname, api_key, api_loc, api_input)

print(''' 
Importing complete... 
''')