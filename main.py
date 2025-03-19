def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        inhalt = f.read()
    return inhalt
file_path = "books/frankenstein.txt"
book_text = get_book_text(file_path)

def word_count(book_text):
    anzahl = len(book_text.split())
    return anzahl 
anzahl = word_count(book_text)
print(f"{anzahl} words found in the document")