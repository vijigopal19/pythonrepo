# lst = ['hello', 'how@@', 'b!it', 'money']
lst = []
inp = ""
while inp != 'e':
    inp = input("Enter words. Type e to quit :")
    lst.append(inp)
# remove the e at the end
lst.pop()
print(lst)
nlist = [words for words in lst if words.isalpha()]
print(nlist)

# extract mixed words
nlist = []
for words in lst:
    if not words.isalpha():
        nlist.append(words)
print(nlist)
