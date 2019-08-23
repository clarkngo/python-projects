def sum_of_three(arr):
    n = len(arr)
    for i in range(n - 2):
        sum = arr[i] + arr[i+1] + arr[i+2]
        print(sum)

sum_of_three([1,2,3,4,5,6])
