#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

t1 = input("Enter a word").strip()
t2 = input("Enter a word").strip()
t3 = input("Enter a word").strip()
t4 = input("Enter a word").strip()
t5 = input("Enter a word").strip()
x = [t1, t2, t3, t4, t5]
print(x)