class Nim:
    """A class representing the Nim game."""

    def __init__(self, piles):
        """
        Initializes a Nim game instance with the specified piles configuration.

        Args:
            piles (list): A list containing the number of stones in each pile.
        """
        self.piles = piles

    def evaluate(self, piles, is_maximizing):
        """
        Evaluates the current game state.

        Args:
            piles (list): A list representing the current state of the piles.
            is_maximizing (bool): A boolean indicating whether it's the maximizing player's turn.

        Returns:
            int: The evaluation score of the current game state.
        """
        if all(pile == 0 for pile in piles):
            return 1 if is_maximizing else -1

    def possible_new_states(self, piles):
        """
        Generator for possible new states from the current state.

        Args:
            piles (list): A list representing the current state of the piles.

        Yields:
            list: A new state resulting from a possible move.
        """
        for i, pile in enumerate(piles):
            for stones in range(1, pile + 1):
                new_piles = piles[:i] + [pile - stones] + piles[i + 1 :]
                yield new_piles

    def minimax(self, piles, is_maximizing):
        """
        Applies the minimax algorithm to find the best move.

        Args:
            piles (list): A list representing the current state of the piles.
            is_maximizing (bool): A boolean indicating whether it's the maximizing player's turn.

        Returns:
            int: The score associated with the best move.
        """
        score = self.evaluate(piles, is_maximizing)
        if score:
            return score

        if is_maximizing:
            best_score = -float("inf")
            for new_piles in self.possible_new_states(piles):
                score = self.minimax(new_piles, False)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for new_piles in self.possible_new_states(piles):
                score = self.minimax(new_piles, True)
                best_score = min(best_score, score)
            return best_score

    def ai_move(self):
        """
        Computes the best move for the AI player using the minimax algorithm.

        The AI player evaluates all possible moves and selects the one that maximizes its score
        while minimizing the opponent's score. It uses the minimax algorithm with alpha-beta pruning
        to efficiently explore the game tree.

        Returns:
            tuple: A tuple containing the index of the pile to remove stones from and the number
            of stones to remove for the best move.
        """
        best_score = -float("inf")
        best_move = None
        for i, pile in enumerate(self.piles):
            for stones in range(1, pile + 1):
                new_piles = self.piles[:i] + [pile - stones] + self.piles[i + 1 :]
                score = self.minimax(new_piles, False)
                if score > best_score:
                    best_score = score
                    best_move = (i, stones)

        pile, stones = best_move
        self.piles = (
            self.piles[:pile] + [self.piles[pile] - stones] + self.piles[pile + 1 :]
        )
        return pile, stones
