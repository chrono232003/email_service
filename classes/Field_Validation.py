import re
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))
import const

class Validation:

    def data_validates_successfully(self, email_content):
        
        validation_arr = [self.__email_is_valid(email_content['recipient_email']),
                          self.__email_is_valid(email_content['sender_email']),
                          self.__name_is_valid(email_content['recipient_name']),
                          self.__name_is_valid(email_content['sender_name']),
                          self.__subject_is_valid(email_content['email_subject']),
                          self.__body_is_valid(email_content['email_body'])]


        # check each field individually
        for val_func_passed in validation_arr:
            if val_func_passed is not None:
                #if there is a validation failure, return the error string
                return val_func_passed
        #everything passed
        return const.VALIDATION_SUCCESS_STRING

    # utility classes
    def __email_is_valid(self, email):
        regex = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
        return None if email and regex.search(email) else const.VALIDATION_FAIL_EMAIL_STRING

    def __name_is_valid(self, name):
        regex = re.compile(r'^[aA-zZ\s]+$')
        return None if name and regex.match(name) else const.VALIDATION_FAIL_NAME_STRING

    def __subject_is_valid(self, subject):
        regex = re.compile(r'^[\w\d\s?,_-]*$')
        return None if subject and regex.match(subject) else const.VALIDATION_FAIL_SUBJECT_STRING

    #NOTE: validate the body with the html tags first and strip them later
    def __body_is_valid(self, body):
        regex = re.compile(r'^[\w\d\s<>/_-]*$')
        return None if body and regex.search(body) else const.VALIDATION_FAIL_BODY_STRING
