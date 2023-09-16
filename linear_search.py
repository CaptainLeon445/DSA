
def linear_search(list, target):
    test = [i for i in range(0, len(list)) if list[i] == target]
    # for i in range(0, len(list)):
    #     if list[i] == target:
    #         return i
    if test == []:
        return None
    return test[0]

def verify(Index):
    if Index is not None:
        print("The target is at position ", Index)
    else:
        print ("Target not found")

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
result=linear_search(numbers, 15)
verify (result)

result=linear_search(numbers, 10)
verify (result)
