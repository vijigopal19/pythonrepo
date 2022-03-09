# program to remove special characters from list elements
lst1 = ["hello", "how1", "are", "you23"]
print(lst1)
lst2 = []
for word in lst1:
    ref = ""
    for chara in word:
        if chara.isalpha():
            ref = ref + chara
    print(ref)
    lst2.append(ref)
print(lst2)
