def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        inhalt = f.read()
    return inhalt

from stats import word_count
from stats import letter_count
from stats import sorted_list

file_path = "books/frankenstein.txt"
book_text = get_book_text(file_path)
anzahl = word_count(book_text)
menge = letter_count(book_text)
sortiert = sorted_list(menge)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {anzahl} total words")
print("--------- Character Count -------")
for line in sortiert:
    print(line)
print("============= END ===============")