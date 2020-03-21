#form field names
TO_NAME    = "recipient_name"
TO_EMAIL   = "recipient_email"
FROM_NAME  = "sender_name"
FROM_EMAIL = "sender_email"
SUBJECT    = "email_subject"
BODY       = "email_body"

#messages to end user
SUCCESS_MESSAGE_TO_USER_MAIL_GUN  = "Your Email was sent successfully through Mail Gun!"
SUCCESS_MESSAGE_TO_USER_SEND_GRID = "Your Email was sent successfully through Send Grid!"
EMAIL_FAILED_TO_SEND_MESSAGE      = "Email service failed, please try again later."
TECHNICAL_ERROR_MESSAGE           = "Something went wrong, please try again later."

#field validation strings
MISSING_EMAIL_CONTENT_STRING   = "The data is missing or not valid."
VALIDATION_SUCCESS_STRING      = "Valid"
VALIDATION_FAIL_EMAIL_STRING   = "Please enter a valid email."
VALIDATION_FAIL_NAME_STRING    = "Please enter a valid name."
VALIDATION_FAIL_SUBJECT_STRING = "Please enter a valid subject."
VALIDATION_FAIL_BODY_STRING    = "Please enter a valid body."

#api status codes
MAIL_GUN_SUCCESS_CODE  = 200
SEND_GRID_SUCCESS_CODE = 202
