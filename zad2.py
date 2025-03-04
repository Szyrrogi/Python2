def round_numbers(numbers: list[int], threshold: int) -> list[int]:
    rounded = []
    for num in numbers:
        if num < threshold:
            rounded.append((num // 10) * 10)         
        else:
            rounded.append(((num + 9) // 10) * 10)
    return rounded
