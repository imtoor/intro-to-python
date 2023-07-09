book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

# iterate through list of book title and count every word contains in it
word_counter = {}

# method 1 -> using for loops
# for word in book_title:
#     if word not in word_counter:
#         word_counter[word] = 1
#     else:
#         word_counter[word] += 1

# method 2 ->  using get

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1

print(word_counter)