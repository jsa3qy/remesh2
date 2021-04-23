# Remesh2

Welcome to Jesse's SWE take home ReadMe!

To briefly summarize/conextualize: I have built a Django web app to fulfill the requirements. Django by default just wraps SQLite so I went with that, and although there is no formal front end framework to get up and running here, with a bit more time I would love to have hooked up React!

All information you might need to get this up and running should be found here.

### Before we start
Please make sure you have npm, python3, and pip3 installed on your OS X machine (apologies, I did not test this on anything other than OS X as I don't own any other OS)

### To Run, please enter each command below in sequence in your unix based terminal:

* git clone git@github.com:jsa3qy/remesh2.git
* cd remesh2
* mkdir venv
* python3 -m venv venv
* source venv/bin/activate
* sudo pip3 install -r requirements.txt
* cd remeshApp
* python3 manage.py runserver

### Next Steps...

go to http://localhost:8000/ to see the live app in your browser! From here you will be able to make your first conversations. Once rendered you will be able to click in to add messages, and further click into messages to add thoughts. 

### Testing!

Before you run any tests, please run 'python3 manage.py flush' from the remeshApp folder (the directory that 'manage.py' lives) to clear the database. It will ask you to confirm by typing 'yes', please do so!

running tests should then be as simple as serving the app in one terminal window (python3 manage.py runserver)and then running in another:

coverage run manage.py test boilerplate -v 2

the '-v' will add some verbosity so it's hopefully clear why any tests fail if that's the case. Selenium can be very finnicky on new machines, as it depends on a downloaded chrome driver binary which doesn't always end up where it would hope!

Briefly, the test suite is contains several unit tests for models and forms, and then some end to end testing of the search functionality, as well as entity creation for Conversations, Messages, and Thoughts. All tests are in Test.py

#### Some assumptions I thought were safe to make:
- Given there is no user-control over when messages and thoughts can be added to conversations (i.e. once the convo is made, it's fair game to add to it), and the dates for thoughts and messages are explicitly supposed to be set when "sent", you will find that dates are automatically attached to all three of these objects. My assumption was that time stamps should be accurate to submission, and therefore should not be user malleable. Ordering in online conversation is important and humans are err prone!

#### Some places I know need improvement but time got the best of me:
- input data validation, I do not protect against malicious users, and I do not have many usability features such as preventing repeat Conversation titles (or an alternative way to handle)
- repeated code across front end modules, the front end could be more modular with cleaner shared code (would love to add sass to this)
- General django best practices -- this was my first django project, any cleanliness pitfalls aren't the norm, mostly just a time constraint issue. (e.g. all tests being in one folder)
- There is some code that would need to be adjusted if we were going to deploy this to a production environment (and other steps I'd probably add, such as dockerizing)
- some variable names could benefit from more verbosity, etc etc.
