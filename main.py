def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        inhalt = f.read()
    return inhalt

from stats import word_count

file_path = "books/frankenstein.txt"
book_text = get_book_text(file_path)
anzahl = word_count(book_text)

print(f"{anzahl} words found in the document")