#exception handling where in a sequential flow of program we get an error then next steps dont get executed but we have to find a way to even execute those steps w error so we try to manage these errors by handling them

try:
    x=int(input("enter x:"))
    ans=10/x
except ZeroDivisionError:
    print(f"Division by 0 is not allowed")

except ValueError:
    print(f"Invalid input")

else:
    print(f"ans={ans}")

finally:#print irrespective of presence of error or not
    print("end of program")

#look for built in exceptions in w3 schools


#In this case:
#If the user enters 0, the ZeroDivisionError block runs, and then finally executes.

#If the user enters invalid input like "abc", the ValueError block runs, and then finally executes.

#If the input is valid (e.g., 2), the else block runs, and then finally executes.

#So, the key idea is that finally acts like a guaranteed last step, ensuring certain code runs regardless of success or failure. This is especially important in real-world programs where leaving resources open or unfinished can cause bugs or system issues.




#Exception handling in Python is a mechanism used to **control what happens when runtime errors occur**, so that the program does not abruptly terminate and can continue executing the remaining logic. In a normal sequential flow, if an error like division by zero or invalid input happens, Python immediately stops execution and throws an exception. Exception handling allows you to **intercept these errors and respond gracefully**, ensuring the program remains stable and user-friendly instead of crashing.

#The `try` block is where you place the code that **might cause an error**. In your example, `x = int(input("enter x:"))` can raise a `ValueError` if the user enters something that cannot be converted to an integer, and `ans = 10/x` can raise a `ZeroDivisionError` if the user enters `0`. Python executes the `try` block normally, but the moment it encounters an error, it **stops executing the rest of the try block and jumps to a matching `except` block**.

#The `except ZeroDivisionError` block specifically handles the case where division by zero occurs. Instead of crashing, the program prints a meaningful message: `"Division by 0 is not allowed"`. This ensures that the user understands what went wrong without seeing a technical error trace. Importantly, only this block runs if that specific error occurs—other types of errors will not be handled here.

#The `except ValueError` block handles invalid input, such as when the user types a string like `"abc"` instead of a number. When `int()` fails to convert the input, Python raises a `ValueError`, and this block catches it and prints `"Invalid input"`. By having multiple `except` blocks, you can **handle different types of errors in different ways**, making your program more precise and robust.

#The `else` block executes only if **no exception occurs in the try block**. That means both the input conversion and division were successful. In that case, it prints the result using `print(f"ans={ans}")`. If any exception is raised, the `else` block is skipped entirely. This separation keeps the normal execution logic clean and distinct from error-handling logic.

#The finally block in exception handling is used to define code that must execute no matter what happens, whether an exception occurs or not. It runs after the try, except, and even the else block (if present). This makes it ideal for cleanup operations, such as closing files, releasing resources, or freeing memory—tasks that should always happen to keep the program stable.

#In the flow of execution, Python first runs the try block. If an exception occurs, it jumps to the matching except block; if no exception occurs, it executes the else block. After all of these, the finally block is always executed, regardless of whether an error was raised, handled, or even if there was a return statement earlier. This guarantees that critical cleanup code is never skipped.

#Overall, this structure ensures that even if an error occurs, the program does not terminate unexpectedly. Instead, it **handles the error, informs the user, and maintains control over execution flow**. This is crucial in real-world applications where programs must be resilient and continue operating despite unexpected inputs or conditions.
