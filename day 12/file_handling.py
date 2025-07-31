#open and read file
# 'r'-read 'w'-write 'a'-append 'x'-exclusive creation 't'-text mode(default) 'b'-binary mode
f = open('operations.txt', 'r')
operations = f.readlines()
print(operations)
f.close()

#using 'with', it automatically closes the file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file!")

#Apeending to a file
with open("example.txt", "a") as file:
    file.write("\nThis line is appended.")

#reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())


