
# # two pointers approach
# # Sum of pair :  17
# # Sorted arr=[1,2,5,7,8,10,56,78]


n = 17
arr = [1, 2, 5, 7, 8, 10, 56, 78]

i = 0
j = len(arr)-1
while j > i:

    if arr[i]+arr[j] == n:
        print(arr[i], arr[j])
        break

    if arr[i] + arr[j] > n:
        j -= 1
    if arr[i] + arr[j] < n:
        i += 1


# normal approach   2loops :
n1 = 17
arr1 = [1, 2, 5, 7, 8, 10, 56, 78]

for i in range(len(arr1)):
    for j in range(i, len(arr1)):
        if arr1[i]+arr1[j] == n1:
            print(arr1[i], arr1[j])
