# Restaurant-Chatbot
## Introduction 
The repository has the code for a chatbot which books rooms/tables for people at a restaurant. `RASA` framework (an open-source machine learning framework) has been used to train the chatbot in order to take requests from the user along with handling FAQs in the middle of conversation.
Click here to know the details of [RASA](https://rasa.com/docs/rasa/).

## About the Project
The chatbot makes use of [Rasa Forms](https://rasa.com/docs/rasa/forms/) to exract the details provided by the user (`number of rooms to be booked, AC/Non-AC and the time`). The slots are filled using the information which the user provides. It also smartely handels the FAQs, even if asked in the middle of details extraction.\
The bot is capable of handling relative time such as in half an hour, after 10 minutes etc. [Duckling Entity Extractor](https://duckling.wit.ai/) has been used for this purpose. \
The bot books the rooms only at intervals of 15 minutes and remains open from 6AM to 11PM. It rejects the booking outside this time. If at 3:15 PM, the user asks to book rooms after 10 minutes, the booking is made for 3:30 PM. These logics have been handled in actions module.

## Installation
`LINUX-type` operating system and `python3` is required.
#### Rasa Installation:
    $ python3 env_setup.py

#### Duckling Entity Extractor installation:
    $ wget -qO- https://get.haskellstack.org/ | sh 
    $ sudo apt-get install libpcre3 libpcre3-dev
    $ git clone https://github.com/facebook/duckling.git
    $ cd duckling
    $ stack build
## Usage steps
#### 1. Run chatbot in command line
    $ source ./myvenv/bin/activate
    $ rasa shell --endpoints endpoints.yml
#### 2. Run Duckling server
    $ cd duckling
    $ stack exec duckling-example-exe
#### 3. Run action server
    $ source ./myvenv/bin/activate
    $ rasa run actions

## FAQs
- What are the specials in the restaurant?
- When does the restaurant remain open?
- How to cancel a reservation?
- What are the timings of the restaurant?

`Have fun booking rooms with the interactive chatbot :)`