from collections import Counter

def most_frequent_element(data: list):
    counter = Counter(data)
    return counter.most_common(1)[0][0]