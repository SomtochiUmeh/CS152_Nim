import random


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
        Make the AI's move using the nim-sum strategy.

        The nim-sum strategy is based on the concept of the nim-sum, which is the bitwise XOR of the sizes of all piles.
        The AI calculates the nim-sum and tries to make a move that reduces the nim-sum to zero.
        If the nim-sum is already zero, the AI makes a random move.

        The nim-sum strategy guarantees a win for the player who reaches a nim-sum of zero on their turn.
        """
        nim_sum = 0
        for pile in self.piles:
            nim_sum ^= pile

        if nim_sum == 0:
            # If the nim-sum is zero, make a random move
            non_empty_piles = [i for i, pile in enumerate(self.piles) if pile > 0]
            pile = random.choice(non_empty_piles)
            stones = random.randint(1, self.piles[pile] - 1)
        else:
            # Find a pile that can be reduced to make the nim-sum zero
            for i, pile_size in enumerate(self.piles):
                target_size = pile_size ^ nim_sum
                if target_size < pile_size:
                    pile = i
                    stones = pile_size - target_size
                    break

        self.piles[pile] -= stones

        return pile, stones
