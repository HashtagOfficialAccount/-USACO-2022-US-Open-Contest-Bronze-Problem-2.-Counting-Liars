import math
N = int(input())
G = []
L = []
for i in range(N):
    R = input().split()
    if R[0] == "G":
        G.append(int(R[1]))
    else:
        L.append(int(R[1]))

liars = math.inf
for i in G:
    liar = 0
    for x in G:
        if x > i:
            liar += 1
    for x in L:
        if x < i:
            liar += 1
    if liar < liars:
        liars = liar
for i in L:
    liar = 0
    for x in G:
        if x > i:
            liar += 1
    for x in L:
        if x < i:
            liar += 1
    if liar < liars:
        liars = liar
print(liars)
