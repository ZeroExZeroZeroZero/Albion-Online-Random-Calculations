#
#Make an tool that calculates tool tip damage per second
#Author 0x000
#Date 30.12.2020
#

WepName = input("Enter Weapon:")
WepDamage = input("Enter Damage:")
WepTimeUsed = input("Enter Cast Time:")
WepTimeReset = input("Enter Cool Down Time:")
#Getting User input

WepDamageNum = int(WepDamage)
WepUsedNum = int(WepTimeUsed)
WepResetNum = int(WepTimeReset)
#Converting user input

print("\033[H\033[J")
#Creating space between the output and input


DpsTimeRestraint = WepResetNum + WepUsedNum
#Calculating the total time restraints

TotalDps = WepDamageNum / DpsTimeRestraint
#Calculating total Damage Per Second

TotalDpm = TotalDps * 60
#Converting Damage Per Second Into Damage Per min

print("Weapon Name = : " + WepName)
print("Dps = : " + str(TotalDps))
print("Dpm = : " + str(TotalDpm))
#Printing everything to the screen


f = open("demofile.txt", "a")
#opening the file

f.write(WepName + " ")
f.write("Dps = : " + str(TotalDps) + " ")
f.write("Dpm = : " + str(TotalDpm) + "\n")
#Adding data to the file

f.close()
#Closing the file
