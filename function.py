def calculate_average(num):
    if len(num)==0:
        return 0
    return sum(num)/len(num)
print(calculate_average([5, 10, 15, 20]))
print(calculate_average([]))  
