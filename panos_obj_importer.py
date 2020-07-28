import csv
import warnings
import contextlib
import json
import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#Global Vars

## 1.0 Tag Objects Importer

def tags(file, location, hostname, key):
    ## vars used to build the payload ##
    tags = csv.DictReader(open(file))
    apiname = '&name='
    apitype = '/restapi/v9.1/Objects/Tags?'
    ####################################

    ## Create Tag objects
    for row in tags:
        name = row["Name"]
        comments = row["Comments"]
        payload = {
                    "entry": {
                        "@name": name,
                        "comments": comments
                            }
                    }

        ## Build API call URL and make API HTTPS Requests call        
        url = hostname + apitype + location + apiname + name
        headers = { 'X-PAN-KEY': str(key)}
        response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

        ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
        print("Tags: ", name, "| Description: ", comments)
        print("API Call URL: ", url)
        print("API Response Code: ", response.text.encode('utf8'))
        print("JSON Body: ", json.dumps(payload))
        print(''' 
                
            ''')

## 2.0 Address Objects Importer

def addrobj(file, location, hostname, key):
    ## vars used to build the payload ##
    addr = csv.DictReader(open(file))
    apiname = '&name='
    apitype = '/restapi/v9.1/Objects/Addresses?'
    ####################################

    ## Create Address Objects with tags
    for row in addr:
        ip = row["Address"]
        name = row["Name"]
        desc = row["Description"]
        tags = row["Tags"].split(";")
        payload = {
                        "entry": {
                            "@name": name,
                            "description": desc,
                            "ip-netmask": ip,
                            "tag": {
                            "member": tags
                            }
                        }
                }
        ## Build API call URL and make API HTTPS Requests call
        url = hostname + apitype + location + apiname + name
        headers = { 'X-PAN-KEY': str(key)}
        response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

        ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
        print("Object Name:",name,"| IP: ", ip, "| Description: ", desc, "| Tags: ", tags)
        print("API Call URL: ", url)
        print("API Response Code: ", response.text.encode('utf8'))
        print("JSON Body: ", json.dumps(payload))
        print(''' 
                
        ''')

        ## Create Address Objects without tags
        if "" in row["Tags"]:
            payload = {
                    "entry": {
                        "@name": name,
                        "description": desc,
                        "ip-netmask": ip
                    }
                }
        ## Build API call URL and make API HTTPS Requests call
        url = hostname + apitype + location + apiname + name
        headers = { 'X-PAN-KEY': str(key)}
        response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

        ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
        print("Object Name:",name,"| IP: ", ip, "| Description: ", desc)
        print("API Call URL: ", url)
        print("API Response Code: ", response.text.encode('utf8'))
        print("JSON Body: ", json.dumps(payload))
        print(''' 
                
        ''')

## 3.0 Address Groups Object Importer

def addrgrpobj(file, location, hostname, key):
    ## vars used to build the payload ##
    addrgrp = csv.DictReader(open(file))
    apiname = '&name='
    apitype = '/restapi/v9.1/Objects/AddressGroups?'
    ####################################
    
    ## Create Dynamic Address Group Objects with tags
  
    for row in addrgrp:
        name = row["Name"]
        desc = row["Description"]
        
        if 'dynamic' in row["Type"]:
            print(''' 
            Deploying Dynamic Group...
            ''')
            grpfilter = row["Addresses"]
            tags = row["Tags"].split(";")
            payload = {
                            "entry": {
                                "@name": name,
                                "description": desc,
                                "dynamic": {
                                    "filter": grpfilter
                                    },
                                    "tag": {
                                        "member": tags
                                }
                            }
                        }

            ## Build API call URL and make API HTTPS Requests call
            url = hostname + apitype + location + apiname + name
            headers = { 'X-PAN-KEY': str(key)}
            response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

            ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
            print("Object Name:",name, "| Description: ", desc)
            print("API Call URL: ", url)
            print("API Response Code: ", response.text.encode('utf8'))
            print("JSON Body: ", json.dumps(payload))
            print(''' 
                
            ''')
                ## Create Dynamic Address Group Objects without tags

            if "" in row["Tags"]:
                grpfilter = row["Addresses"]
                payload = {
                        "entry": {
                            "@name": name,
                            "description": desc,
                            "dynamic": {
                                    "filter": grpfilter
                                    }
                            }
                        }
                ## Build API call URL and make API HTTPS Requests call
                url = hostname + apitype + location + apiname + name
                headers = { 'X-PAN-KEY': str(key)}
                response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

                ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
                print("Object Name:",name, "| Description: ", desc)
                print("API Call URL: ", url)
                print("API Response Code: ", response.text.encode('utf8'))
                print("JSON Body: ", json.dumps(payload))
                print(''' 
                        
                    ''')

        ## Create Static Address Group Objects
        if 'static' in row["Type"]:
            print('''
            Deploying Staic Group... 
            ''')
            member = row["Addresses"].split(";")
            tags = row["Tags"].split(";")
            payload = {
                        "entry": {
                            "@name": name,
                            "description": desc,
                            "static": {
                                "member": member
                                    },
                                "tag": {
                                    "member": tags
                                }
                            }
                        }
            
        ## Build API call URL and make API HTTPS Requests call
            url = hostname + apitype + location + apiname + name
            headers = { 'X-PAN-KEY': str(key)}
            response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

            ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
            print("Object Name:",name, "| Description: ", desc)
            print("API Call URL: ", url)
            print("API Response Code: ", response.text.encode('utf8'))
            print("JSON Body: ", json.dumps(payload))
            print(''' 
                
            ''')

            ## Create Static Address Group Objects without tags
            if "" in row ["Tags"]:
                member = row["Addresses"].split(";")
                payload = {
                            "entry": {
                                "@name": name,
                                "description": desc,
                                "static": {
                                    "member": member
                                    }
                            }
                        }
                ## Build API call URL and make API HTTPS Requests call
                url = hostname + apitype + location + apiname + name
                headers = { 'X-PAN-KEY': str(key)}
                response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

                ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
                print("Object Name:",name, "| Description: ", desc)
                print("API Call URL: ", url)
                print("API Response Code: ", response.text.encode('utf8'))
                print("JSON Body: ", json.dumps(payload))
                print(''' 
                        
                    ''')


## 4.0 Service Object Importer

def svcobj(file, location, hostname, key):
    ## vars used to build the payload ##
    svcobj = csv.DictReader(open(file))
    apiname = '&name='
    apitype = '/restapi/v9.1/Objects/AddressGroups?'
    ####################################

    for row in svcobj:
        name = row["Name"]
        proto = row["Protocol"]
        desc = row["Description"]
        dstprt = row["Destination Port"]
        tags = row["Tags"].split(';')
        ## Create TCP Service Objects with tags
        if 'TCP' in row["Protocol"]:
            payload = {
                "entry": {
                    "@name": name,
                    "description": desc,
                    "protocol": {
                        "tcp": {
                            "port": dstprt,
                            "override": {
                                "no": { }
                                }
                            }
                        },    
                    "tag": {
                        "member": tags
                            }
                        }
                    }

            ## Build API call URL and make API HTTPS Requests call
            url = hostname + apitype + location + apiname + name
            headers = { 'X-PAN-KEY': str(key)}
            response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

            ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
            print("Service Name:", name,"| DST Port: ", dstprt, "| Protocol: ", proto, "| Description: ", desc)
            print("API Call URL: ", url)
            print("API Response Code: ", response.text.encode('utf8'))
            print("JSON Body: ", json.dumps(payload))
            print(''' 
                    
                ''')

            ## Create TCP Service Objects without tags
            if "" in row["Tags"]:
                payload = {
                    "entry": {
                        "@name": name,
                            "description": desc,
                            "protocol": {
                                "tcp": {
                                    "port": dstprt,
                                    "override": {
                                        "no": { },
                                        }
                                    }
                                }
                            }
                        }

                ## Build API call URL and make API HTTPS Requests call
                url = hostname + apitype + location + apiname + name
                headers = { 'X-PAN-KEY': str(key)}
                response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

                ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
                print("Service Name:", name,"| DST Port: ", dstprt, "| Protocol: ", proto, "| Description: ", desc)
                print("API Call URL: ", url)
                print("API Response Code: ", response.text.encode('utf8'))
                print("JSON Body: ", json.dumps(payload))
                print(''' 
                
                ''')

        ## Create UDP Service Objects with tags
        if 'UDP' in row["Protocol"]:
            payload = {
                "entry": {
                    "@name": name,
                    "description": _desc,
                    "protocol": {
                        "udp": {
                            "port": dstprt,
                            "override": {
                                "no": { }
                                }
                            }
                        },    
                    "tag": {
                        "member": tags
                            }
                        }
                    }

            ## Build API call URL and make API HTTPS Requests call
            url = hostname + apitype + location + apiname + name
            headers = { 'X-PAN-KEY': str(key)}
            response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

            ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
            print("Service Name:", name,"| DST Port: ", dstprt, "| Protocol: ", proto, "| Description: ", desc)
            print("API Call URL: ", url)
            print("API Response Code: ", response.text.encode('utf8'))
            print("JSON Body: ", json.dumps(payload))
            print(''' 
            
            ''')

            ## Create UDP Service Objects without tags
            if "" in row["Tags"]:
                payload = {
                            "entry": {
                                "@name": name,
                                "description": desc,
                                "protocol": {
                                    "udp": {
                                        "port": dstprt,
                                        "override": {
                                            "no": { },
                                        }
                                    }
                                }
                            }
                        }

                ## Build API call URL and make API HTTPS Requests call
                url = hostname + apitype + location + apiname + name
                headers = { 'X-PAN-KEY': str(key)}
                response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

                ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
                print("Service Name:", name,"| DST Port: ", dstprt, "| Protocol: ", proto, "| Description: ", desc)
                print("API Call URL: ", url)
                print("API Response Code: ", response.text.encode('utf8'))
                print("JSON Body: ", json.dumps(payload))
                print(''' 
                
                ''')

## 5.0 Service Groups Object Importer

def svcgrpobj(file, location, hostname, key):
    ## vars used to build the payload ##
    apiname = '&name='
    apitype = '/restapi/9.1/Objects/ServiceGroups?'
    ####################################

    ## Create Service Group Objects with tags
    for row in svcgrp:
        name = row["Name"]
        svc = row["Services"].split(";")
        tags = row["Tags"].split(";")
        payload = {
                    "entry": {
                        "@name": name,
                        "members": {
                            "member": svc
                            },
                        "tag": {
                            "member": tags
                            }
                        }
                    }
        ## Build API call URL and make API HTTPS Requests call
        url = hostname + apitype + location + apiname + name
        headers = { 'X-PAN-KEY': str(key)}
        response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)

        ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
        print("SVC Group Name:", name, "| Services: ", svc)
        print("API Call URL: ", url)
        print("API Response Code: ", response.text.encode('utf8'))
        print("JSON Body: ", json.dumps(payload))
        print(''' 
               
            ''')
        ## Create Service Group Objects without tags
        if "" in row["Tags"]:
            payload = {
                        "entry": {
                            "@name": name,
                            "members": {
                                "member": svc
                                }
                            }
                        }

            ## Build API call URL and make API HTTPS Requests call
            url = hostname + apitype + location + apiname + name
            headers = { 'X-PAN-KEY': str(key)}
            response = requests.request("POST", url, headers = headers,  data = json.dumps(payload), verify = False)
            ## Print feedback of API call for logging and review, disable if you do not wish to see this info or modify to send to a file instead
            print("SVC Group Name:", name, "| Services: ", svc)
            print("API Call URL: ", url)
            print("API Response Code: ", response.text.encode('utf8'))
            print("JSON Body: ", json.dumps(payload))
            print(''' 
                
                ''')