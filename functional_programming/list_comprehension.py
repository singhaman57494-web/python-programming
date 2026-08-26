#   map jaisa kaam

number = [1, 2, 3, 4, 5]

squares = [x * x for x in number]

print(squares)


#         filter jaisa kaam

scores = [45, 88, 92, 33, 67, 78, 49]

passing = [x for x in scores if x >= 50]

print(passing)


#             practice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_even = [x * x for x in numbers if x % 2 == 0] 

print(square_even)