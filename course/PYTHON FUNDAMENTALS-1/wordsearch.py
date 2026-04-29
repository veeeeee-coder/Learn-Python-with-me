data=True
line=1
word="Python"

with open("sample.txt","r") as f:
    while data:
        data=f.readline()

        if(word in data):
            print(f"{word} found at line {line}")
            break

        line+=1
