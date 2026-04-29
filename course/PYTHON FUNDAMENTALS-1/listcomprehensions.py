squares=[]
for i in range(6):
    squares.append(i*i)
print(squares)

#INSTEAD OF ABOVEEEEEE

#USSEEE
#[output for item in iterable if condition]
#[output iterable condition]

sq=[i*i for i in range(6)]
print(sq)

#if u want only odd numbers
sqo=[i*i for i in range(6) if i%2!=0]
print(sqo)

#nums=[-2,-4,3,5,2,-1]
#nums=[0,0,3,5,2,0]

nums=[-2,-4,3,5,2,-1]
nums=[0 if val < 0 else val for val in nums]
print(nums)

words=["veee","geethu","love"]
words=[val.upper() for val in words]
print(words)

#List comprehension in Python is a concise and expressive way to create lists in a single line, combining iteration, optional filtering, and transformation into one compact structure. Its basic syntax is `[expression for item in iterable]`, where the iterable can be any sequence like a list, string, or range, and the expression defines what gets stored in the new list. For example, `[x*x for x in nums]` generates a list of squares, replacing a longer loop that appends values manually. You can also include a condition to filter elements, such as `[x for x in nums if x % 2 == 0]`, which selects only even numbers. Additionally, list comprehensions support conditional expressions for transformation, like `["even" if x % 2 == 0 else "odd" for x in nums]`, where every element is included but modified based on a condition.

#They also handle nested loops, allowing combinations like `[(x, y) for x in [1, 2] for y in [3, 4]]`, and are commonly used to flatten structures, such as converting a 2D list into a 1D list with `[num for row in matrix for num in row]`. Compared to traditional loops, list comprehensions are generally faster and more readable due to Python’s internal optimizations, though overly complex ones can reduce clarity and should be avoided. A closely related concept is the generator expression, written with parentheses instead of square brackets, which produces values lazily rather than storing them all in memory, making it more efficient for large datasets. Overall, list comprehension is a powerful and widely used Python feature that enables clean, efficient, and readable list creation and transformation.
