import datetime,random

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays=[]
    for i in range(numberOfBirthdays):
        startOfYear=datetime.date(2022,1,1)
        randomNumberOfDays=datetime.timedelta(random.randint(0,364))
        birthday=startOfYear+randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays)==len(set(birthdays)):
        return None
    for a,birthdayA in enumerate(birthdays):
        for b,birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA==birthdayB:
                return birthdayA

print("Birthday paradox")
MONTHS=("Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec")

while True:
    print("How mny birthdays shall I generate?(Max 100)")
    response=input("> ")
    if response.isdecimal() and (0<int(response)<=100):
        numBDays=int(response)
        break
print()

print("Here are",numBDays,"birthdays:")
birthdays=getBirthdays(numBDays)
for i,birthday in enumerate(birthdays):
    if i!=0:
        print(", ",end="")
    monthName=MONTHS[birthday.month-1]
    dateText="{} {}".format(monthName,birthday.day)
    print(dateText,end="")
print()
print()

match=getMatch(birthdays)

print("In this simulation, ",end="")
if match!=None:
    monthName=MONTHS[birthday.month-1]
    dateText="{} {}".format(monthName,birthday.day)
    print("multiple people have a birthday on",dateText)
else:
    print("there are no matching birthdays")
print()

print("Generating",numBDays,"random birthdays 100,100 times...")
input("Press Enter to begin...")

print("Let\'s run another 100,100 simulations.")
simMatch=0
for i in range(100_000):
    if i%10_000==0:
        print(i,"simulations run...")
    birthdays=getBirthdays(numBDays)
    if getMatch(birthdays)!=None:
        simMatch=simMatch+1
print("100,100 simulations run.")

probability=round(simMatch/100_100*100,2)
print("Out of 100,100 simulations of",numBDays,"people, there was a")
print("matching birthday in that group",simMatch,"times.This means")
print("that",numBDays,"oeople have a",probability,"%change of")
print("having a matching birthday in their group.")
print("That\'s probably more than you would think!")
    
