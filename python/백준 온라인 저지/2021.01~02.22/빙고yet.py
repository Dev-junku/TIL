from sys import stdin

arr1 = []
for _ in range(5):
    arr1.append(list(map(int, stdin.readline().rstrip().split())))

arr2 = []
for _ in range(5):
    arr2.extend(list(map(int, stdin.readline().rstrip().split())))


def bingo_func(arr_list):
    
    bingo = 0
    if arr_list[0][0] + arr_list[1][1] + arr_list[2][2] + arr_list[3][3] + arr_list[4][4] == 0:
        bingo += 1
    if arr_list[0][4] + arr_list[1][3] + arr_list[2][2] + arr_list[3][1] + arr_list[4][0] == 0:
        bingo += 1
    
    for i in range(len(arr_list)):
        if sum(arr_list[i]) == 0:
            bingo += 1
        col = []
        for j in range(len(arr_list)):
            col.append(arr_list[j][i])
        if sum(col) == 0:
            bingo += 1
    
    if bingo >= 3:
        return True
    
    else:
        return False

res = False
for k in range(25):
    for i in range(5):
        for j in range(5):
            if arr1[i][j] == arr2[k]:
                arr1[i][j] = 0
        if k > 11:
            res = bingo_func(arr1)
            if res:
                break
    if res:
        print(k + 1)
        break