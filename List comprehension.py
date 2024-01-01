# List Comprehension is a concise way to create a list.
# It reads like a sentence: "create a list of x for each y in z"

# An example
squares = [x**2 for x in range(10)]
print(squares)

# The If clause can be used as a filter.
# An example: Create a list squares for even numbers
even_squares = [x**2 for x in range(10) if x%2 == 0]
print(even_squares)