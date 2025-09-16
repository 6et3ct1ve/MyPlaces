import random


def random_place(places):
    """
    Randomizer for choise where to go today
    """
    if not places:
        return None

    weights = []
    for place in places:
        weights.append(place["rating"])

    return random.choices(places, weights=weights, k=1)[0]
