# 37. Write List to File

lines = ["Hello", "World"]
f = open("output.txt", "w")
for line in lines:
    f.write(line + "\n")
f.close()