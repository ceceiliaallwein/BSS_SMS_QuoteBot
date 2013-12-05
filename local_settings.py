'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "ACfe77d42a27d74a5e199e9a6dda6dd842" 
AUTH_TOKEN = "dd51a79f15911993c807c9acfec56805"
BSSSPAM_APP_SID = "AP55176de141377159202b0ce15c97f185"
BSS_SPAM_ID = "+12602714996"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
