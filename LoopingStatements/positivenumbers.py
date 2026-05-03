numbers = [-5,-4,-3,-2,-1,0,1,2,3,4,5,]
positive_numbers_count = 0

for num in numbers:
    if num > 0:
        positive_numbers_count += 1

print("Final count is",positive_numbers_count)