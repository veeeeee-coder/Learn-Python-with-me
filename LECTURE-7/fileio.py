#pythin can be used to perform operations on a file(read and write data)

#types of files text files .txt,.docx,.log(Char)
#binary files .mp4,.mov,.png,.jpeg(binary)
#all stored as bits only at last



#we have to open a file before reading or writing
#f=open("file_name","mode")
#mode can be read or write
#bydefault read


# f = open("demo.txt","r")
# data = f.read()

# print(data)
# print(type(data))

# f.close()
#close after finishing

#r-open for reading
#w open for writing truncating the file first
#x-create a new file and open it for writing
#a-open for writing appending to end of file if it exixts
#b-binary mode
#t-text mode
#+-open a disk for updating(reading and writing)


#reading a file
# f = open("demo.txt","r")
# data = f.read(5)#specifying no of characters

# print(data)
# print(type(data))

# f.close()

#f.read() reads entire line
#f.readline() reads one line at a time

# f=open("demo.txt","w")
# f.write("vee is ambitious. shes romanticising her life")
# f.close()
# #for overwriting the file 


# f=open("vee.txt","w")
# f.close()

# f=open("vee.txt","a")
# f.close()

# f=open("demo.txt","r+")
# f.write("abc")
# print(f.read())  #prints from i beacuse after writing the pointer stops there and again contiues from there onli
# f.close()



#using "with" syntax
# with open("demo.txt","a") as f:
#     data=f.read()

# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

# #with automatically closes our file

# with open("demo.txt","w") as f:
#     f.write("blehh")


#deleting a file
# using the os module 
# Module(like a code library) is a file written by another programmer that generally has a functions we can use

# import os
# os.remove("vee.txt")
