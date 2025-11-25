file_path = r"C:\Users\hp\Desktop\PrimeBatch\Day-5\sample.txt"

f = open(file_path, "a+")
f.write("\nAdded using a+ mode.")
f.seek(0)
print(f.read())
f.close()
