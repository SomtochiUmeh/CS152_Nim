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

    # fail-hard alpha beta pruning
    def alpha_beta(self, piles, is_maximizing, alpha, beta):
        score = self.evaluate(tuple(piles), is_maximizing)
        if score:
            return score

        best_score = -float("inf") if is_maximizing else float("inf")
        for new_piles in self.possible_new_states(piles):
            score = self.alpha_beta(new_piles, not is_maximizing, alpha, beta)
            if is_maximizing:
                best_score = max(best_score, score)
                # alpha = max(alpha, best_score)
                if best_score > beta:
                    break
                alpha = max(alpha, best_score)
            else:
                best_score = min(best_score, score)
                # beta = min(beta, best_score)
                if best_score < alpha:
                    break
                beta = min(beta, best_score)

            # if beta <= alpha:
            #     break

        return best_score

    def ai_move(self):
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
