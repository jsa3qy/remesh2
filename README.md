# Remesh2

Welcome to Jesse's SWE take home ReadMe!

All information you might need to get this up and running should be found here.

### Before we start
Please make sure you have npm and pip installed on your OS X machine (apologies, I did not test this on anything other than OS X as I don't own any other OS)

### To Run, please enter each command below in sequence in your unix based terminal:

git clone git@github.com:jsa3qy/remesh2.git
cd remesh2
sudo pip3 install -r requirements.txt
cd remeshApp
npm install

python3 manage.py runserver

### Next Steps...

go to http://localhost:8000/ to see the live app in your browser! From here you will be able to make your first conversations. Once rendered you will be able to click in to add messages, and further click into messages to add thoughts. 

### Testing!

Before you run any tests, please run 'python3 manage.py flush' from the remeshApp folder (the directory that 'manage.py' lives) to clear the database. It will ask you to confirm by typing 'yes', please do so!

running tests should then be as simple as running:

coverage run manage.py test boilerplate -v 2

the '-v' will add some verbosity so it's hopefully clear why any tests fail if that's the case. Selenium can be very finnicky on new machines, as it depends on a downloaded chrome driver binary which doesn't always end up where it would hope!

#### Some assumptions I thought were safe to make:
- Given there is no user-control over when messages and thoughts can be added to conversations, and the dates for thoughts and messages are explicitly when "sent", you will find that dates are automatically attached to all three of these objects. My assumption was that time stamps should be accurate to submission, and therefore should not be user malleable.

#### Some places I know need improvement but time got the best of me:
- input data validation, I do not protect against malicious users
- repeated code across front end modules, the front end could be more modular with cleaner shared code
- 
