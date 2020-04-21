# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:17:24 2020

@author: Grant
"""

# Sandwich Ordering System

def main() :
    
    print("   *******************************************")
    print("  |                                           |")
    print("  |      Welcome to Grant's Sandwich Shop     |")
    print("  |                                           |")
    print("   *******************************************\n")
    
    #greeting message
    menu_or_order = input(" Would you like to see our menu, or order a sandwich? \n :")
    
    #menu or order words to check
    menu_words = ["menu", "Menu, choices, Choices"]
    order_words = ["order", "Order"]
    
    #words to ignore when being entered in string
    ignore = ["please", "Please", "may", "May", "I", "i", "have", "Have", "can", "Can", "thank", "Thank", "you", "You", "the", "The", "I'd", "like", "Like",  
    "thanks", "Thanks","see", "See", "to", "To", "would", "Would", "show", "Show", "me", "Me"]
    
    #split the input string based on words not in the above list
    temp = [x for x in menu_or_order.split() if x not in ignore]
  
    #input to string
    menu_or_order = temp[0]
    
    
    #menu or order
    if(menu_or_order in menu_words):
        menu()
    elif (menu_or_order in order_words):
        order()
    
    while( menu_or_order not in menu_words and menu_or_order not in order_words):
        print("Please choose \"menu\" or \" order\" ")
        menu_or_order = input(" :")
        
        temp = [x for x in menu_or_order.split() if x not in ignore]
            
        #input to string
        menu_or_order = temp[0]
        if(menu_or_order in menu_words):
            menu()
        elif(menu_or_order in order_words):
            order()           



def grant():
    #default and option for Grant's Special
    name = "Grant's Special Sandwich"
    bread = "wheat"
    meats = ["chicken", "bacon"]
    veggies = ["lettuce", "jalapeno"]
    cheese = ["cheddar"]
    spread = ["ranch"]
    other = ["toasted"]    
    print("Name of Sandwich: Grant's Special")
    print("Usual ingredients: wheat bread, chicken, bacon, cheddar, lettuce, jalapeno, ranch, toasted ")
    print("Other bread types: rye, italian")
    print("Other meats: ham, peperoni")
    print("Other veggies: olives, tomato, cucumber, onion")
    print("other cheese: american, swiss")
    print("other spreads: mayo, mustard")
    print("other options: not toasted, salt, pepper")
    
    original(name, bread, meats, veggies, cheese, spread, other)     
    
    
def veggie():
    #default and option for Veggie
    name = "Veggie Sandwich"
    bread = "rye"
    meats = []
    veggies = ["olives", "tomato", "cucumber", "onion"]
    cheese = ["no cheese"]
    spread = ["ranch"]
    other = ["not toasted"]    
    print("Name of Sandwich: Veggie")
    print("Usual ingredients: rye bread, olives, tomato, cucumber, onion, no cheese, ranch, not toasted ")
    print("Other bread types: wheat, italian")
    print("Other veggies: lettuce, jalapeno")
    print("other cheese: american, swiss, cheddar")
    print("other spreads: mayo, mustard")
    print("other options: toasted, salt, pepper")
    
    original(name, bread, meats, veggies, cheese, spread, other)    
    
def blt():
    #default and option for BLT
    name = "BLT Sandwich"
    bread = "wheat"
    meats = ["bacon"]
    veggies = ["tomato","lettuce"]
    cheese = ["no cheese"]
    spread = ["mayo"]
    other = ["not toasted"]    
    print("Name of Sandwich: Bacon Lettuce Tomatoe (BLT)")
    print("Usual ingredients: wheat bread, tomato, lettuce, bacon, no cheese, mayo) not toasted")
    print("Other bread types: rye, italian")
    print("Other meats: chicken, ham, peperoni")
    print("Other veggies: olives, tomato, cucumber, onion, jalapeno")
    print("other cheese: american, swiss, cheddar")
    print("other spreads: ranch, mustard")
    print("other options: toasted, salt, pepper")
    
    original(name, bread, meats, veggies, cheese, spread, other) 
    
    
def basic():
    #default and option for Basic
    name = "Basic Sandwich"
    bread = "italian"
    meats = ["ham", "bacon"]
    veggies = ["lettuce"]
    cheese = ["swiss"]
    spread = ["mayo", "mustard"]
    other = ["toasted"]
    print("Name of Sandwich: Basic")
    print("Usual ingredients: italian bread, ham, bacon, lettuce, swiss, mayo, mustard, toasted")
    print("Other bread types: rye, wheat")
    print("Other meats: chicken, peperoni")
    print("Other veggies: olives, tomato, cucumber, onion, jalapeno")
    print("other cheese: american, cheddar")
    print("other spreads: ranch")
    print("other options: not toasted, salt, pepper")
     
    original(name, bread, meats, veggies, cheese, spread, other)    
    
def menu():
    
    print("\n We offer four different sandwiches: 1.Grant's Special, 2.Veggie, 3.BLT, and 4.Basic.\n")
    print(" if you want more information about a sandwich enter its name below or hit enter to order sandwich")
    info_or_order = input(" \n : ")
    
    if (info_or_order == "Grant's Special" or info_or_order == "grant's special"
        or info_or_order == "special" or info_or_order == "grants special" or info_or_order == "1"):
        grant()
    elif(info_or_order == "veggie" or info_or_order == "Veggie" or info_or_order == "2"):
        veggie()
    elif(info_or_order == "BLT" or info_or_order == "blt" or info_or_order == "3"):
        blt()
    elif(info_or_order == "basic" or info_or_order == "Basic"or info_or_order == "4"):
        basic()
    else:
        order()
    
    

def order():
    sandwich_choice = input("\n What type of sandwich would you like? example: Grant's Special) \n if you want to see the menu please type \" menu \" \n :")
    
    if sandwich_choice == "options" or sandwich_choice == "options" or sandwich_choice == "menu" or sandwich_choice == "Menu":
        menu()
    elif (sandwich_choice == "Grant's Special" or sandwich_choice == "grant's special" or sandwich_choice == "special" or sandwich_choice == "grants special" or sandwich_choice == "Grant's special" or sandwich_choice == "1"):
        grant()
    elif(sandwich_choice == "veggie" or sandwich_choice == "Veggie" or sandwich_choice == "2"):
        veggie()
    elif(sandwich_choice == "BLT" or sandwich_choice == "blt" or sandwich_choice == "3"):
        blt()
    elif(sandwich_choice == "basic" or sandwich_choice == "Basic" or sandwich_choice == "4"):
        basic()            
    
def alter(name, bread, meats, veggies, cheese, spread, other):
    seperator = ', '
    print( name + ", Bread: " + bread + ", Meats: " + seperator.join(meats) + ", Veggies: " + seperator.join(veggies) + ", Cheese: " + seperator.join(cheese) + ", Spread: " + seperator.join(spread) + ", Options: " + seperator.join(other))
    
    types_of_bread = ["wheat", "italian", "rye", "wheat bread", "italian bread", "rye bread"]
    
    types_of_meat = ["ham", "chicken", "bacon", "peperoni"]
    
    types_of_veggie = ["olives", "tomato", "cucumber", "onion", "jalepeno"]
    
    types_of_cheese = ["cheddar", "swiss", "american"]
    
    types_of_spread = ["ranch", "mayo", "mayonnaise","mustard"]  
    
    types_of_other = ["toasted", "not toasted", "salt and pepper"]
    
    ignore = ["please", "Please", "may", "May", "I", "i", "have", "Have", "can", "Can", "thank", "Thank", "you", "You", "the", "The", "I'd", "like", "Like",  
    "thanks", "Thanks","see", "See", "to", "To", "would", "Would", "show", "Show", "me", "Me", "and", "bread", "Bread"]    
    
    hold = ["hold", "no", "not", "except", "Hold", "No", "NO", "Not", "Except"]
    
    place_order = input("Please place order (if you want to hold multiple items please say hold \"ham\" hold \"lettuce\" if in different categories \n :")
    
    temp = [x for x in place_order.split() if x not in ignore]
    
    i = 0
    while (i < len(temp)):
        if (temp[i] in hold):
            j = i
            if (temp[j + 1] in meats):
                while (j + 1 < len(temp) and temp[j + 1] in meats):
                    meats.remove(temp[j + 1])
                    temp.remove(temp[j+1])
            elif (temp[j + 1] in veggies):
                while (j + 1 < len(temp) and temp[j + 1] in veggies):
                    veggies.remove(temp[j + 1])
                    temp.remove(temp[j+1])
            elif (temp[j + 1] in cheese):
                while (j + 1 < len(temp) and temp[j + 1] in cheese):
                    cheese.remove(temp[j + 1])
                    temp.remove(temp[j+1])   
            elif (temp[j + 1] in spread):
                while (j + 1 < len(temp) and temp[j + 1] in spread):
                    spread.remove(temp[j + 1])
                    temp.remove(temp[j+1])  
            elif (temp[j + 1] in other):
                while (j + 1 < len(temp) and temp[j + 1] in other):
                    other.remove(temp[j + 1])
                    temp.remove(temp[j+1])            
        elif(temp[i] in types_of_bread):
            bread = temp[i]
        elif(temp[i] in types_of_meat):
            meats.append(temp[i])
        elif(temp[i] in types_of_veggie):
            veggies.append(temp[i])
        elif(temp[i] in types_of_cheese):
            cheese.append(temp[i])
        elif(temp[i] in types_of_spread):
            spread.append(temp[i])
        elif(temp[i] in types_of_other):
            other.append(temp[i])        
        i += 1

    
    if (len(meats) == 0):
        meats.append("none")
    elif(len(veggies) == 0):
        veggies.append("none")
    elif(len(cheese) == 0):
        cheese.append("none")   
    elif(len(spread) == 0):
        spread.append("none")   
    elif(len(other) == 0):
        other.append("none")    
        
    print( name + ", Bread: " + bread + ", Meats: " + seperator.join(meats) + ", Veggies: " + seperator.join(veggies) + ", Cheese: " + seperator.join(cheese) + ", Spread: " + seperator.join(spread) + ", Options: " + seperator.join(other) + ". is your order correct, yes or no?")
    
    ok = input(" :")
    
    if (ok == "yes" or ok == "y" or ok == "Yes"):
        print("Enjoy your " + name)
        restart()
    else:
        print("please reorder sandwich")
        alter(name,bread,meats,veggies,cheese,spread,other)
    
    
    
def original(name, bread, meats, veggies, cheese, spread, other): 
    change = input("\n Would you like the usual ingredients?\n :")
    if (change == "no" or change == "No" or change == "n"):
        alter(name, bread, meats, veggies, cheese, spread, other)
    elif (change == "yes" or change == "Yes" or change == "y"):        
        print("Enjoy your " + name)
        restart()
   
def restart(): 
    restart = input("\n Would you like to order another sandwich? yes or no \n :")
    if (restart == "no" or restart == "No" or restart == "n"):
        raise SystemExit
    elif (restart == "yes" or restart == "Yes" or restart == "y"):        
        main()

main()