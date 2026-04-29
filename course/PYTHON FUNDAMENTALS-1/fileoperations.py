#modes of file operations:
#r = reading (default)
#w = writing,truncates file first
#x = creates new and open for writing
#a = writing appends at end
#b = binary mode
#t = text mode(Default)
#+ = open disk file for update (r&w)

f=open("data.txt") #file object
print(f.read())
f.close() #here even if we didnt put r in open function by default it takes as reading mode

#write first deleted everything in file first then adds new information it overwrites the info
#write first clears all data then add new data but append operation just appends new data at the end of previous information append mode checks file ki end pointer then inserts new data

f=open("data.txt","a")
f.write("\n hey am new data woohoo \n fresh fresh")
f.close()

#x dedicatedly creates new file and writes
f=open("sample.txt","x")
f.write("heyy am a new file")
f.close()

#Write mode ('w') opens a file for writing and will overwrite the file if it already exists, meaning all previous content is deleted and replaced with new data; if the file does not exist, it simply creates a new one. In contrast, exclusive create mode ('x') is more strict—it only creates a file if it does not already exist, and if the file is already present, it raises a FileExistsError instead of modifying it. In short, 'w' is used when you don’t mind losing existing data, while 'x' is used when you want to ensure that no existing file is accidentally overwritten.

#there are different data formats like text,binary so we can read like rt,rb and write like wt,wb in this text mode is by default

# + is used for updations like using r and w at same time
#r+ → read + modify
#w+ → wipe + read/write
#a+ → append + read