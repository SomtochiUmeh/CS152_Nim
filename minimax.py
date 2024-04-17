class Nim:
    def __init__(self, piles):
        self.piles = piles

    def evaluate(self, piles, is_maximizing):
        if all(pile == 0 for pile in piles):
            return 1 if is_maximizing else -1

    def possible_new_states(self, piles):
        for i, pile in enumerate(piles):
            for stones in range(1, pile + 1):
                new_piles = piles[:i] + [pile - stones] + piles[i + 1 :]
                yield new_piles

    def minimax(self, piles, is_maximizing):
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
