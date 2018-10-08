import os
import time
import random
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid
from ops import clear_screen, stopwatch, attach_dir, clean_html, get_list, validity, img_extension, security_check


class Emails:

    def __init__(self, subject, id, pw, name, content):
        self.subject = subject
        self.id = id
        self.pw = pw
        self.name = name
        self.content = content
        self.from_email = self.id if '@' in self.id else self.id+'@gmail.com'
        self.to_email = attach_dir(content+'.csv')
        self.contents_file = attach_dir(content+'.html')
        self.images = attach_dir(img_extension(content))
        self.timesleep = 3
        self.get_data()

    def get_data(self):
        with open(self.to_email, 'r', encoding='UTF-8') as f:
            self.to_email_list = f.read().splitlines()
        with open(self.contents_file, 'r', encoding='UTF-8') as f:
            self.contents = ''.join(f.read().splitlines())
        
    def sender(self, to_name, to_email):
        msg = EmailMessage()
        msg['Subject'] = self.subject
        msg['From'] = Address(self.name, self.from_email.split('@')[0], self.from_email.split('@')[1])
        msg['To'] = Address(to_name, to_email.split('@')[0], to_email.split('@')[1])
        dear_comment = "<p>Hello {},</p>".format(to_name)
        email_body = dear_comment + self.contents
        msg.set_content(clean_html(email_body))

        asparagus_cid = make_msgid()
        msg.add_alternative(email_body.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
        
        if self.images.endswith('EMPTY'):
            pass
        else:
            with open(self.images, 'rb') as img:
                img_style = self.images.split('.')[1]
                msg.get_payload()[1].add_related(img.read(), 'image', img_style, cid=asparagus_cid)

        # Accept here: https://myaccount.google.com/lesssecureapps
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.login(self.id, self.pw)
            s.send_message(msg)
            print('Send complete to {}({})'.format(to_name, to_email))

    @stopwatch
    def run(self):
        confirm = input('Are you sure to send emails to {} et {}? [Y/n] '.format(self.to_email_list[0].split(',')[0], len(self.to_email_list)-1))
        notice = '\n\n\tCheck {} file and try again.'.format(self.to_email)
        if confirm.lower() in ['y', 'yes']:
            pass
        else:
            raise ValueError(notice)
        print("")
        for each in self.to_email_list:
            to_name = each.split(',')[0].strip()
            to_email = each.split(',')[1].strip()
            self.sender(to_name, to_email)
            time.sleep(self.timesleep+random.random()*2)

# TODO: test mode - send email to myself
# put in individual information script
def main():
    clear_screen()

    # Notice available account
    input('\nMust be use Gmail or G-Suite account. (Enter) ')

    # Check lesssecureapps policy
    lesssecureapps = 'https://myaccount.google.com/lesssecureapps'
    security = input('\nDid you allow the permission on '+lesssecureapps+'? (Y/n) ')
    if security.lower() in ['y', 'yes']:
        pass
    else:
        notice = '\nPlease visit and allow the permission\n\n\t'+lesssecureapps+'\n'
        import webbrowser
        webbrowser.open(lesssecureapps, new=2)
        raise ValueError(notice)

    # Select an email content
    contents = get_list()
    print("")
    for i, content in enumerate(contents):
        print('{}. {}'.format(i+1, content))
    selected = input('Choose one [{}-{}]: '.format(1, len(contents)))
 
    # Input information
    get_id = validity("the account")
    get_name = validity("your name")
    get_pw = validity("the password")
    get_sub = validity("the subject of the email")
    security_check(get_id, get_name, get_pw, get_sub)
    emails = Emails(get_sub, get_id, get_pw, get_name, contents[int(selected)-1])
    print('\n'+'-'*30+' Start sending '+'-'*30+'\n')
    emails.run()


if __name__ == '__main__':
    main()
