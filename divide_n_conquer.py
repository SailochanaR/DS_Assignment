def merge_sort(arr):
    # overflow
    if len(arr) <= 1:
        return arr
    mid = len( arr) // 2
    # Split the list into two halves
    left = arr[:mid]
    right =arr[mid:]
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    sorted_nums =  merge(left_sorted, right_sorted)
    
    return sorted_nums
def merge(num1, num2):     
    sol= []
    i, j = 0, 0
    while i < len(num1) and j < len(num2):        
        if num1[i] <= num2[j]:
            sol.append(num1[i])
            i += 1 
        else:
            sol.append(num2[j])
            j += 1
    num1_tail = num1[i:]
    num2_tail = num2[j:]
    return sol + num1_tail + num2_tail
if __name__=='__main__':
    Ele=[]
    size=int(input())
    i=0
    for i in range(size+1):
        Ele.append(int(input()))
merge_sort(Ele)
