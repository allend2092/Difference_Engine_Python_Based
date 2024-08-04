import numpy as np
import math

def difference_engine(initial_values, order, num_terms):
    """
    Simulates a Difference Engine to predict the positions of a celestial body.

    Args:
        initial_values: A list of initial positions for the celestial body.
        order: The order of the difference engine.
        num_terms: The number of terms (days) to calculate.

    Returns:
        A numpy array containing the predicted positions.
    """

    # Create the difference table with sufficient space
    diff_table = np.zeros((order + 1, num_terms))
    diff_table[0, :len(initial_values)] = initial_values

    # Calculate the difference table
    for i in range(1, order + 1):
        for j in range(num_terms - i):
            diff_table[i, j] = diff_table[i - 1, j + 1] - diff_table[i - 1, j]

    # Generate the terms using the first column of the difference table
    values = np.zeros(num_terms)
    for i in range(num_terms):
        term = diff_table[0, 0]
        for j in range(1, order + 1):
            if i >= j:
                term += diff_table[j, 0] * math.factorial(i) / (math.factorial(j) * math.factorial(i - j))
        values[i] = term

    return values

# Initial positions of the celestial body (e.g., Mars) for the first few days
initial_positions = [100, 150, 210, 280]
order = 2
num_terms = 10  # Predicting the position for the next 10 days

# Using the difference engine to predict the positions
predicted_positions = difference_engine(initial_positions, order, num_terms)
print(predicted_positions)
