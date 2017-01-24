# -*- coding: utf-8 -*-
"""Code snippet with several errors. can you debug and find the error?. If the code executes successfully it will provide a success message.
   a. Run the code line by line using the debug tools. 
   b. Insert breakpoint inside the while loop and execute the loop one by one 
   c. Use the variable window and insert the local variable "char" and "i" in it. """
   
import ctypes

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def debug():
    """This function uses a global list "alphabet" and strows each character in a local variable "char" """
    char = " "
    i = 0    
    while i <= 26:
        i=0
        char = alphabet[i]
        i = i + 1

    if alphabet[i] == 'Z':
        return i
    else: return 0

def main():
    if ( debug() == 25 ): ctypes.windll.user32.MessageBoxW(0, "Success ! ", "Congratulations",1 )        
    else: print('Failed')
    
if __name__ == '__main__':
    main()