n = int(input())
move = []
first = []
second = []
third = []
forth = []

for p in range(3):
    first.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

for q in range(3):
    second.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
for r in range(3):
    third.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
for s in range(3):
    forth.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

for i in range(n):
    move.append(list(map(int, input().split())))

for j in move:
    f = j[1] - 1
    r = j[2] - 1
    if j[0] == 1:
        first[f][r] += j[3]
    elif j[0] == 2:
        second[f][r] += j[3]
    elif j[0] == 3:
        third[f][r] += j[3]
    else:
        forth[f][r] += j[3]

for i in range(3):
    print(' ' + ' '.join(map(str, first[i])))

print("#" * 20)

for i in range(3):
    print(' ' + ' '.join(map(str, second[i])))
    
print("#" * 20)

for i in range(3):
    print(' ' + ' '.join(map(str, third[i])))
    
print("#" * 20)

for i in range(3):
    print(' ' + ' '.join(map(str, forth[i])))
  
