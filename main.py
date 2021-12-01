from connect4.mcts_ai import train_mcts_once, train_mcts_during
from connect4.connect4 import *
from collections import defaultdict
import numpy as np


def utils_print(grid):
    print_grid = grid.astype(str)
    print_grid[print_grid == '-1'] = 'X'
    print_grid[print_grid == '1'] = 'O'
    print_grid[print_grid == '0'] = ' '
    res = str(print_grid).replace("'", "")
    res = res.replace('[[', '[')
    res = res.replace(']]', ']')
    print(' ' + res)
    print('  ' + ' '.join('0123456'))

if __name__ == '__main__':

    mcts_AI1 = None
    mcts_AI2 = None

    for i in range(200):
        mcts_AI1 = train_mcts_once(mcts_AI1)
    for i in range(40):
        mcts_AI2 = train_mcts_once(mcts_AI2)
    
    total_rounds = 4

    print('training finished for both AI\'s')
    for _ in range(total_rounds//2):
        # test AI with real play
        grid = create_grid()
        round = 0
        training_time_AI1 = 2000
        training_time_AI2 = 2000
        node_AI1 = mcts_AI1
        node_AI2 = mcts_AI2
        utils_print(grid)
        while True:
            if (round % 2) == 0:
                new_node, move = node_AI1.next()
                node_AI1 = train_mcts_during(node_AI1, training_time_AI1)
                node_AI1, move = node_AI1.next()
            else:
                new_node, move = node_AI2.next()
                node_AI2 = train_mcts_during(node_AI2, training_time_AI2)
                # print([(n.win, n.games) for n in node.children])
                node_AI2, move = node_AI2.next()

            grid, winner, exception = play(grid, move)

            utils_print(grid)


            # assert np.sum(node_AI1.state - grid) == 0, node_AI1.state
            # assert np.sum(node_AI2.state - grid) == 0, node_AI2.state
            if winner != 0:
                print('Winner : ', 'X' if winner == -1 else 'O')
                break
            elif exception is True:
                print('Bot moving out of bounds.')
                break
            round += 1

    for _ in range(total_rounds//2):
        # test AI with real play
        grid = create_grid()
        round = 0
        training_time_AI1 = 2000
        training_time_AI2 = 2000
        node_AI1 = mcts_AI1
        node_AI2 = mcts_AI2
        utils_print(grid)
        while True:
            if (round % 2) == 0:
                new_node, move = node_AI2.next()
                node_AI2 = train_mcts_during(node_AI2, training_time_AI2)
                # print([(n.win, n.games) for n in node.children])
                node_AI2, move = node_AI2.next()
            else:
                new_node, move = node_AI1.next()
                node_AI1 = train_mcts_during(node_AI1, training_time_AI1)
                node_AI1, move = node_AI1.next()

            grid, winner, exception = play(grid, move)

            utils_print(grid)


            # assert np.sum(node_AI1.state - grid) == 0, node_AI1.state
            # assert np.sum(node_AI2.state - grid) == 0, node_AI2.state
            if winner != 0:
                print('Winner : ', 'X' if winner == -1 else 'O')
                break
            elif exception is True:
                print('Bot moving out of bounds.')
                break
            round += 1


    # from pdb import set_trace; set_trace()

