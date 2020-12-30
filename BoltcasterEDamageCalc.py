#
#Make an application that calculates the boltcaster damage from deathward climax
#Author 0x000
#Date 30.12.2020
#

BaseEDamage = input("Boltcasters Base E damage : ")
#Taking User input for E damage

WepDamageNum = int(BaseEDamage)
#Converting User input into usable data

TotalEDamage = (WepDamageNum * 1) + (WepDamageNum * 2) + (WepDamageNum * 3) + (WepDamageNum * 4) + (WepDamageNum * 5) + (WepDamageNum * 6) + (WepDamageNum * 7) + (WepDamageNum * 8) + (WepDamageNum * 9) + (WepDamageNum * 10) + (WepDamageNum * 11) + (WepDamageNum * 12) + (WepDamageNum * 12)
#Inefficient way of calculating boltcaster E damage

print("Total E damage = " + str(TotalEDamage))
#Printing Boltcaster E damage
