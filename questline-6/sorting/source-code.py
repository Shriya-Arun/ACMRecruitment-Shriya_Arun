lst=[5, 2, 9, 1, 5, 6]
def bubble_sort(lst):
    n = len(lst)
    for i in range(n): #outer loop for iterate through the entire list
        for j in range(0, n - i - 1): #inner loop to compare adjacent pair of elements
            if lst[j] > lst[j + 1]:   #checking whether the current element is greater than the next one
                 lst[j], lst[j + 1] = lst[j + 1], lst[j] #if so, swap the elements 
    return lst  #return the sorted list
print("Sorted list:",bubble_sort(lst))

