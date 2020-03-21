#Prerequisites:
    The user will need to have python installed and a couple of python packages (see below). These should all be available through pip.
    #Packages:
        - os
        - sys
        - requests
        - dotenv
        - re

#How to install the application
    1. Clone this repository locally to your system
    2. Once cloned, navigate to the program folder root file.
    3. In the root file, you will see an environmental variable file (.env_template) which contains 3 global variables (See below). This will need the proper information added and changed to '.env'
        - Send Grid API key - Get this from the Send Grid site when you sign up for email services.
        - Mail Gun API key - Get this from the Mail Gun site when you sign up for email services.
        - There is also a preferred mail service variable that defaults to Sendgrid but there are 2 options (sendgrid, mailgun)

    4. There are a couple ways to launch the program
        - With Python prerequisites already installed: run launch.py
        - If you would like to check if you have the prerequistes and install if you don't: run setup.py

#Language and Libraries

I chose Python as it has some great and easy to use http libraries such as 'requests'. I also find its structure great for abstracting data in data models and the way it handles collections.
There are other great options as well such as Java or even php, but I chose Python and Flask because it is lightweight and flexible unlike some other frameworks meant for bigger projects.

#Tradoffs for project requirements

There are a few things that I would have built differently or expanded upon if I had more time on the project.

For one, I would have fleshed out the UI. The form upon launching the application is pretty simplified and could be a little bit more intuitive for the user. For example, A user can add test or HTML in the body field. Ideally a text editor plugin would be handy for writing
and structuring html. The results page is pretty simple. It just shows a user if their email has been send or not or any form errors if front end validation was bypassed. Obviously in a real work scenario
I would display the form again with the various errors for a user to correct.

Another item I would have built on was the testing. I put in some tests around the classes, but there could always be more test cases to make the testing more robust.

I was also thinking that it could have a setup cmd or exe file that checks the users system for all the prerequisites such as the python version and packages. This would allow for a one click full install.

Lastly, I would create a mail service priority list and go down the list if a previous mail service fails. That way, a user would have less downtime because if a service provides a non 200 response, the program would execute the next one.

