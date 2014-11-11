import random
import math

def calculate_pi(N):
    total_count = 0
    circle_count = 0

    for i in range(N):
        x = random.random()
        y = random.random()

        r = math.sqrt(x**2 + y**2)

        if r <= 1:
            circle_count += 1
        total_count += 1

    return circle_count / total_count * 4