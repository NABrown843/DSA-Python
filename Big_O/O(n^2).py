# O(n^2 + n) simplified to O(n^2)
# O(n^3) simplified to O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)


print_items(10)