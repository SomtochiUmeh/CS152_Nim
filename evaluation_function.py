import random


def is_losing_state(state):
    """
    Checks if the given state is a losing state for the next player.
    These states are not captured by the 0 nim-sum strategy as the nim-sum is 1.
    A state is considered a losing state if it is one of the following:
    [1, 0, 0], [0, 1, 0], [0, 0, 1]
    """
    losing_states = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    return tuple(state) in losing_states


class Nim:
    """A class representing the Nim game."""

    def __init__(self, piles):
        """
        Initializes a Nim game instance with the specified piles configuration.

        Args:
            piles (list): A list containing the number of stones in each pile.
        """
        self.piles = piles

    def ai_move(self):
        """
        Make the AI's move using the nim-sum strategy and prioritizing moves that leave the opponent in a losing state.

        The AI first checks if there is a move that leaves the opponent in a losing state ([1, 0, 0], [0, 1, 0], or [0, 0, 1]).
        If such a move exists, it makes that move.
        If no such move exists, it follows the nim-sum strategy to make a move that reduces the nim-sum to zero.
        If the nim-sum is already zero, the AI makes a random move.
        """
        # Check for moves that leave the opponent in a losing state
        for i, pile_size in enumerate(self.piles):
            for stones in range(1, pile_size + 1):
                new_state = self.piles.copy()
                new_state[i] -= stones
                if is_losing_state(new_state):
                    self.piles[i] -= stones
                    return i, stones

        # If no losing move is available, follow the nim-sum strategy
        nim_sum = 0
        for pile in self.piles:
            nim_sum ^= pile

        if nim_sum == 0:
            # If the nim-sum is zero, make a random move
            non_empty_piles = [i for i, pile in enumerate(self.piles) if pile > 0]
            pile = random.choice(non_empty_piles)
            stones = random.randint(1, self.piles[pile])
        else:
            for i, pile_size in enumerate(self.piles):
                target_size = pile_size ^ nim_sum
                if target_size < pile_size:
                    pile = i
                    stones = pile_size - target_size
                    break

        self.piles[pile] -= stones

        return pile, stones
