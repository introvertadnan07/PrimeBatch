file_path = r"C:\Users\hp\Desktop\PrimeBatch\Day-5\sample.txt"

f = open(file_path, "w+")
f.write("Fresh content written using w+")
f.seek(0)
print(f.read())
f.close()
