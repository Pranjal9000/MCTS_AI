import numpy as np

class Node:

    def __init__(self, state, winning, move, parent):
        self.parent = parent
        self.move = move
        self.win = 0
        self.games = 0
        self.children = None
        self.state = state
        self.winner = winning

    def set_children(self, children):
        self.children = children

    def get_uct(self):
        # GET THE VALUE OF THE UCT FORMULA
        if self.games == 0:
            return None
        return (self.win/self.games) + np.sqrt(2*np.log(self.parent.games)/self.games)


    def next(self):
        #get the next move before next move
        if self.children is None:
            return None, None

        winners = [child for child in self.children if child.winner]
        if len(winners) > 0:
            return winners[0], winners[0].move

        t_games = [child.win/child.games if child.games > 0 else 0 for child in self.children]
        best_move = self.children[np.argmax(t_games)]
        return best_move, best_move.move


    def next_children(self, move):
        if self.children is None:
            return None
        for child in self.children:
            if child.move == move:
                return child

        raise Exception('Not existing child')