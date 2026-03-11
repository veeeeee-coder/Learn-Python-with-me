# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")

# with open("practice.txt","r") as f:
#     data=f.read()

# newdata=data.replace("Java","Cpp")
# print(newdata)

# word = "learning"

# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("not found")


# exact line a word occurs
# def check_for_line():
#     word = "pyq"
#     data = True
#     line_no = 1

#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1

# print(check_for_line())



# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

# num = ""

# for i in range(len(data)):
#     if(data[i] == ","):
#         print(int(num))
#         num = ""
#     else:
#         num += data[i]





# count = 0

# with open("practice.txt", "r") as f:
#     data = f.read()

#     nums = data.split(",")

#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1

# print(count)


