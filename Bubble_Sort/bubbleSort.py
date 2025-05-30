arrIO=[9,4,6,1,3,2,8,7,5]

def bubbleSort(arr: list):
    swapflag=False
    j=len(arr)-1
    while(j>0):
        swapflag=False  # turn back the swap flag to false after each and every pass if swapped happpen in that pass.
        for i in range(0,j,1): # loop to check whether the element is greater than next if yes then swap
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                swapflag=True 
                #print(arr)
            else:
                continue
            # if no element found in pass which needed swap then break the sorting directly.
        if swapflag==True: 
            j-=1
        else: 
            break

bubbleSort(arr=arrIO)
print(arrIO)
