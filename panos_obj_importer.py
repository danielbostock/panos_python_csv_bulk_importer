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


## 1.0 Tag Objects Importer

def tagobject_importer(tags, api_hostname, api_key, api_loc, api_input):
    ## vars used to build the payload ##
    panos_api_objname = '&name='
    panos_api_objtype = '/restapi/9.0/Objects/Tags?'
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

## 2.0 Address Objects Importer

def addrobjects_importer(addr, api_hostname, api_key, api_loc, api_input):
    ## vars used to build the payload ##
    panos_api_objname = '&name='
    panos_api_objtype = '/restapi/9.0/Objects/Addresses?'
    panos_api_hostname = str(api_hostname)
    panos_api_key = str(api_key)
    panos_api_loc = str(api_loc)
    panos_api_input = str(api_input)
    ####################################

    ## Create Address Objects with tags
    for row in addr:
        api_obj_payload_ip = row["Address"]
        api_obj_payload_name = row["Name"]
        api_obj_payload_desc = row["Description"]
        api_obj_payload_tags = row["Tags"].split(";")
        payload = {
                        "entry": {
                            "@name": api_obj_payload_name,
                            "description": api_obj_payload_desc,
                            "ip-netmask": api_obj_payload_ip,
                            "tag": {
                            "member":  
                            api_obj_payload_tags
                            }
                        }
                }
        ## Build API call URL and make API HTTPS Requests call
        url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
        response = requests.request("POST", url, data = json.dumps(payload), verify = False)

        ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
        print("Object Name:",api_obj_payload_name,"| IP: ", api_obj_payload_ip, "| Description: ", api_obj_payload_desc, "| Tags: ", api_obj_payload_tags)
        print("API Call URL: ", url)
        print("API Response Code: ", response.text.encode('utf8'))
        print("JSON Body: ", json.dumps(payload))
        print(''' 
                
        ''')

        ## Create Address Objects without tags
        if "" in row["Tags"]:
            payload = {
                    "entry": {
                        "@name": api_obj_payload_name,
                        "description": api_obj_payload_desc,
                        "ip-netmask": api_obj_payload_ip
                    }
                }
        ## Build API call URL and make API HTTPS Requests call
        url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
        response = requests.request("POST", url, data = json.dumps(payload), verify = False)

        ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
        print("Object Name:",api_obj_payload_name,"| IP: ", api_obj_payload_ip, "| Description: ", api_obj_payload_desc)
        print("API Call URL: ", url)
        print("API Response Code: ", response.text.encode('utf8'))
        print("JSON Body: ", json.dumps(payload))
        print(''' 
                
        ''')

## 3.0 Address Groups Object Importer

def addrgrpobjects_importer(addrgrp, api_hostname, api_key, api_loc, api_input):
    ## vars used to build the payload ##
    panos_api_objname = '&name='
    panos_api_objtype = '/restapi/9.0/Objects/AddressGroups?'
    panos_api_hostname = str(api_hostname)
    panos_api_key = str(api_key)
    panos_api_loc = str(api_loc)
    panos_api_input = str(api_input)
    ####################################
    
    ## Create Dynamic Address Group Objects with tags
    for row in addrgrp:
        api_obj_payload_name = row["Name"]
        api_obj_payload_desc = row["Description"]
        if 'dynamic' in row["Type"] and ';' in row["Tags"]:
            print(''' 
            Deploying Dynamic Group...
            ''')
            api_obj_payload_grpfilter = row["Addresses"]
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

            ## Build API call URL and make API HTTPS Requests call
            url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
            response = requests.request("POST", url, data = json.dumps(payload), verify = False)

            ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
            print("Object Name:",api_obj_payload_name, "| Description: ", api_obj_payload_desc)
            print("API Call URL: ", url)
            print("API Response Code: ", response.text.encode('utf8'))
            print("JSON Body: ", json.dumps(payload))
            print(''' 
                
            ''')

        ## Create Dynamic Address Group Objects without tags
        elif 'dynamic' in row["Type"] and "" in row["Tags"]:
            api_obj_payload_grpfilter = row["Addresses"]
            payload = {
                    "entry": {
                        "@name": api_obj_payload_name,
                        "description": api_obj_payload_desc,
                        "dynamic": {
                                "filter": api_obj_payload_grpfilter
                                }
                        }
                    }
            ## Build API call URL and make API HTTPS Requests call
            url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
            response = requests.request("POST", url, data = json.dumps(payload), verify = False)

            ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
            print("Object Name:",api_obj_payload_name, "| Description: ", api_obj_payload_desc)
            print("API Call URL: ", url)
            print("API Response Code: ", response.text.encode('utf8'))
            print("JSON Body: ", json.dumps(payload))
            print(''' 
                    
                ''')

        ## Create Static Address Group Objects
        elif 'static' in row["Type"] and ';' in row ["Tags"]:
            print('''
            Deploying Staic Group... 
            ''')
            api_obj_payload_member = row["Addresses"].split(";")
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
            
            ## Build API call URL and make API HTTPS Requests call
            url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
            response = requests.request("POST", url, data = json.dumps(payload), verify = False)

            ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
            print("Object Name:",api_obj_payload_name, "| Description: ", api_obj_payload_desc)
            print("API Call URL: ", url)
            print("API Response Code: ", response.text.encode('utf8'))
            print("JSON Body: ", json.dumps(payload))
            print(''' 
                
            ''')

        ## Create Static Address Group Objects without tags
        elif 'static' in row["Type"] and "" in row ["Tags"]:
            api_obj_payload_member = row["Addresses"].split(";")
            payload = {
                        "entry": {
                            "@name": api_obj_payload_name,
                            "description": api_obj_payload_desc,
                            "static": {
                                "member": api_obj_payload_member
                                }
                        }
                    }
            ## Build API call URL and make API HTTPS Requests call
            url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
            response = requests.request("POST", url, data = json.dumps(payload), verify = False)

            ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
            print("Object Name:",api_obj_payload_name, "| Description: ", api_obj_payload_desc)
            print("API Call URL: ", url)
            print("API Response Code: ", response.text.encode('utf8'))
            print("JSON Body: ", json.dumps(payload))
            print(''' 
                    
                ''')


## 4.0 Service Object Importer

def svcobjects_importer(svc, api_hostname, api_key, api_loc, api_input):
    ## vars used to build the payload ##
    panos_api_objname = '&name='
    panos_api_objtype = '/restapi/9.0/Objects/Services?'
    panos_api_hostname = str(api_hostname)
    panos_api_key = str(api_key)
    panos_api_loc = str(api_loc)
    panos_api_input = str(api_input)
    ####################################

    ## Create Service Objects with tags
    for row in svc:
        api_obj_payload_name = row["Name"]
        api_obj_payload_proto = row["Protocol"]
        api_obj_payload_desc = row["Description"]
        api_obj_payload_dstprt = row["Destination Port"]
        api_obj_payload_tags = row["Tags"]
        ## Create TCP Service Objects with tags
        if 'TCP' in row["Protocol"]:
                payload = {
                            "entry": {
                                "@name": api_obj_payload_name,
                                "description": api_obj_payload_desc,
                                "protocol": {
                                    "tcp": {
                                        "port": api_obj_payload_dstprt,
                                        "override": {
                                            "no": { }
                                        },    
                                "tag": {
                                    "member": api_obj_payload_tags
                                        }
                                    }
                                }
                            }
                        }

                ## Build API call URL and make API HTTPS Requests call
                url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
                response = requests.request("POST", url, data = json.dumps(payload), verify = False)

                ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
                print("Service Name:", api_obj_payload_name,"| DST Port: ", api_obj_payload_dstprt, "| Protocol: ", api_obj_payload_proto, "| Description: ", api_obj_payload_desc)
                print("API Call URL: ", url)
                print("API Response Code: ", response.text.encode('utf8'))
                print("JSON Body: ", json.dumps(payload))
                print(''' 
                
                ''')

                ## Create TCP Service Objects without tags
                if "" in row["Tags"]:
                    payload = {
                                "entry": {
                                    "@name": api_obj_payload_name,
                                    "description": api_obj_payload_desc,
                                    "protocol": {
                                        "tcp": {
                                            "port": api_obj_payload_dstprt,
                                            "override": {
                                                "no": { },
                                            }
                                        }
                                    }
                                }
                            }

                ## Build API call URL and make API HTTPS Requests call
                url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
                response = requests.request("POST", url, data = json.dumps(payload), verify = False)

                ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
                print("Service Name:", api_obj_payload_name,"| DST Port: ", api_obj_payload_dstprt, "| Protocol: ", api_obj_payload_proto, "| Description: ", api_obj_payload_desc)
                print("API Call URL: ", url)
                print("API Response Code: ", response.text.encode('utf8'))
                print("JSON Body: ", json.dumps(payload))
                print(''' 
                
                ''')

        ## Create UDP Service Objects with tags
        elif 'UDP' in row["Protocol"]:
                payload = {
                            "entry": {
                                "@name": api_obj_payload_name,
                                "description": api_obj_payload_desc,
                                "protocol": {
                                    "udp": {
                                        "port": api_obj_payload_dstprt,
                                        "override": {
                                            "no": { }
                                        },    
                                "tag": {
                                    "member": api_obj_payload_tags
                                        }
                                    }
                                }
                            }
                        }

                ## Build API call URL and make API HTTPS Requests call
                url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
                response = requests.request("POST", url, data = json.dumps(payload), verify = False)

                ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
                print("Service Name:", api_obj_payload_name,"| DST Port: ", api_obj_payload_dstprt, "| Protocol: ", api_obj_payload_proto, "| Description: ", api_obj_payload_desc)
                print("API Call URL: ", url)
                print("API Response Code: ", response.text.encode('utf8'))
                print("JSON Body: ", json.dumps(payload))
                print(''' 
                
                ''')

                ## Create UDP Service Objects without tags
                if "" in row["Tags"]:
                    payload = {
                                "entry": {
                                    "@name": api_obj_payload_name,
                                    "description": api_obj_payload_desc,
                                    "protocol": {
                                        "udp": {
                                            "port": api_obj_payload_dstprt,
                                            "override": {
                                                "no": { },
                                            }
                                        }
                                    }
                                }
                            }

                ## Build API call URL and make API HTTPS Requests call
                url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
                response = requests.request("POST", url, data = json.dumps(payload), verify = False)

                ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
                print("Service Name:", api_obj_payload_name,"| DST Port: ", api_obj_payload_dstprt, "| Protocol: ", api_obj_payload_proto, "| Description: ", api_obj_payload_desc)
                print("API Call URL: ", url)
                print("API Response Code: ", response.text.encode('utf8'))
                print("JSON Body: ", json.dumps(payload))
                print(''' 
                
                ''')

## 5.0 Service Groups Object Importer

def svcgrpobjects_importer(svcgrp, api_hostname, api_key, api_loc, api_input):
    ## vars used to build the payload ##
    panos_api_objname = '&name='
    panos_api_objtype = '/restapi/9.0/Objects/ServiceGroups?'
    panos_api_hostname = str(api_hostname)
    panos_api_key = str(api_key)
    panos_api_loc = str(api_loc)
    panos_api_input = str(api_input)
    ####################################

    ## Create Service Group Objects with tags
    for row in svcgrp:
        api_obj_payload_name = row["Name"]
        api_obj_payload_svc = row["Services"].split(";")
        api_obj_payload_tags = row["Tags"].split(";")
        payload = {
                    "entry": {
                        "@name": api_obj_payload_name,
                        "members": {
                            "member": api_obj_payload_svc
                            },
                        "tag": {
                            "member":  
                            api_obj_payload_tags
                            }
                        }
                    }
        ## Create Service Group Objects without tags
        if "" in row["Tags"]:
            payload = {
                        "entry": {
                            "@name": api_obj_payload_name,
                            "members": {
                                "member": api_obj_payload_svc
                                }
                            }
                        }

        ## Build API call URL and make API HTTPS Requests call
        url = panos_api_hostname + panos_api_objtype + panos_api_key + panos_api_loc + panos_api_objname + api_obj_payload_name + panos_api_input
        response = requests.request("POST", url, data = json.dumps(payload), verify = False)

        ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
        print("SVC Group Name:", api_obj_payload_name, "| Services: ", api_obj_payload_svc)
        print("API Call URL: ", url)
        print("API Response Code: ", response.text.encode('utf8'))
        print("JSON Body: ", json.dumps(payload))
        print(''' 
               
            ''')