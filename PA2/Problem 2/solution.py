import math


def merge_sorted_arrays(array_a, array_b, p_min_y):
    angle_a = []
    angle_b = []
    array_c = []
    len_c = len(array_a) + len(array_b)
    pointer_a = 0
    pointer_b = 0
    for i in range(len(array_a)):
        den = array_a[i][0] - p_min_y[0]
        if den == 0:
            angle = math.pi / 2
        else:
            angle = math.atan((array_a[i][1] - p_min_y[1]) / den)
            if angle < 0:
                angle = angle + math.pi
        angle_a.append(angle)
    for i in range(len(array_b)):
        den = array_b[i][0] - p_min_y[0]
        if den == 0:
            angle = math.pi / 2
        else:
            angle = math.atan((array_b[i][1] - p_min_y[1]) / den)
            if angle < 0:
                angle = angle + math.pi
        angle_b.append(angle)
    for i in range(len_c):
        if pointer_a == len(array_a):
            array_c.extend(array_b[pointer_b:])
            break
        if pointer_b == len(array_b):
            array_c.extend(array_a[pointer_a:])
            break
        if angle_a[pointer_a] == angle_b[pointer_b]:
            dist_a = math.sqrt((array_a[pointer_a][0] - p_min_y[0]) ** 2 + (array_a[pointer_a][1] - p_min_y[1]) ** 2)
            dist_b = math.sqrt((array_b[pointer_b][0] - p_min_y[0]) ** 2 + (array_b[pointer_b][1] - p_min_y[1]) ** 2)
            if dist_a < dist_b:
                array_a.pop(pointer_a)
                angle_a.pop(pointer_a)
            else:
                array_b.pop(pointer_b)
                angle_b.pop(pointer_b)
            len_c -= 1
            i -= 1
            continue
        elif angle_a[pointer_a] < angle_b[pointer_b]:
            array_c.append(array_a[pointer_a])
            pointer_a += 1
        else:
            array_c.append(array_b[pointer_b])
            pointer_b += 1
    return array_c


def merge_sort_angle(array_c, p_min_y):
    n_c = len(array_c)
    if n_c <= 1:
        return array_c
    return merge_sorted_arrays(merge_sort_angle(array_c[:n_c // 2], p_min_y),
                               merge_sort_angle(array_c[n_c // 2:], p_min_y), p_min_y)


def graham_scan(P):
    min_y = 101
    p_min_y = [101, 101]
    for i in range(len(P)):
        if P[i][1] == min_y:
            if P[i][0] < p_min_y[0]:
                p_min_y = P[i]
        elif P[i][1] < min_y:
            p_min_y = P[i]
            min_y = P[i][1]
    P.remove(p_min_y)
    SP = merge_sort_angle(P, p_min_y)
    SP.insert(0, p_min_y)
    stack = [SP[0]]
    if len(SP) == 1:
        return stack
    stack.append(SP[1])
    if len(SP) == 2:
        return stack
    stack.append(SP[2])
    for i in range(3, len(SP)):
        while len(stack) >= 3:
            pa = stack[-1]
            pb = stack[-2]
            pi = SP[i]
            orientation = (pb[1] - pa[1]) * (pi[0] - pb[0]) - (pb[0] - pa[0]) * (pi[1] - pb[1])
            if orientation >= 0:
                break
            else:
                stack.pop()
        stack.append(SP[i])
    return stack


n = int(input())
if n == 0:
    exit(0)
P = []
for i in range(n):
    P.append(list(map(float, input().strip(' ').split(' '))))
    P[i][1] = -P[i][1]
CHP = graham_scan(P)
print(CHP)
p_min_x_index = 0
p_max_x_index = 0
min_x = 101
max_x = -101
for i in range(len(CHP)):
    if CHP[i][0] < min_x:
        p_min_x_index = i
        min_x = CHP[i][0]
    if CHP[i][0] > max_x:
        p_max_x_index = i
        max_x = CHP[i][0]
counter_LE = 0
if p_min_x_index == 0:
    counter_LE = len(CHP) - p_max_x_index + 1
else:
    counter_LE = p_min_x_index - p_max_x_index + 1
counter_UE = len(CHP) - counter_LE + 2
print(str(counter_UE) + " " + str(counter_LE))
