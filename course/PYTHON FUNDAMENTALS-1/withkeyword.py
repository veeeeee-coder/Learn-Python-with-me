#when we use with keyword by default after all operations it gets closed

with open("data.txt","r") as f:
    print(f.read())
    #can also do len(data)

#The with keyword in Python is used for automatic resource management, most commonly when working with files. It ensures that a file is properly opened and, more importantly, automatically closed after its block of code is executed, even if an error occurs during execution. Without with, you would need to manually call close(), and forgetting to do so can lead to issues like memory leaks or locked files. By using with open(...) as f, Python handles the setup and cleanup for you, making the code safer, cleaner, and easier to manage.

with open("data.txt", "r") as f:
    content = f.read()

#Similarly, writing to a file:

with open("data.txt", "w") as f:
    f.write("Hello World")

#And appending data:

with open("data.txt", "a") as f:
    f.write("\nNew Line")



#DELETING OF FILES we use special module called os(to interact w files(operating systems))
import os
os.remove("sample2.txt")