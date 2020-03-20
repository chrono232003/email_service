from classes import Field_Validation
from classes import Send_Email
import json

##global responses
MISSING_EMAIL_CONTENT = "The data is missing or not valid."

class Process:

    email_content = {}

    def __init__(self, email_content):

        #Check to make sure that we are getting email content here and that it is in json format
        if email_content:
            self.email_content = email_content
        else:
            return MISSING_EMAIL_CONTENT

    def response(self):
        #validation = Field_Validation.Validation()
        send_email = Send_Email.Send_Email(self.email_content)
        return send_email.send_via_mail_gun()
