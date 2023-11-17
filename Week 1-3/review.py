print("What should you do today?")

action = input()

print("Do you have free time?")

time = input()

if (action == "relax") and (time == "yes"):
    print("You have time to relax then!")

elif (action == "i dont know") or (time == "no"):
    print("You could do some work")
    response = input()
    if response == "no":
        print("Well work it out then")
    else:
        print("Have fun working!")

else:
    print("If you have free time and no work to do then you can do what you want")