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
    print(count)
# End of Func().    

def consntCount(sentence):
    print("Calculates counted consonants.")
# End of Func().
    
def wordCount(sentence):
    print("Calculates counted words.")
# End of Func().
    
def display():
    print("Displays counters.")
# End of Func().
    
def main():
    u_sentence = input("Type a sentence: ")
    list_word = u_sentence.split(" ")
    # consonants = consntCount(u_sentence)
    vowels = vowelCount(u_sentence)
    # words = wordCount(list_word)
    # display(u_sentence, consonants, vowels, words)
    
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