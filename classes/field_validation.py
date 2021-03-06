import re
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../constants"))
import const

# perform validations on all the user input fields. Also, format the html to be plain text.
class Validation:

    def data_validates_successfully(self, email_content):
        
        validation_arr = [self.__email_is_valid(email_content[const.TO_EMAIL]),
                          self.__email_is_valid(email_content[const.FROM_EMAIL]),
                          self.__name_is_valid(email_content[const.TO_NAME]),
                          self.__name_is_valid(email_content[const.FROM_NAME]),
                          self.__subject_is_valid(email_content[const.SUBJECT]),
                          self.__body_is_valid(email_content[const.BODY])]


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
        regex = re.compile(r'^[\w\d\s?<>/_-]*$')
        return None if body and regex.search(body) else const.VALIDATION_FAIL_BODY_STRING
