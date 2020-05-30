## Project title
PanOS CSV Bulk Importer

This script is intended to help quickly load configuration
into a PanOS device from another PanOS device using exported CSV files.

Palo's have nearly every part of the GUI exportable as a
CSV, and you can even schedule alot of these exports. For
this reason and others I found it a lot easier to get my
config onto other Palo's that are dissimilar in version



## Motivation

Palo Alto have exceptionally great tools such as Expedition, or even just simply exporting a config and importing it. However I found them unable to meet my needs due to a variety of reasons and so I realised, I finally needed to pull my finger out and get started on my Python journey.

I created this project (and it is my first Python project, I would like to add) because I needed to do some Palo testing and training on a Lab VM and I wanted to replicate another environment. I really could not be bothered in making the thousands of objects and equaly large number of policies. 

Currently there are 3 main tools that people can use for handling config files within Palo Alto - Expedition, Panorama & dealing directly with the XML exported configs. Each one has their pros and cons and their distinct purposes. Panorama is actually the tool that solves the problem but this is a paid solution and for the testing environment I was building this was not feasible.

I was therefore left with 2 tools to choose from, so if Panorama is not a limiatation for you, then Panorama I suggest is a much better system to manage this. However for those also without Panorama, the other two tools available were simply lacking - and this is no fault of their own, their purpose is not for what I desire.

I needed automation, and I needed simplicity. Palo Alto have built a very good REST API to deploy changes to. I decided to use this to leverage the configuration I needed to deploy because most things in a PanOS device can actually be exported as a CSV. So I set out to build an import tool with Python.

This script has helped me to deploy over thousands of objects, and policies, in a consistent and accurate manner. First and foremeost is my motivator to make this fit to my business purposes. I will keep working to add more logic and functionality as I learn more Python and discover more necessities in this script as time progresses and my usage equally increases.

## Screenshots

Include logo/demo screenshot etc.

## Features

Bulk Object (Addresses, Tags etc...) creation using CSV
Bulk Policy (Security, NAT etc...)creation using CSV

## Tests
Describe and show how to run the tests with code examples.

## How to use and important things to not before use

There are quite a few limitations with this script in its current form. It is very simplistic in nature and is really only built to suit my limited needs. I plan to increase its logic and capacity in future iterations, for now however it is what it is and I will outline how to use it in its current form. However before I explain how to use, I will outline the important things to remember.

Important things to note before use!

    1. panos_python_csv_bulk_importer.py is the parent script which will call on all the functions used for importing.
    2. The bulk importer script is setup to iterate through all the functions listed and do all those actions, if you want to pick and choose which objects & policies are imported then you need to either delete or comment out them in the panos_python_csv_bulk_importer.py file. You do not need to touch the functions file of course.
    3. There is pretty much no error handling logic in this script. This will be added in future versions.
    4. There is very little choice logic built into the script and therefore it is assumed you understand how to read Python and ensure that all the CSV file locations are updated.
    5. THIS IS A WORK IN PROGRESS!!! By no means complete and by no means capable of handling all unique configurations out there. I plan to improve on this, but for now you will be very limited to the CSV Row Headers used in my samples. You are welcome to fork or talk to me and raise a PR to improve upon this as I am keen to build better configuration capabilities into this script.

How to use

    1. Ensure all CSV's are collected off Palo you want to import from, I suggest exporting a CSV with ALL headers (click more columns bottom left of window that pops up to do the CSV export), then deleting the columns of information not needed.
    2. Ensure all CSV row headers match what is being called in the API request
    3. Update locations of csvfile for al the vars in the script - panos_python_csv_bulk_importer.py
    4. 





## Contribute

If you would like to contribute to this project, please first contact me via the various media platforms I am on so we can discuss it further. I am really keen and hopeful that there are people out there who want to contribute and make this even better so please don't be afraid to contact me!

LinkedIn - https://linkedin.com/in/dbostock
Twitter - https://twitter.com/DanielBostock
Email - danielbostock@outlook.com

## Credits
Give proper credits. This could be a link to any repo which inspired you to build this project, any blogposts or links to people who contrbuted in this project. 

#### Anything else that seems useful

## License
The MIT License (MIT)

Copyright (c) 2020 Daniel Bostock

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

MIT © [Daniel Bostock]()