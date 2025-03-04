def group_words_by_length(words: list[str]) -> dict:
    grouped = {}
    for word in words:
        length = len(word)
        if length not in grouped:
            grouped[length] = []
        grouped[length].append(word)
    return grouped