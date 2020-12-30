#
#Make an tool that does real damage calculations in albion online
#Author 0x000
#Date 30.12.2020
#

#Start
WepName = input("Enter Weapon: ")
WepDamage = input("Enter Tool Tip Damage: ")
WepDmgReduction = input("Enter Damage Reduction percent: %")
WepDmgMulti = input("Enter Your Armour bonus: %")
#Requesting data from user


DmgReductionPercent = float(WepDmgReduction) / 100
DmgmultiPercent = (float(WepDmgMulti) / 100) + 1
#Converting Data into usable numbers


WepDmgPostReduction = float(WepDamage) * float(DmgReductionPercent)
#Calculating the damage with the reduction


WepDmgPostReduction = round(WepDmgPostReduction)
#Making the damage number with reduction look nice


WepDmgFinalCalc = WepDmgPostReduction * DmgmultiPercent
#Calculating the total damage with armour bonuses


print("The real damage number you should do is : " + str(WepDmgFinalCalc))
#Displaying the real damage you should do
