import sys
import os

def check_sys():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

check_sys()

def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        inhalt = f.read()
    return inhalt

from stats import word_count
from stats import letter_count
from stats import sorted_list

file_path = sys.argv[1]  # Hier holst du den Dateipfad aus den Kommandozeilenargumenten
book_text = get_book_text(file_path)
anzahl = word_count(book_text)
menge = letter_count(book_text)
sortiert = sorted_list(menge)
pfad = os.path.basename(sys.argv[1])


print("============ BOOKBOT ============")
print(f"Analyzing book found at {pfad}...")
print("----------- Word Count ----------")
print(f"Found {anzahl} total words")
print("--------- Character Count -------")
for line in sortiert:
    print(line)
print("============= END ===============")