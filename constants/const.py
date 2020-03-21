#form field names
TO_NAME    = "to_name"
TO_EMAIL   = "to"
FROM_NAME  = "from_name"
FROM_EMAIL = "from"
SUBJECT    = "subject"
BODY       = "body"

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

#api_endpoints
SEND_GRID_ENDPOINT = "https://api.sendgrid.com/v3/mail/send"
MAIL_GUN_ENDPOINT = "https://api.mailgun.net/v3/sandbox81a896c981834ea09476e7b153d9ba24.mailgun.org/messages"

#api status codes
MAIL_GUN_SUCCESS_CODE  = 200
SEND_GRID_SUCCESS_CODE = 202
