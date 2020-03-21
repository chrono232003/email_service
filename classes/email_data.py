import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../classes"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))

import field_validation

class Data:

    def get_to_email(self):
        return self.__to_email

    def get_to_name(self):
        return self.__to_name

    def get_from_email(self):
        return self.__from_email

    def get_from_name(self):
        return self.__from_name

    def get_subject(self):
        return self.__subject

    def get_body(self):
        return self.__body

    def __init__(self, email_content):

        #validate the data before storing it. If there is an issue, send the error back to the view.
        validation = field_validation.Validation()
        if validation.data_validates_succesfully(self.data):

        self.__to_email = email_content['recipient_email']
        self.__to_name = email_content['recipient_name']
        self.__from_email = email_content['sender_email']
        self.__from_name = email_content['sender_name']
        self.__subject = email_content['email_subject']
        self.__body = email_content['email_body']
