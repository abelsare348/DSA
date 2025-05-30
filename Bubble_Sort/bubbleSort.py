arrIO=[9,4,6,1,3,2,8,7,5]

def bubbleSort(arr: list):
    swapflag=False
    j=len(arr)-1
    while(j>0):
        for i in range(0,j,1):
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                swapflag=True
                print(arr)
            else:
                continue
        if swapflag==True:
            j-=1
        else:
            break

bubbleSort(arr=arrIO)
