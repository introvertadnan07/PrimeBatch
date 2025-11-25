file_path = r"C:\Users\hp\Desktop\PrimeBatch\Day-5\sample.txt"

f = open(file_path, "r+")
data = f.read()
print("Old content:", data)

f.write("\nNew text added using r+")
f.close()
