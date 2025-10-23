# Richest Customer Wealth Leetcode : 1672
def my_function(accounts):
    max=0
    sum=0
    for i in range(len(accounts)):
        for j in range(len(accounts[i])):
            sum+=accounts[i][j]
        if(sum>max):
            max=sum
        sum=0
    return max
arr=[[1,2,3],[3,2,1],[4,5]]
result=my_function(arr)
print(result)