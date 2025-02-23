import re

def find_sequences(text):
    pattern = r'\b[a-z]+_[a-z]+\b'  # Matches 'word_word' pattern
    return re.findall(pattern, text)

# Example usage
test_strings = [
    "hello_world",    # ✅ Matches
    "hello_World",    # ❌ Doesn't match (uppercase 'W')
    "hello_world_123", # ❌ Doesn't match (numbers)
    "hello__world",   # ❌ Doesn't match (double underscore)
    "test_example",   # ✅ Matches
    "test_example_more", # ❌ Doesn't match (more than one underscore segment)
]

for s in test_strings:
    print(f"'{s}' -> {find_sequences(s)}")
