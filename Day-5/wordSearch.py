data = True
line = 1
word = "python"

with open(r"C:\Users\hp\Desktop\PrimeBatch\Day-5\sample.txt", "r") as f:
    
    while data:
        data = f.readline()
        
        if(word in data):
            print(f"{word} found at line {line}")
            break
        print(data)
        line += 1
    
    
    