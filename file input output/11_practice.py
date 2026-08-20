# quesion 1:- create a file "practice.txt" using python. add the following data in it:
'''
hi everyone
we are learning file I/O.
using java.
i like programming in java. 
'''

with open("practice.txt", "w") as f:
    f.write("hi everyone! \nWe are learning file I/O. \n")
    f.write("using java.\nI like programming in java.")


#question 2:- WAF that replace all occurrences of "java" with "python" in above file.

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

#question 3:- search if the word "learning" exists in the file or not.

word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

# question 4:- WAF in which line of the file does the word "learning" occur first.
# print -1 if word not found.

def chek_for_line():
    word = "programming"
    data = True
    line_No = 1

    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(f"word found in line : {line_No}")
                return line_No
            line_No += 1

    print("number not found! ")
    return -1
chek_for_line()


#question 5:- from a file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("temp.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)