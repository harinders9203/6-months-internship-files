import os

os_name=os.name.lower()
if os_name == 'posix':
    os_name="Linux"
else:
    os_name='Windows'

uname=os.getlogin()
curdir=os.listdir(".")