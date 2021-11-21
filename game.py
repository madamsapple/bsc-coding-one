import random

taskandtime = {
    "wake up" : str(random.randint(6,7)) + ":" + str(random.randint(0, 3)) + str(random.randint(0, 9)) + " AM",
    "breakfast" : "7:" + str(random.randint(45, 59)) + " AM",
    "rollcall" : "9:" + str(random.randint(45, 50)) + " AM",
    "escorting" : "9:" + str(random.randint(50,59)) or "10:" + str(random.randint(0, 1) + str(random.randint(0, 5))) + " AM",
    "lunch" : "1:" + str(random.randint(30, 45)) + " PM",
    "walkbyward" : "2:" + str(random.randint(15, 30)) + " PM",
    "phonecalls" : "2:" + str(random.randint(35, 45)) + " PM",
    "selfhelp" : "3:" + str(random.randint(15, 30)) + " PM",
    "relgmeet" : "4:" + ((str(random.randint(0,1)) + str(random.randint(0,5))) or ("0" + str(random.randint(6,9)))) + " PM",
    "exercise" : "5:00 PM",
    "cleaning" : "7:" + (("0" + str(random.randint(0,9))) or (str(random.randint(10,15)))) + " PM",
    "supper" : "7:" + str(random.randint(16, 30)) + " PM",
    "lightsout" : ("8:" + str(random.randint(30,59))) or ("9:" + (("0" + str(random.randint(0,9))) or (str(random.randint(10,30))))) + " PM"

}

print(taskandtime)


print("{} {} is great".format("ice", "cream"))