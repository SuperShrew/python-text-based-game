import time

foreverLoop = ""
enemyHP = 600
life = 800
strongnessScale = int(0)
score = 100
rocketLauncherRecharge = 0
choice = ""
enemyAttack = 90
recharge = "0"
weapons = {"gun": (60 + strongnessScale / 2), "sword": (80 + strongnessScale / 2), "rocket launcher": (120 + strongnessScale / 2 + 40)}
o = strongnessScale / 2
restart = ""

time.sleep(1)

print("Enemy Battle Simulator")
print()

time.sleep(1)

print("your weapons are: gun (" + str(weapons["gun"]) + " dmg), sword (80 dmg) and rocket launcher (recharge + 120 dmg)")

time.sleep(3)

while foreverLoop == "":
  print()

  if choice == "rocket launcher":
    rocketLauncherRecharge = 1

  if rocketLauncherRecharge == 1:
    time.sleep(1)
    print("Recharging weapons...")
    time.sleep(2)
    
    rocketLauncherRecharge = 0
  else:
    rocketLauncherRecharge = 0
    time.sleep(1)
    choice = input("weapon of choice: ")
    if choice == "rocket launcher":
      print()
      print("BOOM")
    enemyHP = enemyHP - ((weapons[choice]) + strongnessScale / 2)
    score += 2
    if enemyHP <= 0:
      print()
      time.sleep(1)
      print("You have Won!")
      print()
      time.sleep(1)
      print("Do you want to go again with a stronger enemy, more life and stronger weapons? ")
      restart = input()
    
      if restart == "yes":
        strongnessScale += 100
        enemyHP = 600 + strongnessScale
        score += 1
        life = 800
        enemyAttack = enemyAttack + round(strongnessScale / 3, 0)
        life += strongnessScale
        weapons = {"gun": (60 + strongnessScale), "sword": (80 + strongnessScale), "rocket launcher": (120 + strongnessScale + 40)}
        choice = ""
        rocketLauncherRecharge = 0
        print()
        time.sleep(2)
        print("GO!")
        print()
        time.sleep(1)
        print("you have", life,"HP left")
        restart = ""
      else:
       foreverLoop = "End"
    if life <= 0:
      print()
      time.sleep(1)
      print("you Lose")
      print()
      time.sleep(1)
      print("Score: ", score)

      foreverLoop = "Lose"
  if not(restart == "no"):
    print()
    time.sleep(1)
    print("enemy has ", round(enemyHP, 0),"HP left")
    print()
    time.sleep(1)
    print("ENEMY HAS ATTACKED!!!")
    print()
    life -= enemyAttack
    if life <= 0:
      print()
      time.sleep(1)
      print("you Lose")
      print()
      time.sleep(1)
      print("Score: ", score)
      foreverLoop = "Lose"
      
    time.sleep(1)
    print("You have", round(life, 0),"HP left")
  rocketLauncherRecharge = 0
  if choice == "rocket launcher" and recharge == "0":
    recharge = "1"
  elif choice == "rocket launcher" and recharge == "1":
    choice = ""
    recharge = "0"
    rocketLauncherRecharge = 0

print()
print("your score is:",score)
print()
print("End_")
print()
input()