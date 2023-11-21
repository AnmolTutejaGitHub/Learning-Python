#Random in python

# Random Float:

# To generate a random float between 0 and 1, you can use the random() function.
# python
import random

random_float = random.random()
print(random_float)

# Random Integer:

# To generate a random integer within a specified range, you can use the randint(a, b) function.
# python


# Generates a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print(random_integer)

# Random Choice:

# To randomly choose an element from a sequence (e.g., a list), you can use the choice(seq) function.

my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print(random_element)


# Random Shuffle:
# To randomly shuffle the elements of a sequence, you can use the shuffle(seq) function.


my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

# Random Gaussian (Normal) Distribution:

# To generate random values from a Gaussian (normal) distribution, you can use the gauss(mu, sigma) function.


mean = 0
standard_deviation = 1
random_value = random.gauss(mean, standard_deviation)
print(random_value)
