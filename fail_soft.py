class Nim:
    """
    Initialize the Nim game with the given piles.

    Args:
        piles (list): A list of integers representing the number of stones in each pile.
    """

    def __init__(self, piles):
        self.piles = piles

    def evaluate(self, piles, is_maximizing):
        """
        Evaluate the game state and return the score.

        Args:
            piles (tuple): A tuple representing the current state of the piles.
            is_maximizing (bool): True if it's the maximizing player's turn, False otherwise.

        Returns:
            int: -1 if the game is over and the maximizing player loses, 1 if the game is over and the maximizing player wins.
        """
        if all(pile == 0 for pile in piles):
            return 1 if is_maximizing else -1

    def possible_new_states(self, piles):
        """
        Generator function for all possible new states by removing stones from each pile.

        Args:
            piles (list): A list of integers representing the current state of the piles.

        Yields:
            list: A new state of the piles after removing stones.
        """
        for i, pile in enumerate(piles):
            for stones in range(1, pile + 1):
                new_piles = piles[:i] + [pile - stones] + piles[i + 1 :]
                yield new_piles

    # fail-soft alpha beta pruning
    def alpha_beta(self, piles, is_maximizing, alpha, beta):
        """
        Perform fail-soft alpha-beta pruning to determine the best move.

        Args:
            piles (list): A list of integers representing the current state of the piles.
            is_maximizing (bool): True if it's the maximizing player's turn, False otherwise.
            alpha (float): The alpha value for alpha-beta pruning.
            beta (float): The beta value for alpha-beta pruning.

        Returns:
            float: The best score obtained from the current state.
        """
        score = self.evaluate(tuple(piles), is_maximizing)
        if score:
            return score

        best_score = -float("inf") if is_maximizing else float("inf")
        for new_piles in self.possible_new_states(piles):
            score = self.alpha_beta(new_piles, not is_maximizing, alpha, beta)
            if is_maximizing:
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if best_score >= beta:
                    break
            else:
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if best_score <= alpha:
                    break

            # if beta <= alpha:
            #     break

        return best_score

    def ai_move(self):
        """
        Determine the best move for the AI player using fail-soft alpha-beta pruning.

        Returns:
            tuple: A tuple containing the pile index and the number of stones to remove.
        """
        best_score = -float("inf")
        best_move = None
        for i, pile in enumerate(self.piles):
            for stones in range(1, pile + 1):
                new_piles = self.piles[:i] + [pile - stones] + self.piles[i + 1 :]
                score = self.alpha_beta(new_piles, False, -float("inf"), float("inf"))
                if score > best_score:
                    best_score = score
                    best_move = (i, stones)

        pile, stones = best_move
        self.piles = (
            self.piles[:pile] + [self.piles[pile] - stones] + self.piles[pile + 1 :]
        )
        return pile, stones
