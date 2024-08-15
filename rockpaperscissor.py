import random

# def Play():
#     user = input("What is your Choice?  'R' for Rock , 'P' for Paper , 'S' for Scissors!")
#     computer = random.choice(['R','P','S'])
#     print("Computer's choice :   " +computer)
#     if user == computer:
#         print("Its a tie!")
#         # return 'Its a tie'
#
#     if winner(user, computer):
#         print("You win")
#         # return 'You win!'
#
#     #return 'You lost!'
#     # print("You Lost")
# def winner(user,computer):
#     # r > s, s > p, p > r
#     if (user == 'R' and computer == 'S') \
#        or (user == 'S' and computer == 'P') \
#        or (user == 'P' and computer == 'R'):
#        return True
#
# print(Play())
# Play()

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
print(play())
