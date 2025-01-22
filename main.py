def main(): #our main function, lets keep this at the top of our code and put other functions below it.
    book_path = "books/frankenstein.txt"    #this assigns a variable book_path as the file path to my text file
    text = get_book_text(book_path) #sets the variable text by inserting the book_path variable into the get_book_text function
    num_words = get_num_words(text) #this inputs the above variable into the get_num_words function and returns the integer number
    letter_counter = get_letter_count(text)
    print(f"{num_words} words found in the document") #prints our number.
    print(letter_counter)

def get_num_words(text): #starting a new function that will split the words and count them.
    words = text.split() # splits the text in the string "text" into single words
    return len(words) #the function returns the number of words as len(words) counts the number of words in the string
    
def get_book_text(path): #a function that will take the path to the file and read the text
    with open(path) as f: #the with open() as f: reads the input inside open() and loads it to variable f
        return f.read() #returns the entire text as a string
    
def get_letter_count(text): #adding the letter counter function
    lowered_string = text.lower() #instantly lowercase my string
    letter_count = {} #new dictionary for the characters and counter

    for letter in lowered_string: #loops through each character in the string 
        if letter not in letter_count: # checks to see if its not in there, then adds it
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1 #if its in there it adds another to the counter
    return letter_count #returns the character, and how many times its in there
    #could provide clarity with changing letter with character, as this is counting more than
    #just letters. but i like the code the way it is. 

        



    #my problem as a new developer is trying to give meaning to the parameters in the function. they are arbitrary
    #to make sense to the function and are normally a different value set by a differnt variable.
    # e.g. get_book_text(book_path) book_path is a variable that is passed to the get_book_text function
    # however, setting path in the function is arbitrary to the coder but in the function calls that value to set it to f
    # so the process so far is to take the the path, feed it to get_book_text, return that text, feed it to get_num_words
    # and that gives us the number of words in the book as an integer.

if __name__ == "__main__":
   
   main()

