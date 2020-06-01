import csv
import warnings
import contextlib
import json
import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

## Function definitions used by other functions for building API call

def panos_location ():
    panos_device_location = '&location=vsys&vsys=vsys1'
    panos_api_location = panos_device_location
    return panos_api_location

def panos_inputformat ():
    panos_device_inputformat = '&input-format=json'
    panos_api_inputformat = panos_device_inputformat
    return panos_api_inputformat

def panos_device_info ():
    panos_device_hostname = str(input('Enter the device URL or IP:'))
    panos_device_key = str("key=" + input('Enter the API key:'))
    return panos_device_hostname, panos_device_key
    
#######################################################################


def netzone_importer(tags, api_hostname, api_key, api_loc, api_input):
    ## vars used to build the payload ##
    panos_api_objname = '&name='
    panos_api_objtype = '/https://10.0.13.24/restapi-doc/restapi/v9.1/Network/Zones'
    panos_api_hostname = str(api_hostname)
    panos_api_key = str(api_key)
    panos_api_loc = str(api_loc)
    panos_api_input = str(api_input)
    ####################################

    ## Create Tag objects
    for row in tags:
        api_obj_payload_name = row["Name"]
        api_obj_payload_comm = row["Comments"]
        print("Tag Name:", api_obj_payload_name, "| Comments:", api_obj_payload_comm)
        payload = {
                    "entry": {
                        "@name": api_obj_payload_name,
                        "comments": api_obj_payload_comm
                            }
                    }

        ## Build API call URL and make API HTTPS Requests call        
        url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
        response = requests.request("POST", url, data = json.dumps(payload), verify = False)

        ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
        print("Tags: ", api_obj_payload_name, "| Description: ", api_obj_payload_comm)
        print("API Call URL: ", url)
        print("API Response Code: ", response.text.encode('utf8'))
        print("JSON Body: ", json.dumps(payload))
        print(''' 
                
            ''')
