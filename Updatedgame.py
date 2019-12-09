from tkinter import *
import random

# --------------------------------------Player-Stats-------------------------------------------------
playerChoice = ""
playerMagicChoice = ""
playerSkillChoice = ""
playerAttack = ""
player = []
playerManaCost = 0
playerDead = "Dead" in player
playerPriority = 0
playerSpellList = ["Frostbite", "Heal", "Light", "Blizzard", "Shine", "Permafrost"]
playerSkillList = ["Frigid Jab", "Wide Sweep", "Light Lance", "Triple Thrust", "Icicle Spear", "Sub-Zero Stab"]
playerDamage = 0
playerHealing = 0

playerHP = 100
playerMaxHP = 100

playerMP = 75
playerMaxMP = 75

playerSP = 80
playerMaxSP = 80

playerSTR = 20
playerBaseSTR = 20

playerDEF = 5
playerBaseDEF = 5

playerSKL = 15
playerBaseSKL = 15

playerMAG = 15
playerBaseMAG = 15

playerRES = 5
playerBaseRES = 5

playerSPD = 15
playerBaseSPD = 15

# ----------------------------------------Computer-Stats---------------------------------------------
cpuChoice = random.randint(1, 2)
cpuAttack = ""
cpu = []
cpuOneName = "Bandit"
cpuDead = "Dead" in cpu
cpuPriority = 0
cpuDamage = 0
cpuHealing = 0
cpuHP = 120
cpuMaxHP = 120

cpuMP = 0
cpuMaxMP = 0

cpuSP = 75
cpuMaxSP = 75

cpuSTR = 15
cpuBaseSTR = 15

cpuDEF = 10
cpuBaseDEF = 10

cpuSKL = 15
cpuBaseSKL = 15

cpuMAG = 5
cpuBaseMAG = 5

cpuRES = 5
cpuBaseRES = 5

cpuSPD = 20
cpuBaseSPD = 20
# -------------------------------------Misc-Stats----------------------------------------------------
speedOrder = [playerPriority, cpuPriority]
placeHolderInt = 0
placeHolderStr = ""
manaCost = 0
staminaCost = 0
userSTR = 0
userMAG = 0
userSKL = 0
userACC = 90
targetDEF = 0
targetRES = 0
targetSPD = 0
freezeCounter = 0
bleedCounterCPU = 0
bleedCounterPlayer = 0
blindCounter = 0
extraDamage = 0


# =========================================Functions=================================

def nameEntered():
    player1 = txt.get()

    res = player1 + " has come face to face with bandit. " + player1 + " must battle"

    menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)

    lbl.configure(text=res)

    nameBtn.destroy()
    txt.destroy()


def removeButtons():
    atkBtn.destroy()
    spellBtn.destory()


def enemyAtk():
    atk = random.randint(1, 3)
    if (atk == 1):
        banditBash()
    if (atk == 2):
        banditPoisonBlade()
    if (atk == 3):
        banditLifeSteal()


def Bash():
    global cpuHP

    damage = random.randint(1, 10)

    enemyAtk()

    cpuHP = cpuHP - damage

    if (cpuHP <= 0):
        res = "You  have won!"
    else:
        res = "Bandit took " + str(damage) + " damage."
        menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)

    lbl.configure(text=res)


def Magic():
    frostbiteBtn = Button(window, text="Frostbite", command=Frostbite)
    healBtn = Button(window, text="Heal", command=Heal)
    lightBtn = Button(window, text="Light", command=Light)
    blizzBtn = Button(window, text="Blizzard", command=Blizzard)
    shineBtn = Button(window, text="Shine", command=Shine)
    permaBtn = Button(window, text="Permafrost", command=Permafrost)

    frostbiteBtn.grid(column=3, row=5)
    healBtn.grid(column=3, row=6)
    lightBtn.grid(column=3, row=7)
    blizzBtn.grid(column=3, row=8)
    permaBtn.grid(column=3, row=9)


def Frostbite():
    global cpuHP
    global playerMP

    if (playerMP < 5):
        res = "Not enough mana!"
    else:
        banditBash()
        damage = random.randint(8, 20)
        playerMP -= playerMP - 5
        cpuHP = cpuHP - damage

        if (cpuHP <= 0):
            res = "You  have won!"
        else:
            res = "Bandit took " + str(damage) + " damage."
            menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
        lbl.configure(text=res)


def Heal():
    global cpuHP
    global playerMP

    if (playerMP < 10):
        res = "Not enough mana !"
    else:
        banditBash()
        damage = 0
        playerMP = playerMP - 10
        playerHp = playerHP + random.randint(0, 10)

        if (cpuHP <= 0):
            res = "You have won!"
        else:
            res = "Bandit took" + str(damage) + " damage."
            menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
        lbl.configure(text=res)

def Light():
    global cpuHP
    global playerMP

    if (playerMP < 5):
        res = "Not enough mana !"
    else:
        banditBash()
        damage = random.randint(5,10)
        playerMP = playerMP - 5
        cpuHP = cpuHP - damage

        if (cpuHP <= 0):
            res = "You have won!"
        else:
            res = "Bandit took" + str(damage) + " damage."
            menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
        lbl.configure(text=res)


def Blizzard():
    global cpuHP
    global playerMP

    if (playerMP < 15):
        res = "Not enough mana !"
    else:
        banditBash()
        damage = random.randint(15,20)
        playerMP = playerMP - 15
        cpuHP = cpuHP - damage

        if (cpuHP <= 0):
            res = "You have won!"
        else:
            res = "Bandit took" + str(damage) + " damage."
            menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
        lbl.configure(text=res)


def Shine():
        global cpuHP
        global playerMP

        if (playerMP < 10):
            res = "Not enough mana !"
        else:
            banditBash()
            damage = random.randint(10,15)
            playerMP = playerMP - 10
            cpuHP = cpuHP - damage

            if (cpuHP <= 0):
                res = "You have won!"
            else:
                res = "Bandit took" + str(damage) + " damage."
                menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
            lbl.configure(text=res)

def Permafrost():
    global cpuHP
    global playerMP

    if (playerMP < 20):
        res = "Not enough mana !"
    else:
        banditBash()
        damage = random.randint(20,30)
        playerMP = playerMP - 20
        cpuHP = cpuHP - damage

        if (cpuHP <= 0):
            res = "You have won!"
        else:
            res = "Bandit took" + str(damage) + " damage."
            menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
        lbl.configure(text=res)
def Skills():
    res = "Hi"

    lbl.configure(text=res)


def banditBash():
    global playerHP

    damage = random.randint(1, 10)

    playerHP -= damage

    if (playerHP <= 0):
        res = "You have died"
    else:
        res = "You took " + str(damage) + " damage."

    lbl3.configure(text=res)
    lbl4.configure(text="")


def banditPoisonBlade():
    global playerHP

    damage = random.randint(7, 10)

    poison = random.randint(1, 3)

    playerHP = playerHP - damage - poison

    if (playerHP <= 0):
        res = "You have died"
        res2 = ""
    else:
        res = "Bandit used Poison Blade. You took " + str(damage) + " damage."
        res2 = "You also take " + str(poison) + " damage from poison"

    lbl3.configure(text=res)
    lbl4.configure(text=res2)


def banditLifeSteal():
    global playerHP
    global cpuHP

    damage = random.randint(7, 15)
    heal = damage / 2
    cpuHP += heal
    playerHP -= damage

    res = "You took " + str(damage) + " damage."
    res2 = "Bandit healed for " + str(heal) + " life."
    lbl3.configure(text=res)
    lbl4.configure(text=res2)


def menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice):
    if (playerHP <= 0):
        lbl.configure(text="You have lost")
        lbl2.configure(text="")
        lbl3.configure(text="")
        lbl4.configure(text="")
        atkButton.destroy()
    elif (cpuHP <= 0):
        lbl.configure(text="You have won")
        lbl2.configure(text="")
        lbl3.configure(text="")
        lbl4.configure(text="")
        atkButton.destroy()
    else:
        res = "You: HP:" + str(playerHP) + " MP: " + str(playerMP) + " SP: " + str(playerSP)
        res2 = "Bandit: HP:" + str(cpuHP) + " MP: " + str(cpuMP) + " SP: " + str(cpuSP)

        lbl5.configure(text=res)
        lbl6.configure(text=res2)

        menuChoice()


def menuChoice():
    atkBtn = Button(window, text="Attack", command=Bash)
    mgcBtn = Button(window, text="Magic", command=Magic)

    atkBtn.grid(column=1, row=4)
    mgcBtn.grid(column=2, row=4)


def battle():
    menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)


# ==================Gui==============================#

window = Tk()

window.title("The Game")

window.geometry('500x500')

lbl = Label(window, text="Enter your name: ")

lbl2 = Label(window, text="")

lbl3 = Label(window, text="")

lbl4 = Label(window, text="")

lbl5 = Label(window, text="")

lbl6 = Label(window, text="")

lbl.grid(column=0, row=0)

lbl2.grid(column=0, row=1)

lbl3.grid(column=0, row=2)

lbl4.grid(column=0, row=3)

lbl5.grid(column=0, row=4)

lbl6.grid(column=0, row=5)

txt = Entry(window, width=10)

txt.grid(column=1, row=0)

nameBtn = Button(window, text="Enter", command=nameEntered)

nameBtn.grid(column=2, row=0)

window.mainloop()
