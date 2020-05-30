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


## 1.0 Security Policy Importer

def secpol_importer(secpol, api_hostname, api_key, api_loc, api_input):
    ## vars used to build the payload ##
    panos_api_objname = '&name='
    panos_api_objtype = '/restapi/9.0/Objects/SecurityRules?'
    panos_api_hostname = str(api_hostname)
    panos_api_key = str(api_key)
    panos_api_loc = str(api_loc)
    panos_api_input = str(api_input)
    ####################################

    ## Create Security Policy Rules
    for row in tags:

        ## Security Policy Rule - General
        api_pol_payload_name = row["Name"]
        api_pol_payload_desc = row["Description"]
        api_pol_payload_tags = row["Tags"]
        api_pol_payload_grptag = row["Group"]
        api_pol_payload_rtype = row["Type"]

        ## Security Policey Rule - Source
        api_pol_payload_srczone = row["Source Zone"]
        api_pol_payload_srcaddr = row["Source Address"]
        
        ## Security Police Rule - User
        api_pol_payload_srcusr = row["Source User"]
        api_pol_payload_hipprf = row["Source HIP Profile"]

        ## Security Policy Rule - Destination
        api_pol_payload_dstzone = row["Destination Zone"]
        api_pol_payload_dstaddr = row["Destination Address"]
        
        ## Security Policy Rule - Application
        api_pol_payload_app = row["Application"]


        ## Security Policy Rule - Service/URL Category
        api_pol_payload_svc = row["Service"]
        api_pol_payload_urlcat = row["URL Category"]


        ## Security Policy Rule - Actions
        api_pol_payload_action = row["Action"]
        #api_pol_payload_sched = row["Schedule"] PLACEHOLDER
        #api_pol_payload_log = row["Log Profile"] PLACEHOLDER
        api_pol_payload_prfset = row["Profile"]
        #api_pol_payload_qosdscp = row["QOS Ip-Dscp"] PLACEHOLDER
        #api_pol_payload_qosipprec = row["QOS IP-Precedence"] PLACEHOLDER
        
        ## Log option variable handler
        if 'Traffic log sent at session end' in row["Options"]:
            api_pol_payload_logstart = 'yes'
        if 'Traffic log sent at session start' in row["Options"]:
            api_pol_payload_logend = 'yes'
        if 'Traffic log sent at session start, and at session end' in row["Options"]:
            api_pol_payload_logstart = 'yes'
            api_pol_payload_logend = 'yes'
        if "" in row ["Options"]:
            api_pol_payload_logstart = 'no'
            api_pol_payload_logend = 'no'
        

        ## From all vars above, the Payload (AKA: Body) will built and that will be sent with API Request to deploy the changes
        payload = {
                    "entry": {
                        "@name": api_pol_payload_name,
                        "from": {
                        "member": api_pol_payload_srczone
                        },
                        "to": {
                        "member": api_pol_payload_dstzone 
                        },
                        "source": {
                        "member": api_pol_payload_srcaddr
                        },
                        "source-user": {
                        "member": api_pol_payload_srcusr
                        },
                        "destination": {
                        "member": api_pol_payload_dstaddr
                        },
                        "service": {
                        "member": api_pol_payload_svc
                        },
                        "category": {
                        "member": api_pol_payload_urlcat
                        },
                        "application": {
                        "member": api_pol_payload_app
                        },
                        "tag": {
                        "member": api_pol_payload_tags
                        },
                        "negate-source": "yes",
                        "negate-destination": "yes",
                        "disabled": "yes",
                        "description": api_pol_payload_desc,
                        "group-tag": api_pol_payload_grptag,
                        "hip-profiles": {
                        "member": api_pol_payload_hipprf
                        },
                        "action": api_pol_payload_action,
                        "icmp-unreachable": "yes",
                        "rule-type": api_pol_payload_rtype,
                        "option": {
                        "disable-server-response-inspection": "yes"
                        },
                        "log-setting": "None",
                        "log-start": api_pol_payload_logstart,
                        "log-end": api_pol_payload_logend,
                        "profile-setting": {
                        "group": {
                            "member": api_pol_payload_prfset
                        }
                        }
                    }
                }

        ## Build API call URL and make API HTTPS Requests call        
        url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_pol_payload_name + panos_api_input
        response = requests.request("POST", url, data = json.dumps(payload), verify = False)

        ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
        print("Security Policy: ", api_pol_payload_name, "| Description: ", api_pol_payload_desc)
        print("API Call URL: ", url)
        print("API Response Code: ", response.text.encode('utf8'))
        print("JSON Body: ", json.dumps(payload))
        print(''' 
                
            ''')