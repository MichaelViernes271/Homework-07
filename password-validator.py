"""
Author: Viernes, Michael
Submitted to: Mr. Danilo Madrigalejos
Submission date: December 4, 2021
Subject: Programming Logic and Design - HOMEWORK 07
"""


def capsValid(u_code):
    caps = filter((lambda x: x.isupper()), u_code)
    if len(list(caps)) > 0:
        print("caps valid")
        return True
    else:
        return False
    # print("Validates Capital letters.")
    
def charLenValid(u_code):
    if len(list(u_code)) > 15:
        print("charlenvalid")
        return True
    else:
        return False
    # print("Validates character length.")
    
def numValid(u_code):
    nums = filter((lambda x: x.isnumeric()), u_code)
    if len(list(nums)) > 0:
        print("numvalid")
        return True
    else:
        return False
    # print("Validates digits.")

def speCharValid(iterator):
    
    SPEC_CHARS = "~!@#$%^&*()_+[]\;',./{}|:<>?()"

    
def display(validity):
    if validity == True:
        print("The Password is VALID.")
    else:
        print("The Password is INVALID.")
    
def main():
    
    u_validity = False
    
    passcode = str(input("Enter a passphrase for validity: "))

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
