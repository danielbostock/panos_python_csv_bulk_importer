import csv

# Error Messages
sel_err = 'Selection Error: Please select a supported choice by chosing its respective number.'


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


