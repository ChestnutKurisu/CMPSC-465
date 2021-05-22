inputA = list(map(int, input().strip().split(' ')))  # O(a)
inputB = list(map(int, input().strip().split(' ')))  # O(b)
lenA = inputA[0]  # O(1)
lenB = inputB[0]  # O(1)
inputA.append(2147483648)  # O(1)
inputB.append(2147483648)  # O(1)

listC = []  # O(1)
pointerA = 1  # O(1)
pointerB = 1  # O(1)
listC.append(lenA + lenB)  # O(1)
for i in range(lenA + lenB):
    if inputA[pointerA] <= inputB[pointerB]:  # O(a + b)
        listC.append(inputA[pointerA])  # O(a + b)
        pointerA += 1  # O(a + b)
    else:
        listC.append(inputB[pointerB])
        pointerB += 1

for n in listC:  # O(a + b)
    print(n, end=' ')

# Time complexity: O(5a + 5b + 8) = O(a + b), where a and b are lengths of the two input arrays