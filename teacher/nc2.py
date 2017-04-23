tnum = {0:'영', 1:'일', 2:'이', 3:'삼', 4:'사', 5:'오', 6:'육', 7:'칠', 8:'팔', 9:'구'}
for i in range(1,10):
    number = 9 * i
    if number < 10:
        result = tnum[number]
    else:
        result = tnum[int(number/10)]+'십'+' '+tnum[int(number%10)]
    print("구 x %s = %s" %(tnum[i], result))