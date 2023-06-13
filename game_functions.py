import random
def player_input():
    move = 'empty'
    while move == 'empty':
        move_check = input('Enter you move: ').upper()
        if move_check in ['R', 'P', 'S']:
            move = move_check
        else:
            print('Invalid move. \n Valid moves are R for rock, P for paper or S for scissors')
    return move

def game_outcome(human_play, robot_play):
    if human_play == robot_play:
        outc = 'tie'
    elif(human_play == 'R' and robot_play == 'S') or (human_play == 'P' and robot_play == 'R') or (human_play == 'S' and robot_play == 'S'):
        outc = 'homo win'
    else:
        outc = 'robo win'
    return outc

def magnify(human_plays):
    homo_playsmag = human_plays
    while len(homo_playsmag) < 100:
        try:
            starting_index = random.randint(0, len(homo_playsmag) - 1)
            ending_index = random.randint(starting_index + 1, len(homo_playsmag) - 1)
            subseq = homo_playsmag[starting_index:ending_index]
            homo_playsmag = homo_playsmag + subseq
        except Exception:
            continue
    return homo_playsmag

def transit(a, b, list_plays): #a=predhodna, b ji sledi
    return(len([list_plays[i] for i in range(1, len(list_plays)) if list_plays[i-1] == a and
                list_plays[i] == b])/list_plays.count(a))
