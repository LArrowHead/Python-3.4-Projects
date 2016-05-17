#scope_main.py
#by: LArrowHead
import time
import random
from random import randint

print('\n' * 10)
print('\n\n\n------------------------')
print('        Welcome to Scope!')
print('------------------------')
print('\n\n[Starting... Starting...]')
print('\n\n If stuck: type help-')
time.sleep(3)
print('\nCTRL242 Initiation Process...')
time.sleep(2)
print('\nStarting Droid 242...')
time.sleep(1)
print('\nPlease Wait...')
time.sleep(1)
print('\nAcessing Available Systems...')
time.sleep(1)
print('\nFinding Online Server...')
time.sleep(1)
print('\nConntected!')
time.sleep(1)
print('...')
print('\nDroid Now Active!')
time.sleep(1)

print('''\n\nYou are aboard the Shuttle towards Resesido in the year 5352
near the Milky Way Galaxy. An enemy ship has boarded our vessel and
we are under heavy attack! Your lazer and movement sensor have failed to rebute...
You should go to the Maintenance Room!''')

def start(inventory):
    print('\n--------------')
    print('\nDroid Ready...')
    time.sleep(1)
    print('...')
    time.sleep(1)
	print('\n[-MAIN ELEVATOR-]')
	print('\n1.) level 1 - Security Wing')
	print('2.) level 2 - Maintenanc Room')
	print('3.) level 3 - Cargo Hold - Airlock')
	print('4.) level 4 - Droid Hangar Pad')
	print('5.) level 5 - Shuttle Control Room')
	print('6.) level 6 - Observation Tower')
	print('7.) level 7 - Emergency Exit\n')

	cmdlist = ['1','2','3','4','5','6','7']
	cmd = getcmd(cmdlist)
