
try:
    fptr=open("file2.txt","r")
    try:
        fptr.write("Hello how are you")
    finally:
        fptr.close()
        print("file closed")
except Exception as e:
    print(e)
