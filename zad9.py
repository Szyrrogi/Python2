from itertools import permutations

def unique_permutations(elements: list):
    unique_perms = set(permutations(elements))
    return [list(perm) for perm in unique_perms]