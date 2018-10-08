# Python Email Sender API

This email sender API has a benefit to be able to write an HTML style: You can insert images if you want.

## Adding files on contents
* Set the same file names which you want to send
* `filename.html`: emails body
* `filename.csv`: 'TO' emails list
* `filename.png`: image, which is contains on HTML(optional)

## Run
```shell
$ python3 send_emails.py

Must be use Gmail or G-Suite account. (Enter)

Did you allow the permission on https://myaccount.google.com/lesssecureapps? (Y/n)
    Please visit and allow the permission

        https://myaccount.google.com/lesssecureapps

1. example
Choose one [1-1]: (Integer)

Enter the account: (Gmail or G-Suite account)
Enter your name:
Password:
Enter the subject of the email:

        Should be entered the subject.

------------------------------ Start sending ------------------------------

Are you sure to send emails to John Doe et 1? [Y/n]

Send complete to John Doe(john.doe@example.com)
Send complete to Author(author@example.com)

        Runtime: 16.932s
```

## Issues
1. `smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted.)` - Username or Password error