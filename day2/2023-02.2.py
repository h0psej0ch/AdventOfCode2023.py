data = open("data2.txt", 'r')
sum = 0

def pearlcheck(x, col):
    old = 0
    for i in range(0, len(x)):
        red = x.find(col)
        if red != -1:
            j = 2
            dig = x[red-j].isdigit()
            mul = 1
            pearl = 0
            while dig:
                pearl += int(x[red-j])*mul
                mul *= 10
                j += 1
                dig = x[red-j].isdigit()
            if pearl >= old:
                old = pearl
            x = x[red + len(col):]
            i = red + len(col) - 1
            i += 1
        else:
            break
    return old


count = 0
for x in data:
    pos = x.find(":")
    x = x[pos + 2:]
    found = x.find("red")
    count += 1
    sum += pearlcheck(x, "red") * pearlcheck(x, "green") * pearlcheck(x, "blue")
    print(sum)
    

