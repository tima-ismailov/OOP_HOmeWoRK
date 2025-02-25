lst = [1,2,3,4,5,6,7,8,9,10]


def find_element(lst,target):
    for i in lst:
        if i == target:
            return True
    return False

print(find_element(lst,10))


lst3 = [12, 34, 53, 532,11, 4,]

def bubble_sort(lst):
   n = len(lst)
   for i in range(n):
       for j in range(n - i - 1):
          if lst[j] > lst[j + 1]: #Усли текущий элемент больше следующего то мы будем его менять местами
             lst[j], lst[j + 1] = lst[j + 1], lst[j] #Меняем элементы местами
bubble_sort(lst=lst3)
print(lst3)


