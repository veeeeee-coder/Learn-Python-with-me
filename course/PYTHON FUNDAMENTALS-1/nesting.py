username=input("enter username:")
password=input("enter pwd:")
if username=="admin" and password=="root":
    print("aaya sher")
else:
    if(username!="admin"):
        print("wrong uname")
    else:
        print("wrong pwd")