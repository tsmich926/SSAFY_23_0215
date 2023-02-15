#금요일 문제
# 1234
# 4615
# 1217
# 1224

#계산하는 과정 작성하기

#후위식으로 바꾸는 함수
def fol(exp):
    s_lst = []
    st = []
    for c in exp:
        if c.isdigit():  # 숫자면 스택에 넣음
            s_lst.append(c)
        elif c == '+':# 숫자나 .이 아니면 연산자?
            if len(st) == 0:
                st.append(c)
            else:
                a = st.pop()
                s_lst.append(a)
                st.append(c)

    return s_lst


for tc in range(1,11):
    N = int(input())
    s = input()
    print(fol(s))
    # print(f'{tc} {}')



--------------------계산 하는거

def cal(s_lst):
    st = []
    for num in s_lst:
        if num.isdigit():
            st.append(num)
        else:




