## Project title
PanOS CSV Bulk Importer

This script is intended to help quickly load configuration
into a PanOS device from another PanOS device using exported CSV files.

Palo's have nearly every part of the GUI exportable as a
CSV, and you can even schedule alot of these exports. For
this reason and others I found it a lot easier to get my
config onto other Palo's that are dissimilar in version



## Motivation

Because Palo Alto have exceptionally great tools such as Expedition, or even just exporting a config and importing it. Obviously there are limitations in both of these tools which is why I have made this script.

I created this project because I needed to do some Palo testing and training on a Lab VM and I wanted to replicate my prod environment and I really couldn't be bothered in making the thousands of objects and equaly large number of policies. Also I have used this tool in conjunction with Ansible to allow the config to this LabVM to be constantly up-to-date with CSV files.

To find out more on how I have done this and how Iused this script please feel free to visit my blog - https://www.danielbostock.com


## Screenshots

Include logo/demo screenshot etc.

## Features

Bulk Object (Addresses, Tags etc...) creation using CSV
Bulk Policy (Security, NAT etc...)creation using CSV

## Tests
Describe and show how to run the tests with code examples.

## How to use?
If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.

## Contribute

Let people know how they can contribute into your project. A [contributing guideline](https://github.com/zulip/zulip-electron/blob/master/CONTRIBUTING.md) will be a big plus.

## Credits
Give proper credits. This could be a link to any repo which inspired you to build this project, any blogposts or links to people who contrbuted in this project. 

#### Anything else that seems useful

## License
A short snippet describing the license (MIT, Apache etc)

MIT © [Yourname]()