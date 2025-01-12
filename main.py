
def count_words(book):
    return len(book.split()) 

def sort_on(dict):
    return dict["count"]

def count_characters(book):
    characters = {}
    for character in book:
        if character.isalpha():
            character = character.lower()
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
                
    characters_count = [{"name": character, "count": count} for character, count in characters.items()]
    characters_count.sort(key=sort_on, reverse=True)
    return characters_count


with open('github.com/DrPhil/bookbot/books/frankenstein.txt', 'r') as file:
    book = file.read()
    words = count_words(book)
    characters = count_characters(book)
   
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f'{words} words found in the document')
    for character in characters:
        print(f'The {character["name"]} character was found {character["count"]} times')
    print("--- End report ---")
     
    