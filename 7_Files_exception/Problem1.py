

# Copy content from one file to another file
try:
    with open(r'E:\Personal\Fessorpro\7_Files_exception\portfolio.txt','r') as f1:
        content=f1.read()
        print(content)

    with open('portfolio1.txt','w') as f2:
        f2.write(content)

except FileNotFoundError:
    print("File not found.")