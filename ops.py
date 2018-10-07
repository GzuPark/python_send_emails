import os
import re
import time
from getpass import getpass


def stopwatch(fn):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        print("\n\tRuntime: {:.3f}s\n".format(time.time()-start_time))
        return result
    return wrapper


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return ' '.join(cleantext.split())


def attach_dir(filename):
    return os.path.join(os.getcwd(), 'contents', filename)


def get_list():
    contents = os.listdir('contents')
    result = []
    for content in contents:
        if content.lower().endswith('.html'):
            result.append(content.split('.')[0])
    return result


def validity(feature):
    value = ""
    print("")
    while value == "":
        if feature == "the password":
            value = getpass()
        else:
            value = input('Enter {}: '.format(feature))
    return value


def img_extension(filename):
    contents = os.listdir('contents')
    for content in contents:
        if content.lower().startswith(filename):
            if (content.lower().endswith('png') 
                or content.lower().endswith('jpg')
                or content.lower().endswith('jpeg')
                or content.lower().endswith('bmp')):
                return content
    return "EMPTY"


def security_check(id, name, pw, sub):
    notice = '\n\n\tYour password contains on the '
    if pw in name:
        raise ValueError(notice+'name.')
    elif pw in sub:
        raise ValueError(notice+'subject.')
    else:
        pass
        