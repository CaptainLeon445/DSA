def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(Index):
    if Index is not None:
        print("The target is at position ", Index)
    else:
        print ("Target not found")

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
result=binary_search(numbers, 15)
verify (result)

result=binary_search(numbers, 10)
verify (result)

