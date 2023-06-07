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


homo_plays = []
outcomes = []

number_of_games = int(input('How many games above 15 do you want to play?'))

for x in range(15):
    homo_play = player_input()
    homo_plays.append(homo_play)
    robo_play = random.choice(['R', 'P', 'S'])
    print(robo_play)
    outcome = game_outcome(homo_play, robo_play)
    outcomes.append(outcome)


def magnify(human_plays):
    homo_playsmag = human_plays
    while len(homo_playsmag) < 100:
        starting_index = random.randint(0, len(homo_playsmag) - 1)
        ending_index = random.randint(starting_index + 1, len(homo_playsmag) - 1)
        subseq = homo_playsmag[starting_index:ending_index]
        homo_playsmag = homo_playsmag + subseq
        return homo_playsmag


def transit(a, b, list_plays): #a=predhodna, b ji sledi
    return(len([list_plays[i] for i in range(1, len(list_plays)) if list_plays[i-1] == a and
                list_plays[i] == b])/list_plays.count(a))


while len(outcomes) < 15 + number_of_games:
    hp_mag = magnify(homo_plays)
    n = len(hp_mag)
    initial = [round(hp_mag.count('R') / n, 2),
               round(hp_mag.count('P') / n, 2),
               round(hp_mag.count('S') / n, 2)]
    trans_matrix = [[transit('R', 'R', hp_mag), transit('P', 'R', hp_mag), transit('S', 'R', hp_mag)],
                    [transit('R', 'P', hp_mag), transit('P', 'P', hp_mag), transit('S', 'P', hp_mag)],
                    [transit('R', 'S', hp_mag), transit('P', 'S', hp_mag), transit('S', 'S', hp_mag)]]
    for x in range(5):
        homo_last_play = homo_plays[-1]
        if homo_last_play == 'R':
            index = 0
        elif homo_last_play == 'P':
            index = 1
        else:
            index = 2
        prob = initial[0] + trans_matrix[0][0] + trans_matrix[0][1] + trans_matrix[0][2]
        robo_probs = {
            'R': initial[0] + trans_matrix[index][0],
            'P': initial[1] + trans_matrix[index][1],
            'S': initial[2] + trans_matrix[index][2]
        }
        robo_max_prob = max(robo_probs, key=robo_probs.get)
        robo_probToPlay = {
            'R': 'P',
            'P': 'S',
            'S': 'R'
        }
        robo_play = robo_probToPlay.get(robo_max_prob)
        homo_play = player_input()
        homo_plays.append(homo_play)
        outcome = game_outcome(homo_play, robo_play)
        outcomes.append(outcome)
        print(robo_play)

print('Human wins:', outcomes.count('homo win'),  'Robo wins: ', outcomes.count('robo win'), 'Tie: ', outcomes.count('tie'))


