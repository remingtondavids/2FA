import hashlib
from datetime import datetime
from multiprocessing.connection import wait
from time import sleep

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def generate2FAToken():
        time = datetime.datetime.now()


# dtime = datetime.datetime.now()

while (True):

    dt = datetime.today()
    seconds = dt.timestamp()

    print(seconds)


    sleep(10)

