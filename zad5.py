def transposition_cipher(text: str, key: int) -> str:
    if key > len(text):
        return text

    text_list = list(text)

    for i in range(0, len(text_list) - key + 1, key):
        # Zamiana i-tej litery z (i + key - 1)-tą literą
        text_list[i], text_list[i + key - 1] = text_list[i + key - 1], text_list[i]

    return ''.join(text_list)