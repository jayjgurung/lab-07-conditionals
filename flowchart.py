move = input("\nDoes it move? (yes/no)\n")  
if move == "yes":
  should = input("\nShould it? (yes/no) \n")
  if should == "yes":
    print("\nNo problem\n")
  elif should == "no":
    print("\nUse a duct tape!\n")
  else:
    print("\nInvalid response! You didn't type yes or no.")
elif move == "no":
    should = input("\nShould it? (yes/no) \n")
    if should == "yes":
        print("\nYou should use WD-40\n")
    elif should == "no":
        print("\nNo problem!\n")
    else:
        print("\nInvalid response! You didn't type yes or no.")
else:
    print("\nInvalid response! You didn't type yes or no.\n")