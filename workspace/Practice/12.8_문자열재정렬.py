data = input()
eng = []
num = 0

for i in data:
    if i.isalpha():
        eng.append(i)
    else:
        num += int(i)
        
eng.sort()

for i in eng:
    print(i, end="")
print(num)
