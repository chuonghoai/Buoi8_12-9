import os
os.system('cls')
a = [(0, 0), (5, 6)]
b = [(0, 0), (1, 1), (2, 2)]

i = 0
c = True
while True:
    if i + 1 > len(a) or i + 1 > len(b):
        break
    mot = (a[i][0], a[i][1])
    hai = (b[i][0], b[i][1])
    if mot != hai:
        c = False
        # print("False")
    i += 1

# if c:
    # print("true")

print(a[len(a) - 1][1])