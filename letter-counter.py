"""
Author: Viernes, Michael
Submitted to: Mr. Danilo Madrigalejos
Submission date: December 4, 2021
Subject: Programming Logic and Design - HOMEWORK 07
"""

def vowelCount(sentence):
    
    count = 0
    
    for i in range(len(sentence)):
        for listvowel in "aeiou":
            if sentence[i] == listvowel:
                count += 1
    return count
    
# End of Func().    

def consntCount(sentence):
    
    count = 0
    
    for i in range(len(sentence)):
        for listvowel in "bcdfghjklmnpqrstvwxyz":
            if sentence[i] == listvowel:
                count += 1
    return count
    
# End of Func().
    
def wordCount(listword):
    
    count = 0
    
    for i in range(len(listword)):
        count += 1
    return count
    
# End of Func().
    
def display(*kwargs):
    
    
    print(f"""
    Output:
    
    The sentence: \"{u_sentence}\" with a length of {len(u_sentence)}
    The word count:{words}
    The consonants:{consonants}
    The vowels: {vowels}
    """)
# End of Func().
    
def main():
    u_sentence = input("Type a sentence: ")
    list_word = u_sentence.split(" ")
    consonants = consntCount(u_sentence)
    vowels = vowelCount(u_sentence)
    words = wordCount(list_word)
    display(u_sentence, consonants, vowels, words)
    
# End of Func().   
    

while True: # My template for usual main().
    main()
    quit = input("Quit (y/n): ")
    if quit is type(str):
        quit = quit.lower()
        print(quit)
    if (quit == 'y' or quit == 0):
        print("Closing...\n")    
        break
# End of main()

exit() # Exits python.