def int_text(number):
    tnum = {0:'영', 1:'일', 2:'이', 3:'삼', 4:'사', 5:'오', 6:'육', 7:'칠', 8:'팔', 9:'구'}
    if number < 10:
        return(tnum[number])
    elif number%10 == 0:
        return(tnum[int(number/10)]+'십')
    else:
        return(tnum[int(number/10)]+'십'+' '+tnum[int(number%10)])

result = int(input("숫자를 입력하세요(두 자리까지만): "))
print(int_text(result))