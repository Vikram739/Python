"""
    Created By : Vikram Markali
"""

test_cases = int(input())

for val in range(test_cases):
    size = int(input())
    ele = list(map(int,input().split()))
    res={}
    
    for i in range(len(ele)):
        
        if ele[i] not in res:
            res[ele[i]] = 1
        else:
            res[ele[i]]+=1
    r2 =[]
    for col,val in res.items():
        r2.append(val)
    max_val=max(r2)
    
    if r2.count(max_val)>1:
        print('NO')
    else:
        print('YES')