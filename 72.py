# Read and display file contents line by line.
file = open("user_data.txt", "r")

for line in file:
    print(line.strip())

file.close()