from classes import Field_Validation
from classes import Send_Email
import json
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../classes"))
import email_data


##global responses
MISSING_EMAIL_CONTENT = "The data is missing or not valid."

class Process:

    def __init__(self, email_content):

        #Check to make sure that we are getting email content here and that it is in json format
        if email_content:
            #store information in a data model
            data = email_data.Data(email_content)
        else:
            return MISSING_EMAIL_CONTENT

    def response(self):
        #validation = Field_Validation.Validation()
        send_email = Send_Email.Send_Email(data)
        return send_email.send_email()
