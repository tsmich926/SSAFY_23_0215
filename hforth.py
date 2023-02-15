def cal(c,a,b):
    if c == '/':
        ans = int(a)//int(b)
        return ans
    elif c == '*':
        ans = int(a) * int(b)
        return ans
    elif c == '-':
        ans = int(a) - int(b)
        return ans
    elif c == '+':
        ans = int(a) + int(b)
        return ans

def fol(exp):
    st = []
    for c in exp:
        if c.isdigit():  # 숫자면 스택에 넣음
            st.append(c)
        elif c == '/' or c == '*' or c == '+' or c == '-':  # 숫자나 .이 아니면 연산자?
            if len(st) >= 2:
                b = st.pop()
                a = st.pop()
                ans = cal(c,a,b)
                st.append(ans)
            else:
                return 'error'
        if c == '.':
            if len(st) == 1:
                ans2 = st.pop()
            else:
                ans2 = 'error'
    return ans2


TC = int(input())
for tc in range(1,TC+1):
    exp = input().split()
    ans2 = fol(exp)
    print(f'#{tc} {ans2}')
