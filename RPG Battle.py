import random
from tkinter import*
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

messagebox.showinfo (" Hello, we are going to play an RPG game!",
                     " You'll have to make decisions throughout the game" +\
                     " so be sure to read and respond carefully!"+\
                     " All of your anwsers will be numbers, so be sure"+\
                     " to read what they correspond to. I hope you have fun!")
                    
messagebox.showinfo (" Which class would you like to be?",
                      " You can choose from a Fighter," +\
                      " Mage, Druid, or a Commoner")  

player = simpledialog.askinteger (" Please type the number corresponding to your desired class.",
                                " For Fighter, press 1. " +\
                                " For Mage, press 2. " +\
                                " For Druid, press 3." +\
                                " Or for Commoner, press 4.")
                         
                         
                         
                         
#classes

if player == 1:
    health = random.randint (20, 30)
    damage = random.randint (5, 25)
    luck = random.randint (0, 15)
    special = random.randint (10, 20)
    messagebox.showinfo (" You are now a Fighter.",
                         " Good choice! As a fighter you will have" +\
                         " between 20 and 30 health, higher than any" +\
                         " other class! You have the highest damage range, " +\
                         " but your luck is a bit lacking.")
    
                          
                         

                      
elif player == 2:
    health = random.randint (10, 20)
    damage = random.randint (15, 20)
    luck = random.randint (0, 20)
    special = random.randint (20, 20)
    messagebox.showinfo (" You are now a Mage.",
                         " Nice choice! Your health will be" +\
                         " pretty low, but you are always" +\
                         " going to do at least 15 damage! " +\
                         " Just try not to get hurt too much.") 




elif player == 3:
    health = random.randint (15, 20)
    damage = random.randint (10, 15)
    luck = random.randint (5, 15)
    special = random.randint (15, 20)
    messagebox.showinfo (" YEAY you're a Druid!!",
                         " Great choice! Your health will be pretty average," +\
                         " you're always going to do at least 10 damage," +\
                         " and you're luck is the second best!")


elif player == 4:
    health = random.randint(5, 10)
    damage = random.randint (0, 10)
    luck = random.randint (0, 25)
    special = (10,10)
    messagebox.showinfo ("Oh someone actually choose Commoner...",
                         " Ummm good choice I guess... As the commoner you have the " +\
                         " lowest health, and damage, but your luck is the highest. The" +\
                         " highest damage you can do is 10... and the highest health  " +\
                         " you can have is 10 as well... I'm sure you can do it though!")


#First battle
wolfdmg = random.randint (1,2)
wolfhp = 13

messagebox.showinfo(" The forest.",
                    " You're walking through a forest, you can hear the peaceful chripping " +\
                    " of birds, the faint running of a nearby stream, the bloodthirsty  " +\
                    " growl of a hungry Dire Wolf, the pleasent whistling of a slight wind" +\
                    " in the air WAIT WHAT! You spin around and find yourself face to face" +\
                    " with a grey, red eyed wolf, ready to attack.")

if player == 1:
    messagebox.showinfo("Current stats",
                        "  Your health is"+ str  (health)+\
                        "  Your damage is"+ str  (damage) +\
                        "  Your luck is"+ str  (luck))
elif player == 2:
    messagebox.showinfo("Current stats",
                        "  Your health is"+ str  (health)+\
                        "  Your damage is"+ str  (damage) +\
                        "  Your luck is"+ str  (luck))

elif player == 3:
    messagebox.showinfo("Current stats",
                        "  Your health is"+ str  (health)+\
                        "  Your damage is"+ str  (damage) +\
                        "  Your luck is"+ str  (luck))

elif player == 4:
    messagebox.showinfo("Current stats",
                        "  Your health is"+ str  (health)+\
                        "  Your damage is"+ str  (damage) +\
                        "  Your luck is"+ str  (luck))



while health >= 0 or wolfhp >= 0:
    input("Press enter to attack")
    wolfhp -= damage 
    health -= wolfdmg
    print ("You took {} damage.".format(wolfdmg) +\
           "Your health is now: {}".format(health)+\
           "The wolf has {} health" .format(wolfhp))
    if health <= 0 or wolfhp <= 0:
        break
    

#Luck
if wolfhp <= 0:
            messagebox.showinfo("You Won!",
                        " You flail about, kicking and hitting the wolf," +\
                        " eventually scaring it off. You now realize you may" +\
                        " want to find a weapon. Lets see how lucky you are.")
elif health <= 0:
           messagebox.showinfo("You lost!",
             " Wandering around the woods, unarmed and helpless," +\
             " you fell victim to one of the many dangers that lies " +\
             " within it.")
           root.destroy

messagebox.showinfo (" Are you lucky enough?",
                        "Your luck is" + str(luck))
if luck >= 10:
   messagebox.showinfo (" You got lucky!",
                         " As you continue forward, something in the" +\
                         " forset catches your eye. You find an iron sword" +\
                         " in relativly good condition. You damage will now" +\
                         " be increased by 5.")
   damage+= 5

elif luck < 10:
    messagebox.showinfo (" You weren't very lucky.",
                         " While keeping your eye out for a"+\
                         " weapon, the best thing you could find"+\
                         " was a very pointy stick. You damage will" +\
                         " now be increased by 2.")
    damage += 2


#Fork in the road
messagebox.showinfo (" The Forest...",
                     " After that close enounter, you realize fighting may"+\
                     " not always be the best option. Running away, as cowardly" +\
                     " as it is, would be smart sometimes. Your new experience with" +\
                     " fighting also gives your hero a special attack which may be used" +\
                     " once each battle.")
messagebox.showinfo (" The paths...",
                     " You continue walking through the forest, and you come to a" +\
                     " fork in the path. One way goes to the right, the other continues" +\
                     " stright ahead. Which direction would you like to go?" +\
                     " Press 1 for stright, 2 for right.")

direction  = simpledialog.askinteger (" Stright or right?",
                                     " Press 1 for stright, 2 for right, or if you don't feel like" +\
                                     " even following the path, press 3.")
#Directoins
if direction == 1:
    messagebox.showinfo (" Stright",
                         " After a bit of walking, you see a cabin on the road ahead of you. It's a"+\
                         " small, one room, cozy looking house. You realize you are very tired, and" +\
                         " very hungry. It seems as if you didn't prepare at all for this adventure."+\
                         " You decide to check out the cabbin.")
elif direction ==2:
    messagebox.showinfo ("Right",
                         " You decide to turn right down the path. After a while of walking, the ground"+\
                         " begins to shake. You need to take cover, quick!")
elif direction ==3:
    messagebox.showinfo (" Off the path. You rebel.",
                         " You decide to go on even more of an adventure than you're already on, and leave"+\
                         " the path. You aimlessly wander around for a bit, until you reach a cave. The sun"+\
                         " has been beating down on you all day, and the shade in the cave looks very inviting"+\
                         " You decide to go explore the cave.")


    simpledialog.askinteger ("Where would you like to take cover?",
                             " To climb a near by tree, press 1. To take cover in a bush, press 2."+\
                             " To be brave and stand your ground, press 3.")

#Direction 1
doordmg = random.randint (1,15)
doorhp = 30

door = simpledialog.askinteger (" The Cabin in the Forset",
                                " Do you want to knock or break the door down?"+\
                                " Press 1 for knock, 2 for break the door down.")
if door == 1:
            messagebox.showinfo (" The Cabin in the Forset",
                                 " You hear an old, raspy, female voice call out from inside"+\
                                 " Helloooo?... Come in. I've been waiting for you...")
elif door == 2:
    messagebox.showinfo (" The Cabin in the Forest",
                         " Wow. Thats a bit violent don't you think? Lets see if you can actually"+\
                         " do enough damage to the door to break it down.")
#The door
    while health >= 0 or doorhp >= 0:
        input("Press enter to attack")
        doorhp -= damage 
        health -= doordmg
        print ("You took {} damage.".format(doordmg) +\
           "Your health is now: {}".format(health)+\
           "The door has {} health" .format(doorhp))
        if health <= 0 or doorhp <= 0:
            break

if doorhp <= 0:
            messagebox.showinfo("You Won!",
                " You broke the door down! Congrats! What an amazing feat!" +\
                " You're so pro! What an inspiring acomplishment. You couldn't just knock," +\
                " no, thats too main stream for you. You just broke down the door of some"+\
                " poor old lady's house you twat. Thats so rude now she has to fix the door.")
            
elif health <= 0:
           messagebox.showinfo("Wow you really decided to break down a poor old lady's door?",
             " I'm glad the door killed you. That is so rude why would you do that to the nice" +\
             " lady who just welcomed you into her home? When you went to kick the door down, you, " +\
             " like the complete idiot you are, missed, and kicked you sword, implanting it into your."+\
             " rude inconsiderate skull.")
           





    

                          
