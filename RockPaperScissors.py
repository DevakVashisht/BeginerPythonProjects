import random
def play():
    user = input("Rock='r'\nPaper='p'\nScissors='s'\n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "It is a Tie"
    if is_win(user,computer):
        return 'You Won'
    else:
        return 'You Lost'


def is_win(player, opponent):
    # r > s, s > p, p > r
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 'r':
        return True
    
        

print(play())