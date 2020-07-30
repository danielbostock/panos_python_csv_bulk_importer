import csv


# Error Messages
sel_err = 'Selection Error: Please select a supported choice by chosing its respective number.'
gen_err = 'You have either entered an incorrect expected output or something else has broken, please restart the script.'

# This will gather from the end user what supported file type that they will be using for importing
def selector ():
    selection = 0
    while selection == 0:
        selection = int(input('''

PanOS Bulk Importer currently supports the following file types

1. CSV

Please select a file type that is required: '''))
        

        if selection == 1:
            file = str(input('Enter the full path location to the CSV file to use for importing of objects: '))
            confirmation = 0
            selection = 1
            while confirmation == 0 and selection == 1:
                if confirmation == 0: 
                    print('File selected for importing: ' + file)
                    confirmation = int(input('''Confirm this file location is correct.
1. Yes | 2. No : '''))

                    if confirmation == 1:
                        continue
                    
                    if confirmation >= 2:
                        selection = 0
                        confirmation = 0
                        print (sel_err)
                        break

            return confirmation, selection

        while selection >= 2:
            if selection >= 2:
                selection = 0
                print (sel_err)
                break
        
        else:
            print (sel_err)
            break

    print (selection)


# Device info gatherer


def location ():

    location = 0

    while location == 0:
        if location == 0:
            location = '&location=vsys&vsys=vsys1'
            print('Current API default device vSys location is: ' + location.replace('&location=vsys&vsys=', ''))
            location_conf = int(input('''Please confirm vsys location is correct or you would like to change it. 
1. Yes | 2. Custom :'''))

            if location_conf == 1:
                continue

            if location_conf == 2:
                location = str(input('Enter the device vSys Location: '))
            
            else:
                print(sel_err)
                break

    return location

def hostname ():

    hostname = 0

    while hostname == 0:
        if hostname == 0:
            hostname = 'https://palodevice.local'
            print('Current destination Palo Alto device: ' + hostname )
            hostname_conf = int(input('''Please confirm default hostname is correct or you would like to change it. 
1. Yes | 2. Custom :'''))

        if hostname_conf == 1:
            continue

        if hostname_conf >= 2:
            hostname = str(input('Enter the device URL or IP: '))

        else:
            print(sel_err)
            break

    return hostname

def key ():

    key = 0

    while key == 0:
        if key == 0:
            key = str(input('Enter the API key:'))
            continue

        else:
            print(gen_err)
            break
    
    return key

# File import selector
def selector ():
    selection = 0
    confirmation = 0
    while selection == 0:
        selection = int(input('''

PanOS Bulk Importer currently supports the following file types

1. CSV

Please select a file type that is required: '''))
        

        if selection == 1:
            file = str(input('Enter the full path location to the CSV file to use for importing of objects: '))
            selection = 1

        if selection >= 2:
            selection = 0
            print (sel_err)

        else:
            print (sel_err)
            break

    while confirmation == 0:
        if confirmation == 0: 
            print('File selected for importing: ' + file)
            confirmation = int(input('''Confirm this file location is correct.
1. Yes | 2. No : '''))

        if confirmation == 1:
            continue
                    
        if confirmation >= 2:
            selection = 0
            confirmation = 0
            print (sel_err)
        
        else:
            print (sel_err)
            break
            
    
    return file





