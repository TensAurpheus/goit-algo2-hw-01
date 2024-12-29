input = [2, 3, 0, 1, 4, 10, 7, 8, 2, 1, 5]  

def divide(arr, min = None, max = None):
    if min == None: min = arr[0]
    if max == None: max = arr[0]

    # print(min, max)

    if len(arr) == 1:
        return (min, max)
    
    if arr[0] < min:
        min = arr[0]
    elif arr[0] > max:
        max = arr[0]
    
    print(arr, min, max)

    return divide(arr[1:], min, max)

res = divide(input)
print(f'array: {input}')
print(f'Min: {res[0]}, Max: {res[1]}')    
