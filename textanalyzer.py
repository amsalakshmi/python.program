print("📝 Text Analyzer Tool")

text = input("Enter your paragraph:\n")

# Character count (including spaces)
char_count = len(text)

# Word count
words = text.split()
word_count = len(words)

# Sentence count
sentence_count = text.count('.') + text.count('!') + text.count('?')

# Word frequency
frequency = {}

for word in words:
    word = word.lower().strip(".,!?")
    frequency[word] = frequency.get(word, 0) + 1

# Most frequent word
most_common = max(frequency, key=frequency.get)

print("\n📊 Analysis Result")
print("Total Characters:", char_count)
print("Total Words:", word_count)
print("Total Sentences:", sentence_count)
print("Most Frequent Word:", most_common)
print("Frequency:", frequency[most_common])
