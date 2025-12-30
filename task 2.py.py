# Task 2: Write, append, and read data from a file

filename = "output.txt"

# Take input and write to file
text = input("Enter text to write to the file: ")

with open(filename, "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.")

# Take more input and append
more_text = input("Enter additional text to append: ")

with open(filename, "a") as file:
    file.write(more_text + "\n")

print("Data successfully appended.")

# Read and display final content
print("\nFinal content of output.txt:")
with open(filename, "r") as file:
    print(file.read())
