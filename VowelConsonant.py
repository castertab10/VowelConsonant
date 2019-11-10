# Check whether a character is a vowel or a consonant

EnteredChar = input("Enter a character: ")


if(EnteredChar == "a" or EnteredChar == "e" or EnteredChar == "i" or EnteredChar == "o" or EnteredChar == "u" 
   or EnteredChar == "A" or EnteredChar == "E" or EnteredChar == "I" or EnteredChar == "O" or EnteredChar == "U"):
    print("The entered character is a vowel")
    
    
elif(EnteredChar == "b" or EnteredChar == "c" or EnteredChar == "d" or EnteredChar == "f" or EnteredChar == "g" 
   or EnteredChar == "h" or EnteredChar == "j" or EnteredChar == "k" or EnteredChar == "l" or EnteredChar == "m" or
   EnteredChar == "n" or EnteredChar == "p" or EnteredChar == "q" or EnteredChar == "r" or EnteredChar == "s" 
   or EnteredChar == "t" or EnteredChar == "v" or EnteredChar == "w" or EnteredChar == "x" or EnteredChar == "y" or EnteredChar == "z" or 
   EnteredChar == "B" or EnteredChar == "C" or EnteredChar == "D" or EnteredChar == "F" or EnteredChar == "G" 
   or EnteredChar == "H" or EnteredChar == "J" or EnteredChar == "K" or EnteredChar == "L" or EnteredChar == "M" or
   EnteredChar == "N" or EnteredChar == "P" or EnteredChar == "Q" or EnteredChar == "R" or EnteredChar == "S" 
   or EnteredChar == "T" or EnteredChar == "V" or EnteredChar == "W" or EnteredChar == "X" or EnteredChar == "Y" or EnteredChar == "Z"):
    print("The entered character is a consonant")
    
else:
   print("You have entered an invalid character. Please try again: ")
