def count_words(text):
    return len(text.split())

def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

def count_consonants(text):
    return sum(1 for ch in text.lower() if ch.isalpha() and ch not in "aeiou")

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def remove_vowels(text):
    return ''.join(ch for ch in text if ch.lower() not in "aeiou")

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def longest_word(text):
    words = text.split()
    longest = max(words, key=len)
    return longest, len(longest)

def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))
    
    word, length = longest_word(text)
    print(f"Longest word: {word} ({length} letters)")
    
    print("Word Frequency:", word_frequency(text))

text_input = input("Enter text: ")
analyze_text(text_input)