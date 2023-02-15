exp = '2+3*4/5'
isp = {'+':1,'-':1,'*':2,'/':2}
#glol = '234*5/+'
#스택을 사용해 연산자우선순위를 제어
#+는 스택에 넣어놓고 다음 연산자와 순위 비교
st = []
for c in exp:
    if c.isdigit(): #숫자면 그냥 출력
        print(c)
    else: #숫자가 아니면 
        if len(st)> 0 and isp[st[-1]] > isp[c]: #스택에 있는게 c보다 우선순위가 높으면? # <= 붙이면 안됨
            print(st.pop())
            st.append(c)
        else:
            st.append(c)
    
    while st: #스택에 남아 있는 데이터 처리
        print(st.pop())


#괄호 있는 ver

def step1(exp):
    isp = {'+': 1, '-': 1, '*': 2, '/': 2 '(': 0}  # 팝할때 우선순위
    icp = {'+': 1, '-': 1, '*': 2, '/': 2 '(': 3}  # 들어올때 우선순위


exp = '(6+5*(2-8)/2)'

goal = '6528-2/*+'
st = []
result = []
for c in exp:
    if c.isdigit():  # 숫자면 그냥 출력
        # print(c)
        result.append()
    elif c == ')' : #스택 사이즈 체크. 왼쪽 괄호 나올때 까지 팦
        while st and st[-1] != '('
            st.append(c)
            # print(st.pop())
        st.pop()
    else:  # 숫자가 아니면 
        if len(st) > 0 and isp[st[-1]] > icp[c]:  # 스택에 있는게 c보다 우선순위가 높으면? # <= 붙이면 안됨
            result.append(st.pop())
            # print(st.pop())
            st.append(c)
        else:
            st.append(c)

    while st:  # 스택에 남아 있는 데이터 처리
        print(st.pop())
        result.append(st.pop())

    return result



#숫자가 나오면 스택에 넣고 오퍼가 나오면 계산
def cal(v1,v2,op):
    if op == '+':
        return v1+v2
    if op == '*':
        return v1*v2
    if op == '/':
        return v1//v2
    if op == '-':
        return v1-v2


def step2(exp):
    st = []
    for c in exp:
        if c.isdigit():
            st.append(int(c))
        else:
            v2 = st.pop()
            v1 = st.pop()
            # t = cal(v1,v2,c)
            st.append(cal(v1,v2,c))
    return st[-1]

exp = '(6+5*(2-8)/2)'
post = step1(exp)
print(step2())

#백트래킹
#{1,2,3,4,5,6,7,8,9,10}
# 연습문제 원소의 합이 10인경우?

#완전검색을 위한 기본알고리즘

nums = [1,2,3]
N = 3
a = [-1] * N
#[0,0,0], [0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1]...부분집합

def construct_candidates(c):
    for i in range(N):
        if i not in a[0:k]:
            c[pos] = i
            pos += 1
    return pos
    # c[0] = 0
    # c[1] = 1
    # return 2

def backtrack(c,k)
    c = [-1]* N  #후보 배열넣기
    if k == N :
        print(a)
        return

    construct_candidates(c) #후보군 만들어주는 함수
    for i in range(nc):
        a[k] = c[i]  #i는 후보의 갯수별 인덱스
        backtrack(a,k+1)

backtrack(a,0)

nums = [1,2,3,4,5,6,7,8,9,10]
N = 3
#goal = [0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1]...
#재귀를 이용한 방법


c= [0,1]
def partial(k,curS):
    if curS > 10:
        return

    if k ==N :
        print(a,'=',end=' ')#부분집합 출력
        print(curS)
        if curS == 10:
            for i in range(N):
                if a[i] ==1:
                    print(nums[i], end= ' ')
            print()
        sumV = 0
        for i in range(N):
            if a[i]:
                sumV += nums[i]
        print(sumV)
        return
    c[0] = 0
    c[1] = 1
    # c = [] *후보의 갯수
    # nc = c_c(c)
    a[k] = 0
    partial(k+1,curS+nums[k])
    a[k] = 1
    partial(k+1,curS + nums[k])
    # for i in range(2):
    #     a[k] = c[i]
    #     if c[i] ==1:
    #         partial(k+1, curS+nums[k])
    #     else:
    #         partial(k+1,curS)
    #     partial(k+1,)
    pass

a = [-1] *N #goal[i]
partial(a,0)

#지금까지의 합을 판단하여 유망한지 아닌지를 판단


c= [0,1]
def partial(k,curS):
    if curS> 10:
        return

    if k==N:
        # print(a)
        sumV = 0
        if curS == 10:
            for i in range(N):
                if a[i]:
                    print(nums[i],end='')
                # sumV += nums[i]
            print(curS)
        return

    a[k] = 0
    partial(k+1)
    a[k] = 1
    partial(k + 1,curS+nums[k])
    # for i in range(2):
    #     a[k] = c[i]
    #     partial(k+1)

    c = [0, 1]



    def partial(k, curS):

        if k == N:
            print(a)
            return

        a[k] = 0
        partial(k + 1)
        a[k] = 1
        partial(k + 1, curS + nums[k])

 a= [-1]*N
 partial(0,0)