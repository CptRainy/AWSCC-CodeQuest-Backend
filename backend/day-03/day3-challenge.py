def game(count):
    choice = input("1. You are walking to your boyfriend/girlfriend's house. " +
                   "There are two roads to get there. One is a straight path " +
                   "which takes you there quickly, but is very plain and boring. " + 
                   "The other is curvy and full of wonderful sights on the way, " +
                   "but takes quite a while to reach your loved one's house.\nA. Short\nB. Long\nYour Choice: ")
    choice.upper()
    if (choice == "A"):
        wrong_choice()
        print("You fall in love quickly and easily.\n")
        count -= 1
    elif (choice == "B"):
        right_choice()
        print("You take your time and do not fall in love easily.\n")
        count += 1
    else:
        game(count)
    input("\nPress Any Key To Continue\n")
    count = question2(count)
    count = question3(count)
    count = question4(count)
    count = question5(count)
    count = question6(count)
    return count

def question2(count):
    choice = input("2. On the way, you see two rose bushes. One is full of white roses. " +
          "One is full of red roses. You decide to pick 20 roses for your " +
          "boyfriend/girlfriend.\nA. Equal Amounts\nB. Majority Red Roses\nC. Majority White Roses\nYour Choice: ")
    choice.upper()
    if (choice == "B"):
        wrong_choice()
        print("You expect to give a lot in the relationship, but expects to receive only a bit back.\n")
        count -= 1
    elif (choice == "C"):
        wrong_choice()
        print("You expect to receive a lot in the relationship, but expects to give only a bit back.\n")
        count -= 1
    elif (choice == "A"):
        right_choice()
        print("You equally want to receive and give back in the relationship.\n")
        count += 1
    else:  
        question2(count)
    input("\nPress Any Key To Continue\n")
    return count

def question3(count):
    choice = input("3. You finally get to your boyfriend/girlfriend's house. " +
          "You ring the bell and the maid answers. You can ask the maid to " +
          "please get your loved one, or you may go get them yourself.\nA. Ask the Maid\nB. Do It Yourself\nYour Choice: ")
    choice.upper()
    if (choice == "A"):
        wrong_choice()
        print("You beat around the bush and ask third party to intervene when you have problems.\n")
        count -= 1
    elif (choice == "B"):
        right_choice()
        print("You are direct, you confront problems and deal with it.\nYour Choice: ")
        count += 1
    else:  
        question3(count)
    input("\nPress Any Key To Continue\n")
    return count

def question4(count):
    choice = input("4. Now, you go up to your girlfriend/boyfriend's room. " + 
                   "No one is there. You can leave the roses by the windowsill " + 
                   "or on the bed\nA. On the Bed\nB. By the windowsill\nYour Choice: ")
    choice.upper()
    if (choice == "A"):
        right_choice()
        print("You need lots of reassurance in the relationship and you'd want to see your loved one every day, if possible.\n")
        count += 1
    elif (choice == "B"):
        wrong_choice()
        print("You don't expect or need to see your loved one too often.\n")
        count -= 1
    else:  
        question4(count)
    input("\nPress Any Key To Continue\n")
    return count

def question5(count):
    choice = input("5. Later, its time for bed. You and your loved one go to sleep, " + 
                   "in separate rooms. You wake up in the morning, and go to your " +
                   "boyfriend/girlfriend's room to check up on him/her. You enter the room: " + 
                   "Is he/she awake or sleeping?\nA. Finding them asleep.\nB. Finding them awake.\nYour Choice: ")
    choice.upper()
    if (choice == "A"):
        right_choice()
        print("You accept your loved one the way they are.\n")
        count += 1
    elif (choice == "B"):
        wrong_choice()
        print("You expect him/her to change for you.")
        count -= 1
    else:  
        question5(count)
    input("\nPress Any Key To Continue\n")
    return count

def question6(count):
    choice = input("6. It's time to go home now, and you start to head back. You can " + 
                   "take either road home now: The plain, boring one that gets you home " +
                   "fast; or the curvy, sight-filled road that you can just casually " +
                   " take your time with. Which road do you choose? Short or long?" + 
                   "\nA. Short.\nB. Long.\nYour Choice: ")
    choice.upper()
    if (choice == "A"):
        wrong_choice()
        print("You fall out of love easily.\n")
        count -= 1
    elif (choice == "B"):
        right_choice()
        print("You tend to stay in love for a long time.")
        count += 1
    else:  
        question6(count)
    input("\nPress Any Key To Continue\n")
    return count

def right_choice():
    print("You made your boyfriend/girlfriend happy.")

def wrong_choice():
    print("Your boyfriend/girlfriend pouts and is angry at you.")

count = 0
ave = 0
count = game(count)
ave = (count/6) * 100
print(f"\n\nYour Result is {count} / 6!\n")

if (ave >= 85):
    print("You passed!")
elif(ave < 85 and ave > 65 ):
    print("You kinda passed...")
else:
    print("You better reflect. You did not pass the test.")