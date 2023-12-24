def rps(p1, p2):
    rps_arr = [2,1,0] # Rock, Scissors, Paper

    # 2 > 1, 1 > 0, 0 < 2
    # 2 > 0, 1 < 2, 0 < 1
    # 2 = 2, 1 = 1, 0 = 0
    #p1 wins: Rock > Scissors, Scissors > Paper, Paper < Rock
    #p2 wins: Rock > Paper, Scissors < Rock, Paper > Scissors
    #no wins: Rock = Rock, Scissors = Scissors, Paper = Paper
    if(((p1 > p2) and (p1 != 2)) or (p1 == 0 and p2 == 2) or  ((p1 > p2) and (p2 != 0))):
        print("Player1 Wins")
    elif(((p1 < p2) and (p1 != 2)) or (p1 == 2 and p2 == 0)):
        print("Player2 Wins")
    else:
        print("It's a Tie!")

def assign_num(num):
    match(num):
        case "Rock":
            num = 2
        case "Scissors":
            num = 1
        case "Paper":
            num = 0
        case _:
            print("Wrong input")
            exit()
    return num

print("Rock, Paper, or Scissors")
p1 = int(assign_num(input("Player1: ")))
p2 = int(assign_num(input("Player2: ")))
rps(p1,p2)