# Prerequisites:

The user will need to have python installed and a couple of python packages (see below). These should all be available through pip.
### Packages:
* os
* sys
* requests
* dotenv
* re

# How to install the application

1. Clone this repository locally to your system
1. Once cloned, navigate to the program folder root file.
1. In the root file, you will see an environmental variable file (.env_template) which contains 5 global variables (See below). This will need the proper information added and changed to '.env' (NOTE: it is very important to change the filename to '.env' and strip '_template' for the service to work).
    * Send Grid API endpoint - Get this from the Send Grid site when you sign up for email services.
    * Mail Gun API endpoint - Get this from the Mail Gun site when you sign up for email services.
    * Send Grid API key - Get this from the Send Grid site when you sign up for email services.
    * Mail Gun API key - Get this from the Mail Gun site when you sign up for email services.
    * There is also a preferred mail service variable that defaults to Sendgrid but there are 2 options (sendgrid, mailgun)
1. Testing (Optional) - In the root file, there is a cmd called 'run_tests.cmd' which will run some of the tests including an success integration test with the default email service.

1. There are a couple ways to launch the program
    * With Python prerequisites already installed: run launch.py
    * If you would like to check if you have the prerequistes and install if you don't: run setup.py

# Language and Libraries

I chose Python as it has some great and easy to use http libraries such as 'requests'. I also find its structure great for abstracting data in data models and the way it handles collections.
There are other great options as well such as Java or even php, but I chose Python and Flask because it is lightweight and flexible unlike some other frameworks meant for bigger projects.

# Tradoffs for project requirements

There are a few things that I would have built differently or expanded upon if I had more time on the project.

1. For one, I would have fleshed out the UI. The form upon launching the application is pretty simplified and could be a little bit more intuitive for the user. For example, A user can add test or HTML in the body field. Ideally a text editor plugin would be handy for writing and structuring html. The results page is pretty simple. It just shows a user if their email has been send or not or any form errors if front end validation was bypassed. Obviously in a real work scenario, I would display the form again with the various errors for a user to correct.

1. Data Models - I am a big believer in structured data. If I had more time on the project, I would have created a data model for each request. The data is much the same, but request.post is pretty common in python with the general variation of the body. I would have abstracted the request with individual subclasses for each mail api. That way, the code would be extendable if we add more api services. 

1. Another item I would have built on was the testing. I put in some tests around the classes, but there could always be more test cases to make the testing more robust. There are so many different variations with free text fields and these should be tested thoroughly.

1. I was also thinking that it could have a setup cmd or exe file that checks the users system for all the prerequisites such as the python version and packages. This would allow for a one click full install.

1. Lastly, I would create a mail service priority list and go down the list if a previous mail service fails. That way, a user would have less downtime because if a service provides a non 200 response, the program would execute the next one.

