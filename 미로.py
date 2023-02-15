#2에서 0을 통해 3까지 올라간다

def dfs(row,col):
    st = []
    visited = [ [False] *N for _ in range(N)]
    st.append((row,col))
    visited[row][col] = True
    while st:
        # v = st.pop() #튜플 하나가 팝됨 귀찮으니 아래꺼씀
        row,col = st.pop()
        for dr ,dc in [(1,0),(-1,0),(0,1),(0,-1)]: #아래.위.오른.왼
            newr = row +dr
            newc =  col +dc
            if 0 <=newr<N and 0<= newc<N and arr[newr][newc] != 1 and not visited[newr][newc]:
                if arr[newr][newc] == 3:
                    return 1
                st.append((newr,newc))
                visited[newr][newc] = True
    return 0

TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    arr = [ list(map(int,input())) for _ in range(N) ]
    for row in range(N):
        # if 2 in arr[row]:
        if arr[row].count(2) == 1:
            col = arr[row].index(2)
            break

    ans = dfs(row,col)
    print(f'#{tc} {ans}')