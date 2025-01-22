def main(): #our main function, lets keep this at the top of our code and put other functions below it.
    book_path = "books/frankenstein.txt"    #this assigns a variable book_path as the file path to my text file
    text = get_book_text(book_path) #sets the variable text by inserting the book_path variable into the get_book_text function
    num_words = get_num_words(text) #this inputs the above variable into the get_num_words function and returns the integer number
    print(f"{num_words} words found in the document") #prints our number.

def get_num_words(text): #starting a new function that will split the words and count them.
    words = text.split() # splits the text in the string "text" into single words
    return len(words) #the function returns the number of words as len(words) counts the number of words in the string
    
def get_book_text(path): #a function that will take the path to the file and read the text
    with open(path) as f: #the with open() as f: reads the input inside open() and loads it to variable f
        return f.read() #returns the entire text as a string
    
    #my problem as a new developer is trying to give meaning to the parameters in the function. they are arbitrary
    #to make sense to the function and are normally a different value set by a differnt variable.
    # e.g. get_book_text(book_path) book_path is a variable that is passed to the get_book_text function
    # however, setting path in the function is arbitrary to the coder but in the function calls that value to set it to f
    # so the process so far is to take the the path, feed it to get_book_text, return that text, feed it to get_num_words
    # and that gives us the number of words in the book as an integer.
    
if __name__ == "__main__":
   
   main()

