angka1, angka2 = map(int, input().split())
if(angka1 < angka2):
    a = 1
    for i in range(angka1, angka2 + 1):
        x = angka2 - a + 1
        a +=  1
        if i == angka1:
            print(end="")
        else:
            print(" - ", end=" ")
        print(f"{i} {x}", end=" ")
else:
    a = 0
    for i in reversed(range(angka2, angka1 + 1)):
        x = angka2 + a
        a += 1
        if (i == angka1):
            print(end="")
        else:
            print(" - ", end=" ")
        print(f"{i} {x}", end=" ")