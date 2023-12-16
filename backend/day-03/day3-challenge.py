def game(count):
    choice = input("1. You are walking to your boyfriend/girlfriend's house. " +
                   "There are two roads to get there. One is a straight path " +
                   "which takes you there quickly, but is very plain and boring. " + 
                   "The other is curvy and full of wonderful sights on the way, " +
                   "but takes quite a while to reach your loved one's house.\nA. Short\nB. Long\nYour Choice: ")
    choice.upper()
    if (choice == "A"):
        wrong_choice()
        print("You fall in love quickly and easily.")
        count -= 1
    elif (choice == "B"):
        right_choice()
        print("You take your time and do not fall in love easily.")
        count += 1
    else:
        game(count)

    count = question2(count)
    count = question3(count)
    return count

def question2(count):
    choice = input("2. On the way, you see two rose bushes. One is full of white roses. " +
          "One is full of red roses. You decide to pick 20 roses for your " +
          "boyfriend/girlfriend.\nA. Equal Amounts\nB. Majority Red Roses\nC. Majority White Roses\nYour Choice: ")
    choice.upper()
    if (choice == "B"):
        wrong_choice()
        print("You expect to give a lot in the relationship, but expects to receive only a bit back.")
        count -= 1
    elif (choice == "C"):
        wrong_choice()
        print("You expect to receive a lot in the relationship, but expects to give only a bit back.")
        count -= 1
    elif (choice == "A"):
        right_choice()
        print("You equally want to receive and give back in the relationship.")
        count += 1
    else:  
        question2(count)
    return count

def question3(count):
    choice = input("3. You finally get to your boyfriend/girlfriend's house. " +
          "You ring the bell and the maid answers. You can ask the maid to " +
          "please get your loved one, or you may go get them yourself.\nA. Ask the Maid\nB. Do It Yourself\nYour Choice: ")
    choice.upper()
    if (choice == "A"):
        wrong_choice()
        print("You beat around the bush and ask third party to intervene when you have problems.")
        count -= 1
    elif (choice == "B"):
        right_choice()
        print("You are direct, you confront problems and deal with it.")
        count += 1
    else:  
        question3(count)
    return count

def right_choice():
    print("You made your boyfriend/girlfriend happy.")

def wrong_choice():
    print("Your boyfriend/girlfriend pouts and is angry at you.")

count = 0
count = game(count)
print(count)