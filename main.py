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

# scheduling: tues/thurs 5:30 cst

# for word in ["hello", "world"]:
#     print(word)


# # Returning values
# def add(a, b):
#     return a + b


# result = add(5, 2)

# print(result) # 7


# for char in "hello":
#     print(char)




# Write a function hasChar(str, char) that returns whether a string has a given character in it
# Example 1: hasChar("hello", "e") -> return True
# Example 2: hasChar("hello", "z") -> return False
# Iterate over the characters in the string
the_string = "hello"

def hasChar(string, char):
    for c in string:
        if c == char:
            return True
    
    return False


# word = input("Word: ")
# char = input("Letter to find: ")
# print(hasChar(word, char))

"a".upper() # A


def capitalize(word: str):
    print(word.upper())

caps = "hello"
# capitalize(caps)


# write a function findMaximum(array) that finds the highest number in an array of numbers
# Example: findMaximum([1, 2, 3]) => return 3
# Example: findMaximum([]) => return None
array = [1, 6, 89, 102, 47, 88, 405, 156, 85]

def findMaximum(array):
    if len(array) == 0:
        return None
    
    highest = array[0]
    for num in array:
        if num > highest:
            highest = num
    return highest






# Object Oriented Programming
#


class Animal:
    def __init__(self, name: str, age: int, kind: str):
        self.name: str = name
        self.age: int = age
        self.kind: str = kind
    
    def noise():
        pass
    
    
    def who_am_i(self):
        print(f"I am {self.name} the really lazy {self.kind} of age {self.age}!")



# Dog extends Animal -> Dog is a subclass of Animal and inherits all methods/variables
class Dog(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "dog")
        self.noise()

    def noise(self):
        print(f"{self.name} says: woof")


class Cat(Animal):
    num_cats = 0
    cats = []

    def __init__(self, name: str, age: int):
        super().__init__(name, age, "cat")
        Cat.num_cats += 1
        Cat.cats.append(self)
        self.noise()

    def noise(self):
        print(f"{self.name} says: meow")
    
    @staticmethod
    def big_noise():
        for cat in Cat.cats:
            cat.noise()
    
    @staticmethod
    def get_num_cats():
        return Cat.num_cats





# pop = Cat("pop", 2)
# # pop.noise()
# # pop.who_am_i()
# lucy = Cat("Lucy", 3)
# Cat.big_noise()
# Juicy = Cat("Juicy", 37)
# print(Cat.get_num_cats())


# spike = Dog("spike", 5)
# spike.who_am_i()
# cuddles_the_dog_that_cuddles_you_a_lot = Dog("cuddles_the_dog_that_cuddles_you_a_lot", 1047) #fly years
# cuddles_the_dog_that_cuddles_you_a_lot.noise()


# create a class Person, every class needs __init__
class Person:
    def __init__(self, name: str, age: int, shirt_color: str):
        self.name = name
        self.age = age
        self.shirt_color = shirt_color
    
    def is_cool(self):
        if self.age > 16:
            print(True)
        else:
            print(False)
    
    def __str__(self):
        return f"{self.name} of age {self.age}, with shirt color of {self.shirt_color}"

braeden = Person("Braeden", 20, "White")
eli = Person("Eli", 11, "Black")
print(braeden)
print(f"{eli} and his name is pronounced \"EL-EEh\"")

braeden.is_cool()


# Create additional classes for Animal, expand Animal with more functions
# Example: old() if age > 50 print I'm really old 