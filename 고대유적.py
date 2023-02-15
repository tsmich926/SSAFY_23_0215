T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    #가로 검사
    lst1 = []
    for row in range(N):
        sum1 = 0
        for col in range(M):
            if arr[row][col] == 1:
                sum1 += 1
                lst1.append(sum1)
    max1 = max(lst1)

    #세로 검사
    lst2 = []
    for col in range(M):
        sum2 = 0
        for col in range(M):
            if arr[row][col] == 1:
                sum2 += 1
                lst2.append(sum2)
    max2 = max(lst2)

    if max1 >= max2:
        print(f'#{tc} {max1}')
    else:
        print(f'#{tc} {max2}')
