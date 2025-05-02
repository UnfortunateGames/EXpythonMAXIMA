# ex - PYTHON - maxima

# Dear reader,
# If you're reading this to optimize my code
# I would be grateful you're here, cause this
# code SUCKS! please help me out ok :)

# sorry -ElectricSplash

# Import Libraries

import os
import random
import time

# Variables

# Code Related

STwidth = 32
savefile = "GameFiles/saveFile/save.txt"

# Sprites

GOLsprite = [
    r"   ( )",
    r"  __|__",
    r" /~~+~~\ ",
    r"(-0-*-0-)",
    r" |'.+.'|",
    r"  \___/",
    r"   (#)",
    r"  __|__",
    r" /~~+~~\ ",
    r"(-X-*-X-)",
    r" |'.+.'|",
    r" \'.+.'/",
    r"   ( )",
    r"  __|__",
    r" /--+--\ ",
    r"(-_-*-_-)",
    r" |'.+.'|",
    r"  \___/",
]

GOCsprite = [
    r"   -=-",
    r".---+---.",
    r"(0 ^ ^ 0)",
    r" | -_- |",
    r" \'.-.'/",
    r"  \___/",
    
    r"   -=-",
    r".---+---.",
    r"(> ^ ^ <)",
    r" | -_- |",
    r" |'.-.'|",
    r" \'.-.'/",

    r"   -=-",
    r".---+---.",
    r"(U ^ ^ U)",
    r" | -_- |",
    r" \'.-.'/",
    r"  \___/",
]

GOAsprite = [
    r"  .' '.",
    r"  |. .|",
    r" ( \./ )",
    r"_=======_",
    r"   | |",
    r"  ('_')",

    r"  .' '.",
    r"  |. .|",
    r" ( \./ )",
    r"_=======_",
    r"   | |",
    r"  (>o<)",

    r"  .' '.",
    r"  |. .|",
    r" ( \./ )",
    r"_=======_",
    r"   | |",
    r"  (-_-)",
]

# TODO Enemy sprites missing!

rabbitSprite = []

bedSprite = [
    r".----,_,-||", 
    r"|,..,|-'-||", 
    r"||-------||"
]

villSprite = [
    r"    ';,",
    r"   ___,,",
    r" /\   ||\ ",
    r"/__\_____\ ",
    r"|,,| [ ] |",
    r"||||_____|",
]

townSprite = [
    r" _____",
    r"|oOoOo|',",
    r"|OoOoO|::|",
    r"|oOoOo|::|",
    r"|OoOoO|__|",
    r"' ''  ' ''",
]

castSprite = [
    r"[|__[]__|]",
    r"  |;;;;|",
    r"  |:/\:|",
    r"  |;;;;|",
    r"--'----'--",
    r" '  ''  ' ",
]

shopSprite = [
    r"._",
    r"|\\   __()__",
    r" \\\ |======|",
    r" .\\\.  ||",
    r" '-,o,' ||",
    r"    \\  []"
]

# Your Stats

# TODO Get more weapons

weapons = {
    "Hbow": {
        "name": "Hunter's Bow",
        "DMG": 2,
        "critX": 2
    },
    "Isword": {
        "name":"Iron Sword",
        "DMG": 4,
        "critX": 1
    }

    # TODO more weapons
}

armors = {
    "chainmail": {
        "name": "Chainmail",
        "defense": 2,
        "block": 2
    }

    # TODO more armors
}

curGear = []

inventory = []

curlocation = {"locNumber": 0, "locName": "towns"}

BattleStats = {"HP": 15, "MP": 10, "DMG": 2, "AR": 1, "RNGDMG": 3, "block": 2}

PersonalStats = {"Name": "Adventurer", "EXP": 0, "B": 0, "level": 1}

LevelMaxStats = {"MAXHP": 15, "MAXMP": 10, "MAXEXP": 20}

# Enemy Stats

GuardianOfLife = {
    "HP": 10,
    "MAXHP": 10,
    "AR": 0,
    "DMG": 2,
    "RNGDMG": 3,
    "EXP": 20,
    "B": 30,
    "level": 1,
    "sprite": GOLsprite,
}

GuardianOfChildhood = {
    "HP": 15,
    "MAXHP": 15,
    "AR": 2,
    "DMG": 3,
    "RNGDMG": 3,
    "EXP": 40,
    "B": 50,
    "level": 2,
    "sprite": GOCsprite,
}

GuardianOfAdventure = {
    "HP": 20,
    "MAXHP": 20,
    "AR": 2,
    "DMG": 4,
    "RNGDMG": 2,
    "EXP": 60,
    "B": 70,
    "level": 3,
    "sprite": GOAsprite,
}

rabbit = {
    "HP": 10,
    "MAXHP": 10,
    "AR": 1,
    "DMG": 2,
    "RNGDMG": 4,
    "EXP": 30,
    "B": 10,
    "level": 1,
    "sprite": rabbitSprite,
}

deer = {
    "HP": 20,
    "MAXHP": 20,
    "AR": 2,
    "DMG": 2,
    "RNGDMG": 4,
    "EXP": 30,
    "B": 15,
    "level": 3,
    "sprite": rabbitSprite,
}

bandit = {
    "HP": 40,
    "MAXHP": 40,
    "AR": 2,
    "DMG": 4,
    "RNGDMG": 3,
    "EXP": 80,
    "B": 30,
    "level": 4,
    "sprite": rabbitSprite,
}

# Locations

towns = {
    "village": {
        "sprite": villSprite,
        "rest": "Home",
        "shop": "Shop",
        "quest": "Elder",
        "where": ["Grasslands", "town"],
    },
    "town": {
        "sprite": townSprite,
        "rest": "Inn",
        "shop": "Blacksmith",
        "quest": "Mayor",
        "where": ["Village", "Castle"],
    },
    "castle": {
        "sprite": castSprite,
        "tavern": "Tavern",
        "armory": "Armory",
        "king": "King",
        "leave": ["Town", "Wilderness"],
    },
}

shop = ["Hbow", "Isword", "chainmail"]

# TODO add more weapons to add into here

blacksmith = []

royalarmory = []

wild = {
    "Grasslands": {
        "enemies": [rabbit, deer, bandit],
        "leave": ["village", "Forest"],
    },
    "Forest": {
        "enemies": [], 
        "leave": ["Grasslands", "Deep Forest"]
    },
    "Deep Forest": {
        "enemies": [],
        "leave": ["Forest", "Deeper Forest"]
    },
    "Deeper Forest": {
        "enemies": [],
        "leave": ["Deep Forest", "Forest Core"]
    },
    "Forest Core": {
        "enemies": [],
        "leave": ["Deeper Forest"]
    }
},

# Dreams

pathofminima1 = [
    "\n\n\t\t\tYou Walk through the Grasslands...", 
    "\t\t\tYou wonder...", 
    "\t\t\tIs killing every monster worth it?", 
    "\n\t\t\tThen a revelation comes to your mind",
    "\t\t\tWhat if...",
    "\t\t\tEverything is...",
]

dreamlist = [pathofminima1]

# Functions

# Essential

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def wait(n):
    time.sleep(n)

# Calculation

def calculateDMG(target):
    if curGear != []:
        weapon = weapons[curGear[1]]
        wpDMG = weapon["DMG"]
        wpCRIT = weapon["critX"]
    else:
        wpDMG = 0
        wpCRIT = 0
    dealtdmg = BattleStats["DMG"] + random.randint(0, BattleStats["RNGDMG"]) + wpDMG
    clear()
    loadEnemy(target, 1)
    if random.randint(0, 10) >= 7:
        print("Critical Hit!")
        dealtdmg = dealtdmg * round((wpCRIT + 1.5))
        wait(2)
    if target["AR"] > 0:
        dealtdmg -= round(target["AR"] / 2)
    target["HP"] -= int(dealtdmg)
    print(f"You dealt {dealtdmg} damage to the Enemy!")
    wait(1.5)
    print(f"The enemy has {target['HP']} HP left!")
    wait(2)

def calculateStats():
    global LevelMaxStats, BattleStats
    level = PersonalStats["level"]
    BattleStats["DMG"] = round((level * 1.25) + 1)
    BattleStats["AR"] = level
    BattleStats["RNGDMG"] = level + random.randint(0, round(level * 1.5))
    BattleStats["block"] = round(level * 1.5)
    LevelMaxStats["MAXHP"] = level * 2 + 13
    LevelMaxStats["MAXMP"] = level + 9
    LevelMaxStats["MAXEXP"] = level * 15 + (level * 5)

# Game Parts

def drawTopBar():
    B = PersonalStats["B"] % 100
    S = PersonalStats["B"] // 100 % 100
    G = PersonalStats["B"] // 10000
    name = PersonalStats["Name"]
    hp = int(BattleStats["HP"])
    maxhp = LevelMaxStats["MAXHP"]
    mp = BattleStats["MP"]
    maxmp = LevelMaxStats["MAXMP"]
    level = PersonalStats["level"]
    exp = PersonalStats["EXP"]
    maxexp = LevelMaxStats["MAXEXP"]
    print("-." * STwidth, end="")
    print(f"\n\tName: {name}\t\t   EX\t  //ESplash")
    print(f"\tHP: {hp}/{maxhp} MP: {mp}/{maxmp}\t\t PYTHON\t / /__ :)")
    print(f"\t[G]-{G} [S]-{S} [B]-{B}\t\t-.-.-.-./__  / (:")
    print(f"\t{level}LV | {exp}XP/{maxexp}\t\t\t MAXIMA\t  / /  :)")
    print(".-" * STwidth, end="", flush=True)

def fakeLoadingScreen():
    clear()
    print("\n")
    print("Importing Libraries...")
    print("\t>> OS ", end="", flush=True)
    wait(0.5)
    print("\t\t\t[ OK! ]")
    print("\t>> Time ", end="", flush=True)
    wait(0.8)
    print("\t\t[ OK! ]")
    print("\t>> Random ", end="", flush=True)
    wait(0.6)
    print("\t\t[ OK! ]")
    wait(1)
    print("Loading Variables...")
    print("\t>> Code Related ", end="", flush=True)
    wait(0.7)
    print("\t[ OK! ]")
    print("\t>> Your Stats ", end="", flush=True)
    wait(0.4)
    print("\t\t[ OK! ]")
    print("\t>> Enemy Stats ", end="", flush=True)
    wait(1.4)
    print("\t\t[ OK! ]")
    wait(1)
    print("Loading Functions...")
    print("\t>> Essental Functions ", end="", flush=True)
    wait(0.5)
    print("\t[ OK! ]")
    print("\t>> Game Parts ", end="", flush=True)
    wait(1)
    print("\t\t[ OK! ]")
    print("\t>> Intro ", end="", flush=True)
    wait(0.3)
    print("\t\t[ OK! ]")
    print("\t>> Other Stuff ", end="", flush=True)
    wait(1.2)
    print("\t\t[ OK! ]")
    wait(1)

# Save Files

def loadGame():
    # TODO Load Game
    pass

def loadSave():
    # TODO Update this with the new stats
    global PersonalStats, BattleStats, LevelMaxStats
    try:
        with open(savefile, "r") as file:
            data = file.readlines()
            if not data or len(data) < 6:
                raise ValueError("Save file is empty or corrupted.")
            PersonalStats["Name"] = data[0].strip()
            PersonalStats["EXP"] = int(data[1].strip())
            PersonalStats["B"] = int(data[2].strip())
            BattleStats["HP"] = int(data[3].strip())
            BattleStats["MP"] = int(data[4].strip())
            calculateStats()
        print("\n\n\tSave file found!")
        input("\n\t\tContinue?")
        loadGame()
    except FileNotFoundError:
        print("\n\n\tSave file not found. Starting a new game.")
        input("\n\t\tContinue?")
        firstBattles()
    except ValueError as e:
        print(f"\n\n\tError: {e}")
        print("\tThe save file is either empty or corrupted.")
        input("\n\t\tContinue?")
        firstBattles()
    except Exception as e:
        print(f"\n\n\tAn unexpected error occurred: {e}")
        input("\n\t\tContinue?")
        firstBattles()

def saveGame():
    with open(savefile, "w") as file:
        file.write(f"{PersonalStats['Name']}\n")
        file.write(f"{PersonalStats['EXP']}\n")
        file.write(f"{PersonalStats['B']}\n")
        file.write(f"{BattleStats['HP']}\n")
        file.write(f"{BattleStats['MP']}\n")
        file.write(f"{PersonalStats['level']}\n")

# Battle System

def HealStats():
    global BattleStats, LevelMaxStats
    BattleStats["HP"] = LevelMaxStats["MAXHP"]
    BattleStats["MP"] = LevelMaxStats["MAXMP"]

def getDream():
    dreamRNG = random.randint(0, 10)
    dream = dreamlist[dreamRNG]
    for line in dream:
        print(line, end="", flush=True)
        wait(1.5)

def restPlace(n):
    if n == 0:
        drawTopBar()
        print("\n\n")
        for sprite in range(0, 5):
            print("\t\t\t" + bedSprite[sprite])
        print("\t\t < Your own abode. >\n\n\t[ Sleep ] [ Exit ]")
        x = input("\n\n\t\tChoose an action - ").strip().lower()
        if x == "sleep":
            chancetodream = random.randint(0, 20)
            clear()
            drawTopBar()
            print("\n\n\tEating... ", end="", flush=True)
            wait(2)
            print("Drinking... ", end="", flush=True)
            wait(2)
            print("Sleeping... ", end="", flush=True)
            wait(1.5)
            if chancetodream >= 13:
                clear()
                drawTopBar()
                print("\n\n\t\tYou begin to dream...")
                wait(2)
                getDream()
                wait(2)
                print("\n\n\t\tEverything fades, and you feel to wake...", end="", flush="")
            wait(1.5)
            print("Waking up... ", end="", flush=True)
    elif n == 1:
        pass
    if n == 2:
        pass

def equipQ(item):
    global curGear
    x = input("\n\t\t[ Equip or Put in inventory? (E/I) ] >> ").lower
    if x == "I":
        inventory.append(item)
        
    elif x == "E":
        inventory.append(item)
        curGear = item


def shopMenu(x, n=1):
    clear()
    drawTopBar()
    print("\n\n")
    for sprite in range(len(x)):
        print("\t\t\t" + x[sprite])
    if n == 1:
        menu = shop
    elif n == 2:
        menu = blacksmith
    elif n == 3:
        menu = royalarmory
    wp1 = weapons[menu[0]]
    wp2 = weapons[menu[1]]
    ar1 = armors[menu[2]]
    print(f"\n\t\t     [ Choose an item ]\n\t  [ {wp1["name"]} ] [ {wp2["name"]} ] [ {ar1["name"]} ]")
    x = input("\n\t\t[ Pick an item ] >> ").lower()
    if x == wp1["name"].lower():
        clear()
        drawTopBar()
        print(f"\n\t\tYou have chosen the {wp1['name']}")
        wait(2)
        equipQ(wp1)
    elif x == wp2["name"].lower():
        clear()
        drawTopBar()
        print(f"\n\t\tYou have chosen the {wp2['name']}")
        wait(2)
        equipQ(wp2)
    elif x == ar1["name"].lower():
        clear()
        drawTopBar()
        print(f"\n\t\tYou have chosen the {ar1['name']}")
        wait(2)
        equipQ(ar1)
    elif x == "exit":
        
        drawLocation()
    else:
        print(f"\n\t\t[ {x} is not an item! ]")
        wait(2)
        shopMenu(x, n)

def drawLocation():
    if curlocation["locName"] == "village":
        if curlocation["locNumber"] == 0:
            loc = towns["village"]
        elif curlocation["locNumber"] == 1:
            loc = towns["town"]
        elif curlocation["locNumber"] == 2:
            loc = towns["castle"]
    elif curlocation["locName"] == "wild":
        if curlocation["locNumber"] == 0:
            pass
        elif curlocation["locNumber"] == 1:
            pass
        elif curlocation["locNumber"] == 2:
            pass
    spritesheet = loc["sprite"]
    drawTopBar()
    print("\n\n")
    for sprite in range(0, len(spritesheet)):
        print("\t\t" + spritesheet[sprite])
    rest = loc["rest"]
    shop = loc["shop"]
    quest = loc["quest"]
    print(
        f"\n\n\t\t[ CHOOSE A PLACE ]\n\t( {rest} )\t( {quest} )\n\t( Leave )\t( {shop} )"
    )
    x = input("\n\t\tWhere do you want to go? > ").strip().lower()
    if loc == "village":
        if x == rest:
            restPlace(curlocation)
        elif x == shop:
            # shop menu
            pass
        elif x == quest:
            # fetch quest
            pass
        elif x == "leave":
            # leave function
            pass
        else:
            print("\n\n\t\t\tThat's not a place...")
            wait(2)
            clear()
            drawLocation()

def loadEnemy(enemy, i=0):
    hp = enemy["HP"]
    maxhp = enemy["MAXHP"]
    localSprite = enemy["sprite"]
    drawTopBar()
    print("\n")
    offset = 6 * i
    for sprite in range(0, offset + 6):
        if sprite >= offset:
            print("\t\t\t" + localSprite[sprite])
    print(f"\n\t\t    [ HP ] {hp} / {maxhp}")

def respawnSystem(r, enemy):
    global curlocation
    if not r:
        clear()
        print("\n\n\t\t\tYou have died...")
        wait(2)
        print("\t\t\tBut it refused to give up!")
        wait(3)
        input("\t\t\tPress enter to retry... ")
        HealStats()
        enemy["HP"] = enemy["MAXHP"]
        BattleSystem(enemy, r)
    else:
        curlocation["locName"] = "village"
        HealStats()
        clear()
        print("\n\n\t\t\tYou have died...")
        wait(2)
        print("\t\t\tIt all starts anew...")
        wait(3)
        input("\t\t\tPress enter to respawn... ")

def enemyChoice(enemy, r):
    enemyRNG = random.randint(0, 100)
    if enemyRNG <= 60:
        enemyDMG = enemy["DMG"] + random.randint(0, enemy["RNGDMG"])
        donedmg = enemyDMG - BattleStats["AR"] // 2
        BattleStats["HP"] -= donedmg
        clear()
        loadEnemy(enemy)
        print(f"\n\n\tThe enemy dealt {int(donedmg)} damage!")
        wait(2)
        if BattleStats["HP"] <= 0:
            respawnSystem(r, enemy)
        else:
            BattleSystem(enemy, r)
    elif enemyRNG <= 90:
        clear()
        loadEnemy(enemy, 2)
        print("\n\n\tThe enemy is resting?")
        wait(1)
        enemy["HP"] += enemy["MAXHP"] // 6
        BattleSystem(enemy, r)
    else:
        clear()
        loadEnemy(enemy)
        print("\n\n\tThe enemy is casting a spell!")
        wait(1)
        enemyDMG = enemy["DMG"] * random.randint(0, 2)
        BattleStats["HP"] -= enemyDMG
        clear()
        loadEnemy(enemy)
        print(f"\n\n\tThe enemy dealt {int(enemyDMG)} damage!")
        wait(2)
        if BattleStats["HP"] <= 0:
            respawnSystem()
        else:
            BattleSystem(enemy, r)

def LevelupSystem():
    clear()
    global PersonalStats, LevelMaxStats
    if PersonalStats["EXP"] >= LevelMaxStats["MAXEXP"]:
        PersonalStats["EXP"] = 0
        PersonalStats["level"] += 1
        calculateStats()
        drawTopBar()
        print("\n\n\t\t\tYou leveled up!")
        wait(2)
        input("\n\t\t\tPress enter to continue...")

def rewardSystem(enemy):
    clear()
    loadEnemy(enemy, 1)
    print("\n\n\tYou defeated the enemy!")
    wait(1)
    PersonalStats["EXP"] += enemy["EXP"]
    PersonalStats["B"] += enemy["B"]
    print(f"\n\tYou gained {enemy['EXP']} EXP and {enemy['B']} Bronze!")
    wait(1)
    input("\n\tPress Enter to continue...")
    LevelupSystem()

def BattleSystem(enemy, r=True):
    global BattleStats
    if r:
        runchance = 60 // enemy["level"] * 1.5
    else:
        runchance = 0
    mp = BattleStats["MP"]
    clear()
    loadEnemy(enemy)
    print(
        f"\n\t\tActions:\n\n\t[ ATTACK ]\n\n\t[ MAGIC ]\n\n\t[ RUN ]\n\t>> ( {runchance}% )"
    )
    x = input("\n\t\tChoose an action - ").lower()
    if x == "attack":
        calculateDMG(enemy)
        if enemy["HP"] <= 0:
            rewardSystem(enemy)
        else:
            enemyChoice(enemy, r)
    elif x == "magic":
        clear()
        loadEnemy(enemy)
        print(f"\n\t\tYou have {mp} MP left.")
        # Print magic spells function
        input("Choose a spell - ")
        # returns to main actions since no magic spells yet
        BattleSystem(enemy, r)
    elif x == "run":
        chance = random.randint(0, 100)
        clear()
        loadEnemy(enemy)
        if chance <= runchance:
            loadEnemy(enemy)
            print("\n\n\tYou ran away!")
            wait(2)
        else:
            loadEnemy(enemy)
            print("\n\n\tYou couldn't run away!")
            wait(2)
            enemyChoice(enemy, r)
    else:
        clear()
        loadEnemy(enemy)
        print(f"\n\n\t{x} is an invalid action!")
        wait(2)
        BattleSystem(enemy, r)

# Story Related

def firstBattles():
    clear()
    drawTopBar()
    print("\n\n\t\t\tYou are born.")
    wait(2)
    print("\n\tYou see 3 Guardians blocking your journey.")
    wait(3)
    print("\tThe first you encounter is the Guardian of Life.")
    wait(2)
    input("\n\t\t\tPress Enter to fight!")
    BattleSystem(GuardianOfLife, False)
    clear()
    drawTopBar()
    print("\n\n\t\tYou have advanced through your life.")
    HealStats()
    wait(2)
    print("\t\tThe second Guardian is approaching.")
    wait(2)
    print("\t\tThe Guardian of Childhood.")
    input("\n\t\tPress Enter to fight!")
    BattleSystem(GuardianOfChildhood, False)
    clear()
    drawTopBar()
    print("\n\n\t\tYou progressed through childhood.")
    HealStats()
    wait(2)
    print("\n\t\tLonging for adventure")
    wait(2)
    print("\t\tYou meet the final Guardian.")
    wait(2)
    print("\n\t\tIt challenges you to test your skills.")
    wait(2)
    print("He gives you two weapons of choice...")
    wait(2)
    print("How do you wish to be armed?")
    wait(1)
    for _ in weapons:
        x = input("A Sword or a Bow? > ").strip().lower()
        if x == "sword":
            curGear.append("sword")
            break
        elif x == "bow":
            curGear.append("bow")
            break
        else:
            print("\n\n\tInvalid input!")
    BattleSystem(GuardianOfAdventure, False)

def initIntroSequence():
    clear()
    print("\n\n\n\t\tWelcome to exPYTHON")
    wait(1.5)
    print("\t\tA game made in python")
    wait(2)
    print("\n\t\tBased on a game named 'EXP MINIMA'")
    wait(1.5)
    print("\t\tBy: Karmatic")
    wait(1.5)
    print("\n\t\tRead the README.txt for more info")
    wait(1.5)
    input("\n\t\tPress enter to continue...")
    clear()
    for _ in range(0, STwidth):
        print("-", end="", flush=True)
        wait(0.02)
        print(".", end="", flush=True)
        wait(0.02)
    print("\n\n\n")
    for _ in range(0, STwidth):
        print(".", end="", flush=True)
        wait(0.02)
        print("-", end="", flush=True)
        wait(0.02)
    clear()
    drawTopBar()
    wait(2)
    print("\n\n\t\tYou are about to enter")
    print("\t\tthe world of MAXIMA.")
    wait(1.5)
    print("\n\t\tThere are many souls to pick.")
    wait(1.5)
    print("\t\tLet us find, a soul fit for you.")
    wait(2)
    while True:
        x = input("\n\t\t[ Load a save? Or Start anew? ]\n\t\t>> ( load/new ) ")
        if x == "load":
            loadSave()
            break
        elif x == "new":
            firstBattles()
            saveGame()
            break
        else:
            print("\n\n\tInvalid input!")
    loadGame()

# Run Code

# fakeLoadingScreen()
# initIntroSequence()

BattleSystem(GuardianOfLife, False)