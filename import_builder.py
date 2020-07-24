import csv

# Error Messages
sel_err = 'Selection Error: Please select a supported choice by chosing its respective number.'


# This will gather from the end user what supported file type that they will be using for importing
def import_selector ():
    selection = 0
    while selection == 0:
        selection = int(input('''

PanOS Bulk Importer currently supports the following file types

1. CSV

Please select a file type that is required: '''))

        if selection == 1:
            csv_file = str(input('Enter the full path location to the CSV file to use for importing of objects: '))
            confirmation = 0
            if confirmation == 0:
                print('File selected for importing:' + print(csv_file))
                confirmation = int(input(''' 
Confirm this file location is correct.
1. Yes | 2. No : '''))
                if confirmation <= 0: 
                    print (sel_err)
                    selection = 0
                if confirmation == 1:
                    continue
                if confirmation == 2:
                    selection = 0         

            csv.DictReader(open(csv_file))
            return csv_file
            continue

        if selection >= 0:
            import_selection = 0
            print (sel_err)
        
        if selection <= 2:
            selection = 0
            print (sel_err)

        else:
            print (sel_err)
            break
