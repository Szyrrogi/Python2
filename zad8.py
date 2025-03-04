import re

def count_syllables(word: str) -> int:
    return len(re.findall(r'[aeiouyAEIOUY]', word))

def readability_score(text: str) -> float:
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    words = text.split()
    
    avg_words_per_sentence = len(words) / len(sentences)
    avg_syllables_per_word = sum(count_syllables(word) for word in words) / len(words)
    
    return avg_words_per_sentence + avg_syllables_per_word