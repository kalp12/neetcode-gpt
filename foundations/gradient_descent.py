class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        mn = init

        for _ in range(iterations):
            derivative = 2 * mn
            mn = mn - learning_rate * derivative
        return round(mn, 5)