file_path = r"C:\Users\hp\Desktop\PrimeBatch\Day-5\sample.txt"

print("Trying to open:", file_path)

# Append mode
f = open(file_path, "a")
f.write("New text being appended\n to the file")
f.close()

# Read back and show content
f = open(file_path, "r")
data = f.read()
print("\nFile content after append:\n")
print(data)
f.close()
