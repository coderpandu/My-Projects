# with open(r"C:\Users\sumee\Desktop\oop in python\File_Input_Output\demo.txt", "r") as f:
#     data = f.read()
#     print(data)


# f = open("File_Input_Output\demo.txt", "r")
# data = f.read()
# print(data)
# f.close()

# f = open("File_Input_Output\demo.txt", "r")
# data = f.read(5)
# print(data)
# f.close()

# f = open("File_Input_Output\demo.txt", "r")
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)
# f.close()

# f = open("File_Input_Output\demo.txt", "w")
# f.write("I play Basketball\n")
# f.close()

# f = open("File_Input_Output\demo.txt", "a")
# f.write("I play Football")
# f.close()

# f = open("File_Input_Output\demo.txt", "r")
# data = f.read()
# print(data)

# with open("File_Input_Output\demo.txt", "a") as f:
#     f.write("\nHello Guys")


with open("File_Input_Output\practice.txt", "w") as f:
    f.write("Hi Everyone \nwe are learning file I/O \nusing java. \nI like a programming in java.")

with open("File_Input_Output\practice.txt", "r") as f:
    data = f.read()
    print(data)

# def replace_java_with_python(filename):
#     # Read the file
#     f = open(filename, "r")
#     data = f.read()
#     f.close()
    
#     # Replace "java" with "python"
#     new_data = data.replace("java", "python")
    
#     # Write back to file
#     f = open(filename, "w")
#     f.write(new_data)
#     f.close()
    
#     print("Replacement completed!")

# # Call the function
# replace_java_with_python("File_Input_Output\practice.txt")

with open("File_Input_Output\practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)

with open("File_Input_Output\practice.txt", "w") as f:
    f.write(new_data)
    
def check_for_word():
    word = "learning"
    with open("File_Input_Output\practice.txt", "r") as f:
        data = f.read()
        if (data.find(word) != -1):
            print("Word Found")

        else:
            print("Word Not Founf")

check_for_word()