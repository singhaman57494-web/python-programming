#                          prectice question in list and tuple

# Question 1:- WAP to ask the user to enter name of there 3 favorite movies and store them in a list.

name1 = input("enter your favorite movie : ")
name2 = input("enter your favorite movie : ")
name3 = input("enter your favorite movie : ")

movies = [name1 , name2 , name3]

print(movies)

#              method 2

movie1 = input("enter your favorite movie : ")
movie2 = input("enter your favorite movie : ")
movie3 = input("enter your favorite movie : ")

movies =[]
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)


# question 2 :- wap to check if a list contains a palindrome of elements. (hint : use copy()method).

nums = [1, 2, 3, 2, 1]

reverse_nums = nums[::-1]

if reverse_nums == nums:
    print("list is palindrome")
else:
    print("not palindrome")