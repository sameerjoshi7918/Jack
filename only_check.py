with open(r'memory\names.txt','a') as file:
    file.write(' namaste')
with open(r'memory\names.txt','r') as file:
    print(file.read())
