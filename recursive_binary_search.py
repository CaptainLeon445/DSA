def recursive_binary_search(list, target):
    if len(list) == 0:
        print ("Not found")
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            print("found it")
            return True 
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint-1], target)


def verify(Index):
    if Index is not None:
        print(Index)
    else:
        print ("Target not found")

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
result=recursive_binary_search(numbers, 15)
verify (result)

result=recursive_binary_search(numbers, 10)
verify (result)

