import schedule
import sys
import os

path = os.chdir('/home/coder/project/'+ str(sys.argv[1]))

def add():
    os.system('git add .')
    os.system('git commit -m "Add a chore"')

def push():
    os.system('git push origin master')
    
schedule.every(30).minutes.do(add)
schedule.every(1).hours.do(push)

while True:
    schedule.run_pending()