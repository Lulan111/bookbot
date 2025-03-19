def word_count(book_text):
    anzahl = len(book_text.split())
    return anzahl 

def letter_count(book_text):
    letters = {} 
    for buchstabe in book_text.lower():
        if buchstabe in letters:
            letters[buchstabe] += 1
        else:
            letters[buchstabe] =  1
    return letters

def sorted_list(menge):
    formatted_list = [
    f"{buchstabe}: {anzahl}" 
    for buchstabe, anzahl in sorted(menge.items(), key=lambda x: x[1], reverse=True)
]
    return [line for line in formatted_list if line[0].isalpha()]