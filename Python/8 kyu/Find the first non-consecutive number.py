# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/solutions/python

def first_non_consecutive(arr):
    if not arr: return 0
    x = arr[0]
    for num in arr:
        if num != x: return num
        x += 1
    return None

print(first_non_consecutive([1,2,3,5,6,7,8]))

# -------------best practice-------------------

def first_non_consecutive2(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            return arr[i]

print(first_non_consecutive2([11,12,13,14,15,16,17,18,20]))

# -------------best practice-------------------

def first_non_consecutive3(a):
    for count, x in enumerate(a, a[0]):
        if count != x:
            return x

print(first_non_consecutive3([1,2,3,4,5,6,25]))

# -------------best practice-------------------

first_non_consecutive4=lambda arr: ([e for i,e in enumerate(arr[1:]) if e!=arr[i]+1])[0]

print(first_non_consecutive4([1,2,3,4,10,12,13,14,15]))

# -------------best practice-------------------

def first_non_consecutive5(arr):
    return next((j for i, j in zip(arr, arr[1:]) if i + 1 != j), None)

print(first_non_consecutive5([45,46,47,48,50,51,55,78,90,100]))

