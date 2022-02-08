def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1, i, -1):
            if my_list[j] < my_list[j-1]:
                temp = my_list[j]
                my_list[j] = my_list[j-1]
                my_list[j-1] = temp
    return my_list

print(bubble_sort([4,2,6,5,1,3,9,22,37,0,-2]))