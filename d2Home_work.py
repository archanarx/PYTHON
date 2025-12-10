# Store a short paragraph using a multiline string
paragraph = """Python is a powerful language used by beginners and professionals. 
This Python course will help you learn important concepts easily.
"""

# Display the length of the paragraph (number of characters).
length = len(paragraph)
print("Length of paragraph: ", length)

# Display the first and last characters in the paragraph.
print("First character : ", paragraph[0])
print("Last character : ", paragraph[-1])

# Slice and print a short preview: the first 50 characters.
preview = paragraph[:50]
print("Preview:", preview)

# Replace all occurrences of the word "Python" with "PYTHON" (in all caps)
replacedText = paragraph.replace("Python", "PYTHON")
print("Replaced text:\n", replacedText)

# Convert the entire paragraph to lowercase.
lowercaseText = paragraph.lower()
print("Lowercase:\n", lowercaseText)

# Remove any extra whitespaces from the start or end.
cleanedText = paragraph.strip()
print("Trimmed paragraph:\n", cleanedText)

# Split the paragraph into individual words and print the list.
words = cleanedText.split()
print("Word list: ", words)

# Check if the word "course" exists in the paragraph.Print a message if found
if "course" in cleanedText.lower():
    print("The word 'course' was found in the paragraph.")

# Display the final message: "The course description is {} characters long and has {} words." using the format() method.
wordCount = len(words)
finalMessage = "The course description is {} characters long and has {} words." .format(length, wordCount)
print(finalMessage)




# # import re
# import string

# # 1. Count sentences
# sentences = re.split(r'[.!?]+', paragraph.strip())
# sentences = [s for s in sentences if s.strip()]
# print("Number of sentences:", len(sentences))

# # 2. Remove punctuation
# clean_no_punc = paragraph.translate(str.maketrans("", "", string.punctuation))
# print("Paragraph without punctuation:\n", clean_no_punc)

# # 3. Word frequency dictionary
# word_freq = {}
# for word in words:
#     w = word.lower().strip(string.punctuation)
#     word_freq[w] = word_freq.get(w, 0) + 1

# print("Word Frequency Dictionary:")
# print(word_freq)

# # 4. Print paragraph in a box
# text = cleanedText
# line = "-" * (len(text) + 4)
# print(line)
# print("| " + text + " |")
# print(line)




# import string
# from collections import Counter

# # 1. Count vowels
# vowels = "aeiouAEIOU"
# vowel_count = sum(1 for char in cleanedText if char in vowels)
# print("Total vowels:", vowel_count)

# # 2. Longest & shortest words
# clean_words = [w.strip(string.punctuation) for w in words]
# longest = max(clean_words, key=len)
# shortest = min(clean_words, key=len)
# print("Longest word:", longest)
# print("Shortest word:", shortest)

# # 3. Reverse paragraph
# reversed_para = cleanedText[::-1]
# print("Reversed paragraph:\n", reversed_para)

# # 4. Most frequent word
# word_count = Counter(clean_words)
# most_common_word = word_count.most_common(1)[0]
# print("Most frequent word:", most_common_word)

# # 5. Remove duplicate words
# unique_words = []
# for w in clean_words:
#     if w.lower() not in [uw.lower() for uw in unique_words]:
#         unique_words.append(w)
# print("Unique words:", unique_words)

# # 6. Sort words alphabetically
# sorted_words = sorted(clean_words, key=str.lower)
# print("Sorted words:", sorted_words)
