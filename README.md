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