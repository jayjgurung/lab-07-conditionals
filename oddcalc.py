firstNum = input("\nEnter a value for first number:\n")
secondNum = input("\nEnter a value for second number:\n")
operation = input("\nWhat kind of operation do you want?\n* mul\n* div\n* mod\n\n: ")
if (operation=="mul"):
    answer = float(firstNum)*float(secondNum)
    print("\n"+str(firstNum)+"x"+str(secondNum)+" is : "+str(answer)+"\n")
elif (operation=="div") :
    answer = float(firstNum)/float(secondNum)
    print("\n"+str(firstNum)+"/"+str(secondNum)+" is : "+str(answer)+"\n")
elif (operation=="mod") :
    answer = float(firstNum)%float(secondNum)
    print("\n"+str(firstNum)+"%"+str(secondNum)+" is : "+str(answer)+"\n")
else :
    print("\ninvalid operation!\n")