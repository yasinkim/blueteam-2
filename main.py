
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_index=[]
odd_index=[]

for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        even_index.append(my_list[i])
    else:    
        odd_index.append(my_list[i])
    
print(even_index)
print(odd_index)
