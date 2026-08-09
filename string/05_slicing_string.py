#                 slicing in python 

# slicing :- String slicing means taking a part of a string.

"""
Syntax:- string[start:end]

start = where to begin
end = where to stop (exclusive)

* importent:-

If you skip start, it starts from the beginning.
If you skip end, it goes to the end.
"""
# example :-

word = "Python"
print(word[0:3])

print(word[0:len(word)])

print(word[: 4])

print(word[3:])

#                                                   negitive indexing string

# Negative indexing in a string means accessing characters from the end of the string.

place = "Dehradun"

print(place[-5: -1])