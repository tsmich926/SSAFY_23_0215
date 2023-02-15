nums = [1,2,3,4,5,6,7,8,9,10]
N = 10
#goal = [0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1]...
#재귀를 이용한 방법


c= [0,1]
def partial(k,curS):
    if curS > 10:
        return
    if k == N :
        if curS == 10:
            for i in range(N):
                if a[i]:
                    print(nums[i], end = ' ')
            print()
        # print(a)#부분집합 출력

        return

    a[k] = 0
    partial(k+1,curS)
    a[k] = 1
    partial(k+1,curS + nums[k])


a = [-1] * N
#goal[i]
partial(0,0)
