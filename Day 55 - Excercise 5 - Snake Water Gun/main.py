import random

#    S  W  G
# S  0 -1  1
# W  1  0 -1
# G -1  1  0

game_matrix = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

while True:
    player = int(input("Enter 0 for Snake, 1 for Water or 2 for Gun: ").strip())
    computer = random.randint(0, 2)

    match game_matrix[computer][player]:
        case 0:
            print("There is a Draw!")
        case 1:
            print("You Win!")
        case -1:
            print("Computer Wins!")
