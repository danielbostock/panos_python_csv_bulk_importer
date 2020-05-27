import csv
import warnings
import contextlib
import json
import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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
    

## 1.0 Tag Objects Importer

def tagobject_importer(tags, api_hostname, api_key, api_loc, api_input):
    panos_api_objname = '&name='
    panos_api_objtype = '/restapi/9.0/Objects/Tags?'
    panos_api_hostname = str(api_hostname)
    panos_api_key = str(api_key)
    panos_api_loc = str(api_loc)
    panos_api_input = str(api_input)
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
        url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
        response = requests.request("POST", url, data = json.dumps(payload), verify = False)
        print(response.text.encode('utf8'))


## 2.0 Address Objects Importer

# Address Object Import Loop

def addrobjects_importer(addr, api_hostname, api_key, api_loc, api_input):
    ## vars used to build the payload ##
    panos_api_objname = '&name='
    panos_api_objtype = '/restapi/9.0/Objects/Addresses?'
    panos_api_hostname = str(api_hostname)
    panos_api_key = str(api_key)
    panos_api_loc = str(api_loc)
    panos_api_input = str(api_input)
    ####################################
    for row in addr:
        api_obj_payload_ip = row["Address"]
        api_obj_payload_name = row["Name"]
        api_obj_payload_desc = row["Description"]
        if "" in row["Tags"]:
            payload = {
                        "entry": {
                            "@name": api_obj_payload_name,
                            "description": api_obj_payload_desc,
                            "ip-netmask": api_obj_payload_ip,
                        }
                }
        elif " " in row["Tags"]:
            payload = {
                        "entry": {
                            "@name": api_obj_payload_name,
                            "description": api_obj_payload_desc,
                            "ip-netmask": api_obj_payload_ip,
                        }
                }
        else:
            addrobj_payload_tags = row["Tags"].split(";")
            payload = {
                        "entry": {
                            "@name": api_obj_payload_name,
                            "description": api_obj_payload_desc,
                            "ip-netmask": api_obj_payload_ip,
                            "tag": {
                            "member":  
                            addrobj_payload_tags
                            }
                        }
                }
        print("Object Name:",api_obj_payload_name,"| IP: ", api_obj_payload_ip, "| Description: ", api_obj_payload_desc)
        url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
        response = requests.request("POST", url, data = json.dumps(payload), verify = False)
        print(response.text.encode('utf8'))
        print(json.dumps(payload))


## 3.0 Address Groups Object Importer

## Address Object Import Loop

def addrgrpobjects_importer(addrgrp, api_hostname, api_key, api_loc, api_input):
    ## vars used to build the payload ##
    panos_api_objname = '&name='
    panos_api_objtype = '/restapi/9.0/Objects/AddressGroups?'
    panos_api_hostname = str(api_hostname)
    panos_api_key = str(api_key)
    panos_api_loc = str(api_loc)
    panos_api_input = str(api_input)
    ####################################
    for row in addrgrp:
        if 'dynamic' in row["Type"]:
            print(''' 
            Deploying Dynamic Group...
            ''')
            api_obj_payload_name = row["Name"]
            api_obj_payload_desc = row["Description"]
            api_obj_payload_grpfilter = row["Addresses"]
            if "" in row["Tags"]:
                        payload = {
                        "entry": {
                            "@name": api_obj_payload_name,
                            "description": api_obj_payload_desc,
                            "dynamic": {
                                "filter": api_obj_payload_grpfilter
                                }
                        }
                    }
            else :
                api_obj_payload_tags = row["Tags"].split(";")
                payload = {
                            "entry": {
                                "@name": api_obj_payload_name,
                                "description": api_obj_payload_desc,
                                "dynamic": {
                                    "filter": api_obj_payload_grpfilter
                                    },
                                    "tag": {
                                        "member": api_obj_payload_tags
                                }
                            }
                        }
            print("Object Name:",api_obj_payload_name, "| Description: ", api_obj_payload_desc)
            url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
            #print(url)
            response = requests.request("POST", url, data = json.dumps(payload), verify = False)
            print(response.text.encode('utf8'))
            print(json.dumps(payload))

        elif 'static' in row["Type"]:
            print('''
            Deploying Staic Group... 
            ''')
            api_obj_payload_name = row["Name"]
            api_obj_payload_desc = row["Description"]
            api_obj_payload_member = row["Addresses"].split(";")
            if "" in row["Tags"]:
                        payload = {
                        "entry": {
                            "@name": api_obj_payload_name,
                            "description": api_obj_payload_desc,
                            "static": {
                                "member": api_obj_payload_member
                                }
                        }
                    }
            elif " " in row["Tags"]:
                    payload = {
                    "entry": {
                            "@name": api_obj_payload_name,
                            "description": api_obj_payload_desc,
                            "static": {
                                "member": api_obj_payload_member
                                }
                        }
                    }
            else :
                api_obj_payload_tags = row["Tags"].split(";")
                payload = {
                            "entry": {
                                "@name": api_obj_payload_name,
                                "description": api_obj_payload_desc,
                                "static": {
                                    "member": api_obj_payload_member
                                    },
                                    "tag": {
                                        "member": api_obj_payload_tags
                                }
                            }
                        }
            print("Object Name:",api_obj_payload_name, "| Description: ", api_obj_payload_desc)
            url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
            print(url)
            response = requests.request("POST", url, data = json.dumps(payload), verify = False)
            print(response.text.encode('utf8'))
            print(json.dumps(payload))