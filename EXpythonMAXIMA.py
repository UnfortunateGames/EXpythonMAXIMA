# ex - PYTHON - maxima

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

# Your Stats

weapons = {
    "bow": {
        "level": 1,
        "DMG": 2,
        "critX": 2
    },
    "sword": {
        "level": 1,
        "DMG": 4,
        "critX": 1
    }
}

armor = {
    "chainmail": {
        "level": 1,
        "AR": 2,
        "block": 5
    }
}

inventory = []

curlocation = {"locNumber": 0, "locName": "towns"}

BattleStats = {"HP": 15, "MP": 10, "DMG": 1, "critX": 1, "AR": 1, "RNGDMG": 4, "block": 0}

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

wild = {
    "Grasslands": {
        "enemies": [rabbit, deer, bandit],
        "leave": ["village", "Forest"],
    },
    "Forest": {
        "enemies": [], 
        "leave": ["Grasslands", "Caverns"]
    },
},

# Functions

# Essential

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def wait(n):
    time.sleep(n)

# Calculation

def calculateStats():
    global LevelMaxStats, BattleStats
    level = PersonalStats["level"]
    LevelMaxStats["MAXHP"] = level * 5 + 10
    LevelMaxStats["MAXMP"] = level + 5 * 2
    LevelMaxStats["MAXEXP"] = level * 20 + random.randint(0, level)
    BattleStats["DMG"] = level * 2
    BattleStats["AR"] = level * 1.5
    BattleStats["RNGDMG"] = level * 2 + random.randint(0, 5)

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
    print(f"\tG]-{G} [S]-{S} [B]-{B}\t\t-.-.-.-./__  / (:")
    print(f"\tLV: {level} EXP: {exp}/{maxexp}\t\t\t MAXIMA\t  / /  :)")
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

def loadSave():
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

def LOADorSAVE():
    x = input("\n\t\t[ Load a save? Or Start anew? ]\n\t\t>> ( load/new ) ")
    if x == "load":
        loadSave()
    elif x == "new":
        firstBattles()
    else:
        print("\n\n\tInvalid input!")
        LOADorSAVE()

# Battle System

def HealStats():
    global BattleStats, LevelMaxStats
    BattleStats["HP"] = LevelMaxStats["MAXHP"]
    BattleStats["MP"] = LevelMaxStats["MAXMP"]

def getDream():
    # TODO Work on this feature!
    print("\n\n\t\t\tYou walk through the Grasslands")
    wait(2)
    print("\t\t\tYou wonder...")
    wait(2)
    print("\t\t\tIs killing every monster worth it?")
    wait(2)
    print("\t\t\tThen a revelation comes to your mind")
    wait(2)
    print("\t\t\tWhat if...", end="", flush=True)
    wait(1)
    print("\t\t\tEverything is...")

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
    dmg = BattleStats["DMG"]
    rng = BattleStats["RNGDMG"]
    clear()
    loadEnemy(enemy)
    print(
        f"\n\t\tActions:\n\n\t[ ATTACK ]\n\n\t[ MAGIC ]\n\n\t[ RUN ]\n\t>> ( {runchance}% )"
    )
    x = input("\n\t\tChoose an action - ").strip().lower()
    if x == "attack":
        critchance = random.randint(0, 10)
        dealtdmg = dmg + random.randint(0, int(rng))
        if critchance >= 7:
            dealtdmg = dealtdmg * 2
        if enemy["AR"] == 0:
            donedmg = dealtdmg
            enemy["HP"] -= dealtdmg
        else:
            donedmg = dealtdmg - enemy["AR"] // 2
            enemy["HP"] -= donedmg
        clear()
        loadEnemy(enemy, 1)
        print(f"\n\n\tYou dealt {donedmg} damage!")
        if enemy["HP"] <= 0:
            rewardSystem(enemy)
        else:
            wait(2)
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
    input("\n\t\tYou stand for one final trial\n\n\t\tPress enter to battle!")
    BattleSystem(GuardianOfAdventure, False)

def initIntroSequence():
    clear()
    print("\n\n\n\t\tWelcome to exPYTHON")
    wait(2)
    print("\t\tA game made in python")
    wait(3)
    print("\n\t\tBased on a game named 'EXP MINIMA'")
    wait(2)
    print("\t\tBy: Karmatic")
    wait(2)
    print("\n\t\tRead the README.txt for more info")
    wait(2)
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
    wait(2)
    print("\n\t\tThere are many souls to pick.")
    wait(2)
    print("\t\tLet us find, a soul fit for you.")
    wait(3)
    LOADorSAVE()

# Run Code

fakeLoadingScreen()

initIntroSequence()