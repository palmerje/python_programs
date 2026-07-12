# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# print(word_per_page)
# print(pages)
# The issue is that word_per_page is being evaluated against the input instead of assigned the input


pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"The total words in the book is: {total_words}")