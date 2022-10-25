# By submitting this assignment, I agree to the following:
#      "Aggies do not lie, cheat, or steal, or tolerate those who do."
#      "I have not given or received any unauthorized aid on this assignment."
# Names: Lindsey Wilkin, Nishi Mishra, Charlie Simpson, and Kai Brown
# Section: 543
# Assignment: Final Project - Game: UwU KnightsQuest 
# Date: November 22, 2020

# Import random for the battle_monster, monster, sayings, get loot, next event functions
from random import randint

#ATTENTION TO ANYONE TRYING TO TEST I HAVE ADDED COLORS -- THEY LOOK TERRIBLE IN REPL run in Spyder .. sorry 

# Catalog of every item in the game
# Items dictionary holds all of the items availible to buy in the shop
items = {"Butter Knife":["weapon",0,0,1,0],
         "T-shirt and Shorts":["armor",0,0,0,0],
         "Jeff healing":["healing",99,0,50,100], 
         "Jeff Weapon":["weapon",99,1,5,0], 
         "Jeff Armor":["armor",99,1,25,1000], 
         "Bread":["healing",2,0,5,2],
         "Rusty Sword":["weapon",2,0,2,5], 
         "Tunic":["armor",3,0,1,5],
         "Witches Potion":["healing",4,0,6,5],
         "Silver Dagger":["weapon",5,0,10,37],
         "Leather Sheaves":["armor",6,0,35,100],
         "Healing Potion":["healing",7,0,60,150],
         "Longsword":["weapon",8,0,20,45], 
         "Bronze Breastplate":["armor",9,0,40,150], 
         "Bottle of Jack Daniels":["healing",10,0,70,200], 
         "Spined Club":["weapon",11,0,25,56], 
         "Iron Breastplate":["armor",12,0,50,200], 
         "Magic Brew":["healing",12,0,80,205], 
         "Legendary Tennis Racket":["weapon",13,0,30,60], 
         "Chestpiece of the Warrior":["armor",14,0,64,210], 
         "Vial of Harmony":["healing",14,0,90,200],
         "Flameblade":["weapon",15,0,40,70],
         "Titanium Breastplate":["armor",16,0,70,310], 
         "Flask of Wisdom":["healing",16,0,80,320], 
         "Jade Cutlass":["weapon",17,0,30,50], 
         "Obsidian Helmet":["armor",18,0,80,320], 
         "Dark Potion":["healing",18,0,100,200],
         "Wizards Instrument":["weapon",19,0,50,75], 
         "Vest of Chains":["armor",20,0,60,80]}
current_monster = None

# list of all of the possible monster names in the game
monster_names = ["Belloc the Ogre", "Sabertooth", "Basilisk", "Hydra", "Troll", 
                  'Abaddon "The Destroyer"', "Madame White Snake", "Kraken","Werewolf",
                  "Cyclops","Knome","Gargoyle","Manticore"]

# The levels list displays all of the levels and the number of events that happens in each
levels = [[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,3],[10,3],[11,3],[12,3],[13,3],[14,3],[15,3],[16,3],[17,3],[18,3],[19,3],[20,3]]

def monster():
    global monster_names
    '''
    This function creates a monster with abilities based on the player's level. 
    The data is put into a list called monster info which is then returned to the calling function. 
    The calling function sets the the result as the current_monster. 

    No input. Output is in list form : 
    indexes refer to the monster's 0 = name, 1 = health, 2 = defense, 3 = XP gain, 4 = gold gain 
    '''

    backup_names = ["Belloc the Ogre", "Sabertooth", "Basilisk", "Hydra", "Troll", 
                     'Abaddon "The Destroyer"', "Madame White Snake", "Kraken","Werewolf",
                     "Cyclops","Knome","Gargoyle","Manticore"] #so names don't run out 
    
    #data[5] = baseline player health
    att_randnum = randint(1,data[2])
    def_randnum = randint(1,data[2]) #dependent on level 
    XP_randnum = randint(8,15)
    
    monster_attack = int((att_randnum/20)*data[5])
    monster_defense = int((def_randnum/20)*(data[5]))-1 #monster defense is changed each call 
    monster_health = int(data[5]*0.75)-10
    
    XP_gained = int((XP_randnum / 10)*(data[2]**(3)) // 7)+1
    gold_gained = int((XP_randnum / 10)*(data[2]**(2.5)) // 7)+1 #more XP than gold  
    
    randname = -1000
    if len(monster_names) >= 2: 
        randname = randint(0, len(monster_names)-1)
    elif len(monster_names) == 1: 
        randname = 0
    elif len(monster_names) == 0:
        monster_names += backup_names #backup is never touched 
        randname = randint(0, len(monster_names)-1) 
        #print("backup names was needed")
    else:
        print("Why are you seeing this")
    
    monster_info = [monster_names[randname], monster_health, monster_defense, XP_gained, gold_gained,monster_attack]
    monster_names.pop(randname)
    
    return monster_info # 0 = name, 1 = health, 2 = defense, 3 = XP gain, 4 = gold gain 

# print_format_table() 
# website: https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#deletion
# print("\x1b[%sm %s \x1b[0m" % ('7;35;40', "Testing")) 
# this tests color changing (it works)

##### These are all the colorful text functions using ANSI escape sequences #####

def purple_black(text): #first color is the text, second color is background -- add as many as you want 
    print("\x1b[%sm%s \x1b[0m" % ('2;35;40', text)) #purple text/black background
def blue_black(text):
    print("\x1b[%sm%s \x1b[0m" % ('2;36;40', text)) #light blue text/black background
def black_red(text):
    print("\033[%sm%s \033[0m" % ('2;30;43', text)) #black text/red background
def white_red(text):
    print("\033[%sm%s \033[0m" % ('2;46;43', text)) #white text/red background
def white_blue(text):
    print("\033[%sm%s \033[0m" % ('2;46;44', text)) #white text/blue background
def white_green(text): 
    print("\033[%sm%s \033[0m" % ('2;46;42', text)) #white text/green background
def yellow_black(text): 
    print("\033[%sm%s \033[0m" % ('1;33;33', text)) #yellow text/black background

def saying():
    '''
    This function creates a list of sayings (random observations/phrases for roleplaying) and returns one random one as a string.'''

    saying_list = ["It is a warm sunny day.", "I am very worried for this next battle", "I heard there is a foul beast lurking around these parts"]
    saying_list += ["Rest your soul, for I will save the day!", "Did you know I have a crew 20 men strong?", "Die, die, off with their heads"]
    saying_list += ["You approach a waterfall", "Enter darkess", "A hawk decides to take your hat. You chase after it, highly disgruntled."]
    saying_list += ["Yo ho off we again on a curious adventure!","You know..I wish I were a unicorn", "Cat got your tongue?"]
    saying_list += ["I am a genius! *Sing-song voice*", "When you can do nothing, what can you do?","Darkness smiles back ;)"]
    saying_list += ["I should hire an apprentice at some point"]
    rand_index = randint(0, len(saying_list)-1)

    return saying_list[rand_index]

def addGold_to_player(gold_amount):
  '''Function takes in an integer for amount of gold to be added. data[1] (refers to player gold amount) is updated accordingly.'''
  data[1] += gold_amount

def removeGold_from_player(gold_amount):
  '''Function takes in an integer for amount of gold to be removed. data[1] (refers to player gold amount) is updated accordingly as long as there enough gold to do so without debt.'''
  if data[1] - gold_amount >= 0: 
      data[1] -= gold_amount
  else:
    data[1] = 0
    print("Shouldn't be removing gold..")

def update_lvl():
  '''Function checks if player is able to level up. If they can, then their level is updated and the user health is increased by 10. These do direct changes to the data array to update values to prepare for the next level'''
  # 50 is the max level. # also add to health 10
  Nextlevel = data[2]**(2.5) + 3 # data[2] is the current level 
  if data[3] >= Nextlevel:
    data[2] += 1 # level  
    data[5] += 10 # baselinehealth
    white_blue("You leveled up to level %d!" % data[2])
    input()

def addXP_to_player(num_XP): 
    '''Function adds XP to player and checks if the player is able to increase their level after their XP increase. data[3] refers to player XP and update_lvl() is called inside'''
    data[3] += num_XP
    update_lvl()

# Save each object in "data" to a file (User will be able to stop the game, and come back to finsih it later)
def save():
  '''This function saves the game as the file UWU_DATA.csv'''
  with open("UwU_DATA.csv", "w") as savefile:
    savefile.write(str(data[0])[1:-1]+"\n")
    for line in data[1:6]:
      savefile.write(str(line)+"\n")
    savefile.write(str(data[6])[1:-1]+"\n")

# USE THIS INSTEAD OF INPUT!
def prompt(*question):
    '''This function checks if the input is valid. You would call it with: prompt("Question text", "Possible answer 1", "Possible answer 2", keep going for as many possible answers exist.) Returns the answer the user selected.'''
    while (True):
        answer = input(question[0])
        for i in question[1:]:
            if (answer == i):
                return(i)
        print("\n\""+ answer + "\" is not a valid response.")


def prompt2(question,answers):
  '''
  Use this version if the number of potenital answers can vary.
  Syntax: prompt("Question text", [all possible answers in this specific instance,2,3,4,5,etc])
  Returns the answer the user selected.
  '''
  while (True):
    answer = str(input(question))
    if answer in answers:
      return(answer)
    print("\n\""+ answer + "\" is not a valid response.")

def shop():
  '''The shop is where the user will come to buy and sell items in their inventory.'''
  shopping = True
  while(shopping):
    print("\n----------------------")
    white_red("LOCAL SHOP")
    shoppo = prompt("Buy items (1) \nSell      (2) \nExit      (3)\nEnter your decision: ","1","2","3") # options for the user to choose from
    if shoppo == "1": # code for buying items(new items are appended to the users data list)
      buying = True
      while(buying):
        print("\n----------------------")
        print("\nItems for sale:")
        currentiems = []
        prompt_index = ["-1"]
        for i in items:
          if items[i][1] <= int(data[2]):
            currentiems.append(i)
            prompt_index.append(str(currentiems.index(i)+1))
            print(i + " (" + str(currentiems.index(i)+1) + ")")
        shoppo = int(prompt2("Enter the number for the item you wish to inspect. \nOr (-1) to return to the shop menu: ",prompt_index))-1
        if shoppo == -2:
          buying = False
        else:
            print(items[currentiems[int(shoppo)]][0])
            if (items[currentiems[int(shoppo)]][0] == "weapon"): # buying weapons
              print("\n----------------------")
              print("\nWeapon name: " + currentiems[shoppo])
              print("Cost: " + str(items[currentiems[shoppo]][4]))
              print("Damage: " + str(items[currentiems[shoppo]][3]))
            elif(items[currentiems[int(shoppo)]][0] == "armor"): # buying armor
              print("\nArmor name: " + str(currentiems[shoppo]))
              print("Cost: " + str(items[currentiems[shoppo]][4]))
              print("Protection Value: " + str(items[currentiems[shoppo]][3]))
            elif(items[currentiems[int(shoppo)]][0] == "healing"): # buying healing
              print("\nHealing name: " + str(currentiems[shoppo]))
              print("Cost: " + str(items[currentiems[shoppo]][4]))
              print("Health restored: " + str(items[currentiems[shoppo]][3]))
            if(prompt("Do you want to buy this for " + str(items[currentiems[shoppo]][4]) + " Gold? (You have " + str(data[1]) + " Gold)" + "\nYes (0), No (1): ","0","1") == "0"):
              if (data[1] >= items[currentiems[shoppo]][4]):
                if len(data[0]) > 22:
                  print("Your inventory is full!") # if you have no room in your inventory for new items, this error statement will be displayed
                else:
                  data[1] -= items[currentiems[shoppo]][4]
                  data[0].append(currentiems[shoppo]) # name of item chosen
                  print("Item bought sucessfully!") # if transaction is successful, this statement willbe displayed
            
              else:
                print("Aye, you no money! Get out of my shop!") # if you don't have enough money to buy something, this error statement will be displayed
              input()
    if shoppo == "2": # code for selling items
        buying = True
        while(buying):
            n = get_inventory_value("Which item would you like to sell? \n(type e to exit): ")
            if (n != "null"):
                e = prompt("Are you sure you want to sell " + data[0][n] + " for " + str(items[data[0][n]][4]//4) + " gold?\n(1) yes, (2), no: ","1","2")
                if e == "1":
                    data[1] += items[data[0][n]][4]//4
                    data[0].remove(data[0][n])
                    input("item sold sucessfully!")
            else:
                buying = False
    if shoppo == "3": # code to leave the shop
        shopping = False

# prints every item in the player's inventory. (aka Data[0])
def viewinventory():
  '''This function prints every item in the inventory and is called in the checkInventory() function.'''
  print("\n----------------------")
  print(f"LEVEL: {data[2]} XP: {data[3]}/{int(data[2]**(2.5) + 3)} GOLD: {data[1]}")
  print("\n--IN HAND--")
  print(f"Primary weapon: {data[0][0]}")
  print(f"Primary: {data[0][1]}")
  white_red("\n--INVENTORY--")
  if len(data[0]) <= 2:
    print("(empty)")
  else:
    for i in range(2,len(data[0])):
      print(f"({i-1}): {data[0][i]}")

def get_inventory_value(action): #does not look through items equipped
    '''Allows the user to look through specific items in their inventory. This function does NOT include the user's equipped items.'''
    index = ["e"]
    white_red("\n--INVENTORY--")
    for i in range(2,len(data[0])):
        index.append(str(i+1))
        print(f"({i+1}): {data[0][i]}")
    try:
        return int(prompt2(action,index))-3
    except:
        return "null"

# asks the user for the value of an item in their inventory and returns that value. action is the question in the prompt.
# check inventory: swap, exit, inspect 
# INCLUDES EQUPITED ITEMS
def get_inventory_value2(action): 
    '''Allows the user to look through specific items in their inventory. This function does include the user's equipped items.'''
    index = ["e"]
    print("\n----------------------")
    white_red("--IN HAND--")
    index.append(str(1))
    print(f"({1}): {data[0][0]}")
    index.append(str(2))
    print(f"({2}): {data[0][1]}")
    white_red("\n--INVENTORY--")
    for i in range(2,len(data[0])):
        index.append(str(i+1))
        print(f"({i+1}): {data[0][i]}")
    if len(data[0]) == 2:
        print("(empty)")
    try:
        return int(prompt2(action,index))-1
    except:
        return "null"

def checkInventory():
    ''' This function allows/prompts the player to inspect or swap items in the inventory. This function calls the swap() and inspect() functions as needed. This mostly presents the menu and navigation options.'''
    choice = "0"
    while choice != "3":
      viewinventory()
      print("\n----------------------")
      choice = prompt("Would you like to: \n(1) Inspect your items \n(2) Swap items in inventory \n(3) Exit\n","1","2","3")
      if choice == "1":
        item_ind = get_inventory_value2("Which item would you like to inspect? ") 
        inspect(item_ind)
      elif choice == "2":
        item_out = int(get_inventory_value2("Enter item #1 which you would like to swap out: ")) 
        item_in = int(get_inventory_value2("Enter item #2 which you would like to to swap in: "))
        if item_in < item_out:
            temp = item_in
            item_in = item_out
            item_out = temp
        swap(item_in, item_out)

def inspect(index):
    '''This function gets the intex in the items array and displays the property of that item via a print statement. '''
    print("\n----------------------")
    print("Name:",data[0][index])
    print("Unlocked at level:",items[data[0][index]][1])
    if items[data[0][index]][0] == "weapon":
        print("Attack value:", items[data[0][index]][3]) 
    elif items[data[0][index]][0] ==  "armor":
        print("Protection value:", items[data[0][index]][3]) 
    elif items[data[0][index]][0] == "healing":
        print("Amount of health this item restores:", items[data[0][index]][3])
    input()
        
def swap(item_in, item_out):
    '''Takes in two indexes, the first one refers to the item being swapped in and the other swapped out. This function allows the user to equip different weapons/armor. This directly changes the data array containing the current armor and weapon equipped.'''
    if data[0][item_out] == data[0][0] and items[data[0][item_in]][0] != "weapon": 
        input("You can't have a non-weapon as your primary weapon...")
    elif data[0][item_out] == data[0][1] and items[data[0][item_in]][0] != "armor":
        input("You can't have non-armor as your armor...")
    else:
        temp = data[0][int(item_in)]
        data[0][int(item_in)] = data[0][int(item_out)]
        data[0][int(item_out)] = temp

#Town menu
def town(x):
    '''The town function welcomes the user and provides options of how to procede into the game. This function is for organization purposes.'''
    print("----------------------")
    if x == 0:
      white_red("Welcome to the town square!")
    else:
      white_red("Welcome back to the town square!")
    return prompt("Venture forth!  (1)\nVisit Shop      (2)\nCheck inventory (3)\nSave & Quit     (4)\nEnter your decision: ","1","2","3","4") # gives the user a choice of how to procede


# =============================================================================
                        # Dungeon Functions #
# =============================================================================

def getLoot():
    '''This function will be one of the three functions called in the next event function. If called, the user will gain a randomized amount of loot in the dungeon.'''
    chance_randnum = randint(1,4)
    amount_randnum = randint(2,7) 
    if chance_randnum == 1: # 25% chance 
        XP = int((amount_randnum/10)*(data[2]**2.5) // 7)+1
        addXP_to_player(XP)
        yellow_black("You found " + str(XP) + " XP!\n")
    else: # 75% chance 
        gold = int((amount_randnum/10)*(data[2]**2.5) // 7)+1
        addGold_to_player(gold)  
        yellow_black("You found " + str(gold) + " gold!\n")

# Function to decide the next event. (50% chance saying, 12% loot, 38% monster) 
# pauses after each event. The player can check inventory if they want.

def battle_monster(): # monster battle stats
    '''This function determines the monster's attacks and defense for the current level.'''
    e = [0,0,0,0]
    for i in range(2):
      choice = randint(0,3)
      e[choice]+=1
    return e
     
def battle_user(): # user battle stats
    '''This function determines the users attacks for the current level.'''
    e = [0,0,0,0,0,0]
    white_green("You have "+ str(data[4]) + " out of " + str(data[5]) + " health points remaining.")
    print("Pick three choices, you can pick the same choice mulitple times")
    healing = []
    menuhealingaddition = ""
    menuhealingadditionnum = 6
    for n in range(len(data[0])):
      if items[data[0][n]][0] == "healing":
        if not (data[0][n] in healing):
          healing.append(data[0][n])
          menuhealingaddition += f"\n({menuhealingadditionnum}) use {data[0][n]}"
          menuhealingadditionnum += 1
    # the user will be prompted to choose their attack and defense options 
    print("(1) Attempt Risky Attack\n(2) Attempt Weak Attack\n(3) Protect Your Left\n(4) Protect Your Right\n(5) Protect your Back" + menuhealingaddition)
    choices = ["1","2","3","4","5"]
    for i in range(menuhealingadditionnum-6):
      choices.append(str(i+6))
    for i in range(3):
      e[int(prompt2("",choices))-1]+=1
    return e

def battle():
    '''This function runs the monster battles. The code matches up all of the possible outcomes of monster/user attacks and defenses and prints a statement to the user. The math behind monster/user attacks and defenses are also calculated in this code.'''
    global dead
    current_monster = monster()
    # [monster_names[randname], monster_health, monster_defense, XP_gained, gold_gained, attack]
    print()
    white_blue("A " + current_monster[0] + " appears!")
    input()
    
    while (data[4] > 0 and current_monster[1] > 0):
      # print("testing purposes:",current_monster)
      print(f"{current_monster[0]} has {current_monster[1]} health remaining")
      user_input = battle_user()
      # [Risky attack, Weak attack, protect left, protect right, protect back,healing]
      mon_input = battle_monster()
      # [defend, attack left, attack right, attack back]
      # print("testing purposes:",user_input)
      # print("testing purposes:",mon_input)
      plyerdamage = 0
      mondamage = 0
      while user_input[0]+user_input[1] > 0 or mon_input[1]+mon_input[2]+mon_input[3] > 0:
        # the following if-elif-else series defines the diffent types of outcomes for the monster's randomized data choices and the user's choices
        if(mon_input[1] > 0):
          mon_input[1]-=1
          if(user_input[2] > 0):
            print(f"The {current_monster[0]} tried for an attack on the left, but you dodged it!")
            input()
          elif():
            print(f"The {current_monster[0]} suprised you on the left! You took damage!")
            
            plyerdamage+=(current_monster[5]-items[data[0][1]][3])
            print(f"monster attack ({current_monster[5]}) - armor protection ({items[data[0][1]][3]}) = total damage ({plyerdamage})")
            input()
        elif(mon_input[2] > 0):
          mon_input[2]-=1
          if(user_input[3] > 0):
            print(f"The {current_monster[0]} attemped an attack on the right, but you dodged it!")
            input()
          else:
            print(f"The {current_monster[0]} attacked your weak spot on the right! You took damage!")
            
            plyerdamage+=(current_monster[5]-items[data[0][1]][3])
            print(f"monster attack ({current_monster[5]}) - armor protection ({items[data[0][1]][3]}) = total damage ({plyerdamage})")
            input()
        elif(mon_input[3] > 0):
          mon_input[3]-=1
          if(user_input[4] > 0):
            print(f"The {current_monster[0]} went for a back attack, but You dodged it!")
            input()
          else:
            print(f"The {current_monster[0]} out-smarted you with an attack to the back! You took damage!")
            
            plyerdamage+=(current_monster[5]-items[data[0][1]][3])
            print(f"monster attack ({current_monster[5]}) - armor protection ({items[data[0][1]][3]}) = total damage ({plyerdamage})")
            input()
        elif(user_input[0] > 0):
          user_input[0]-=1
          if(mon_input[0] > 0):
            print(f"You went for a risky attack but the {current_monster[0]} saw it coming! Your attack was used against you!")
            plyerdamage+=(current_monster[5]-items[data[0][1]][3])
            print(f"monster attack ({current_monster[5]}) - armor protection ({items[data[0][1]][3]}) = total damage ({plyerdamage})")
            input()
            
          else:
            print("Your risky attack paid off! Critical damage!")
            mondamage+=(items[data[0][0]][3]*2-current_monster[2]//2)
            print(f"Weapon damage X 2 ({items[data[0][0]][3]*2}) - Monster armor / 2 ({current_monster[2]//2}) = net attack ({mondamage})") 
            input()
        elif(user_input[1] > 0):
          user_input[1]-=1
          if(mon_input[0] > 0):
            input("Your weak attack was blocked!")
            mon_input[0]-=1
          else:
            print("Your weak attack connected! Damage has been dealt!")
            mondamage+=(items[data[0][0]][3]-current_monster[2])
            print(f"Weapon damage ({items[data[0][0]][3]}) - Monster armor ({current_monster[2]}) = net attack ({mondamage})")
            input()
        else: # for situations in which the user chooses to use healing
          count = 0
          itemlist = []
          itemlistindex = []
          for i in range(5,len(user_input)):
              if user_input[i] > 0:
                  break
              count+=1
          for item in data[0]:
              if items[item][1] == "healing":
                  itemlist.append(item)
                  itemlistindex.append(data[0].index(item))
          print(f"You applied the {itemlist[count]} it healed {items[itemlist[count]][3]} health points")
          input()
          data[4]+=items[itemlist[count]][3]
          if data[4] > data[5]:
              data[4] = data[5]
          data[0].remove(itemlist[count])
      if (plyerdamage < 0):
            plyerdamage = 0
      if (mondamage < 0):
            mondamage = 1
      # displays the user and monster damages so the user can see the effects of their choices
      print(f"Total damage to player: {plyerdamage}")
      print(f"Total damage to monster: {mondamage}")
      data[4]-=plyerdamage
      current_monster[1]-=mondamage
    if(data[4] < 0):
        dead = True
    else: # printed when the monster has no reamining health
        print("You have defeated the monster!")
        yellow_black("You earned " + str(current_monster[4]) + " gold and "+ str(current_monster[3]) + " xp!")
        addGold_to_player(current_monster[4])
        addXP_to_player(current_monster[3])

def dungeon():
    '''This function is the main function of the level. It runs every event.'''
    numlvel = 0
    while data[6][numlvel] != 0:
      numlvel+=1
    print("\n----------------------")
    white_red("You are now entering level " + str(levels[numlvel][0]))
    print()
    turncount = 0
    dead = False
    while (turncount < levels[numlvel][1] or dead):
      nextEvent()
      turncount+=1
    if dead: # if dead
        input("\n--------------------\nYou died!\n--------------------")
        data[4] = data[5]
    else: # if alive
        chance_randnum = randint(2,7)
        XP = int((chance_randnum/10)*(data[2]**2.5) // 7)+1
        chance_randnum2 = randint(2,7)
        Gold = int((chance_randnum2/10)*(data[2]**2.5) // 7)+1
        addXP_to_player(XP)
        addGold_to_player(Gold)
        white_blue("You beat the level! You earned "+ str(Gold) + " Gold and "+ str(XP) +" XP!")
        data[6][numlvel]=1
        save()
        input()

def nextEvent(): # 3 events occur each level, this function defines which type of event will occur
  '''This function decides the next event the user will encounter while in the dungeon.'''
  num = randint(1,100)
  if 1 <= num <= 35:
      purple_black(saying()+"\n") 
  elif 35 < num <= 65:
      getLoot()
  elif 65 < num <= 100:
      battle()
      
# =============================================================================
                        # MAIN CODE #
# =============================================================================

# Lists all of the players stats
data = []

# user promts so that the game will run most effectivly with colorama
print("On Spyder for the colors to properly show please change your background to the darkest black.")
print("\nTo change:\nTools > Preferences > Appearance > Syntax Highlighting Scheme > Create New Scheme > Background (bottom right -- click the color box) > move the color slider to the darkest black")
input("Press any key to continue..")

# prints opening title to the game
white_red("----------------------")
white_red("|                    |")
white_red("|  UWU KnightsQuest  |")
white_red("|                    |")
white_red("----------------------")
purple_black("\n\nThis program's goal is to provide entertainment by immersing the user into a text adventure")
purple_black("You will be prompted to provide choices throughout the game. Follow the prompts.")

# loads save file
if(prompt("Open saved game (o) | Start new game (n): ","o","n") == "o"):
    # See syntax.txt for syntax details
      with open("UwU_DATA.csv", "r") as savefile:
        for i in savefile:
          try:
            data.append(int(i[0:-1]))
          except:
              if len(data) == 0:
                s = i[0:-1].split(",")
                s[0] = s[0][1:-1]
                for j in range(1,len(s)):
                  s[j] = s[j][2:-1]
                data.append(s)
              else:
                s = i[0:-1].split(",")
                for j in range(len(s)):
                    s[j] = int(s[j])
                data.append(s)
          
else:
    # See syntax.txt for syntax details
    data = [["Butter Knife", "T-shirt and Shorts"],0,1,0,20,20,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    save()
    print("\n----------------------\n")
    input("*You awake in your hometown.* (press enter to continue)") # print statements for roleplay
    input("*Today you will become an adventurer.* (press enter to continue)")

# game loop
game = True
x = 0
while(game):
    choice = town(x) 
    if (choice == "1"):
        dungeon()
        x = 0
    elif (choice == "2"):
        shop()
        x = 1
    elif (choice == "3"):
        checkInventory()
        x = 1
    elif (choice == "4"):
        game = False
    else: # used for testing purposed, not important for actual game play
        print("This is an error message. You shouldn't be able to see this!")


save() # save the game for later, can be saved at virtually any point in the game
print("----------------------")
print("Game saved and closed.") # print to the user to show that the game saved 