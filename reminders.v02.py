import datetime
now = datetime.datetime.now()
hour=now.hour
if(hour>=0 and hour<5):
    print("\nIt’s early. You should be sleeping!")
elif(hour>=5 and hour<7):
    print("\nWake up, brew that coffee, get that mile run in, and get that breakfast…\n")
elif(hour>=7 and hour<9):
    print("\nTime to go to work.\n")
elif(hour>=9 and hour<12):
    print("\nYou should be working!\n")
elif(hour>=12 and hour<13):
    print("\nTake your lunch break!\n")
elif(hour>=13 and hour<17):
    print("\nDo you feel that afternoon lull?\n")
elif(hour>=17 and hour<19):
    print("\nTime to hit the gym…\n")
elif(hour>=19 and hour<21):
    print("\nGotta eat that dinner.\n")
elif(hour>=21 and hour<=23):
    print("\nGet that SLEEP. And rePEAT!\n")
else:
    print("\nYou didn't type and acceptable value! (0-23)\n")
