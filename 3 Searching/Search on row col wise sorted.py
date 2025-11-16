  row=0
        col=len(arr[0])-1
        while(row<len(arr) and col>=0):
            if(arr[row][col]==target):
                return True
            elif(arr[row][col]<target):
                row+=1
            else:
                col-=1
        return False