# String
string = "Hello, World"

# Integer
integer = 9

# Float
decimal = 1.258251

# Boolean
condition = True


# Not Python, only lower-level languages C, C++, C#
# char
character = '>'

# unsigned integer
unsigned = 4200526 # 0 to 428254726

#long
long = 24269219856
######################################################

# Advanced data types
list_one = [1, "cat", 2.3]





# temperature = 80

# if temperature > 70:
#     print("It's kinda hot outside")
# elif temperature < 70:
#     print("It's kinda cold")
# else:
#     print("Just right")


# print("Even" if 16 % 2 == 0 else "Odd")


# for index in range(0, 10): # 1 to 10 -> iterations = end - start = 11 - 1 = 10
#     print(f"Loop iteration: {index}")


# # From 60 to 120 inclusive
# for i in range(60, 121):
#     print(i)


# temperature = 70

# while temperature <= 80:
#     print(temperature)
#     temperature += 1

############### 0   1   2   3   4   5
# temperatures = [80, 70, 52, 40, 30, 20]

# total = 0

# for index in range(len(temperatures)):
#     temperature = temperatures[index]
#     total = total + temperature

# print(total)



# total = 0

# for temperature in temperatures:
#     total = total + temperature

# average = total / len(temperatures)

# print("Average temperature: " + str(average))


# # print the total amount of numbers greater than 50
# numbers = [16, -2, 9, 20, 99, 81, 72, 50, 1, 0, 0, 100]

# # Counts the total amount of numbers greater than 50.
# total = 0

# for num in numbers:
#     if num > 50:
#         total += 1
# print(total)


# func name | arguments 
def my_print(n = 1, i = 0, r = 0):
    for _ in range(n):
        print("hi")
    for _ in range(i):
        print("hello")
    for _ in range(r):
        print("wow")


# Make a function that prints the given string word only if the length of the word is greater than 5
# If it is 5 or less in length, print 'too short'.
# Example: "octagon" -> length 7 -> print 'octagon'
# Example: "dog" -> length 3 -> print 'too short'

def word(w):
    number = 10
    if len(w) > 5:
        print(w)
    else:
        print("too short")


sentence = "I went to the store the other day and I got some apples."
queue = "queue"

# for char in sentence:
#     char = char + char * 5
#     print(char)
# print(sentence)

# print(sentence.split(" "))
# ['I', 'went', 'to', 'the', 'store', 'the', 'other', 'day', 'and', 'I', 'got', 'some', 'apples.']


# print("")
# print(queue.count("u") + queue.count("e"))

# TODO: scheduling: tues/thurs 5:30 cst


# Make a number guessing game.
# User inputs a number until they get it right.
# Hidden number is randomly generated.
# input() -> int()
1
user_input = input("Input your guess: ")

print(user_input)

print(type(user_input))




