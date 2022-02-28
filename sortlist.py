list1 = [4, 3, 2, 5]
list2 = [0, 5, 1, 8, 9]
new = list1 + list2
new.sort()
print(new)

res = []
[res.append(x) for x in new if x not in res]

# printing list after removal 
print("The list after removing duplicates : " + str(res))
