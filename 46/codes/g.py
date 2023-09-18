import random

# Define the urns and their respective probabilities of being chosen
urns = [
    {"white": 2, "black": 3},
    {"white": 3, "black": 2},
    {"white": 4, "black": 1}
]

total_trials = 1000000  # Number of trials to run the simulation
chosen_urn_count = [0, 0, 0]  # Initialize counts for each urn being chosen
white_ball_count = 0  # Initialize the count of white balls drawn

i = 0

while i < total_trials:
    chosen_urn_index = random.randint(0, 2)  # Randomly choose an urn (0, 1, or 2)

    # Simulate drawing a ball from the chosen urn
    urn = urns[chosen_urn_index]
    total_balls = urn["white"] + urn["black"]
    drawn_ball = random.randint(1, total_balls)

    # If the drawn ball is white, increment the count
    if drawn_ball <= urn["white"]:
        white_ball_count += 1

    chosen_urn_count[chosen_urn_index] += 1
    i += 1

# Calculate the probability that the ball drawn was from the second urn
probability_second_urn = chosen_urn_count[1] / total_trials

print(f"Probability that the ball drawn was from the second urn: {probability_second_urn:.4f}")

