class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Possible moves for the knight
        moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        
        # Create a 3D array to store probabilities of the knight being at each position after each move
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        
        # Initialize the probability of starting at (row, column) after 0 moves to 1 (certainty)
        dp[0][row][column] = 1
        
        # Calculate the probabilities for each move
        for m in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            dp[m][r][c] += dp[m - 1][nr][nc] / 8.0
        
        # Sum up all the probabilities after k moves to get the final result
        probability = sum(dp[k][r][c] for r in range(n) for c in range(n))
        
        return probability
