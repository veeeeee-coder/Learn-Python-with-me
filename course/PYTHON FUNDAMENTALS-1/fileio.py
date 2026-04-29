
#we have diff files .txt,.csv
#whenever we need to read or write in a file we use file io functions
#how to open operations like read write append delete close
#The "Restaurant" AnalogyTo make it click, imagine you are at a restaurant:Opening the Menuopen("menu.txt", "r")You have the menu in your hand, and you are allowed to look at it.Looking at the itemsf.read()You are actually processing the information with your eyes.Closing the Menuf.close()You put the menu back on the table.

#1. open(..., "r") is like Opening a Book
#When you use f = open("data.txt", "r"), you are telling Python:

#Find this specific file.

#Get ready to access it.

#Set the mode: "r" stands for Read. This ensures you don't accidentally overwrite or delete anything. It’s like picking up a book and holding it in your hands, but you haven't actually looked at the words on the page yet.

#2. f.read() is like Actually Reading the Words
#The variable f is a file object (or a "pointer"). It represents the connection to the file, not the content itself.

#f.read() tells Python to go into that opened file, start at the very first character, and pull all the text into a string variable (which you named data).

#ithout .read(), if you tried to print(f), you wouldn't see your text; you would see a technical description of the file object (like <_io.TextIOWrapper ...>).
#file operations
#f= open("data.txt","r")
f=open("data.txt","a+")
#first argument is filename or path of the file and second is mode in which we want to use the file
#if that file is in outside of folder we need to give absolute file path orelse just give the file name
#file opens and gives file object
#data=f.read()
#data=f.readline() #do it multiple times to get another lines,, pointer by pointer reading lines
f.write("234ded")
print(f.read())
#print(data)
f.close()
#the most imp thing is to close the file to avoid unexpected changes 
#readline reads line by line

#while writing the previous file is overrided means previous info is gone we write new data into it,we replace old text with new one