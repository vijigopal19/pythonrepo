inp = input("Enter the string to reverse :")
rev = ""
wordlist = list(inp)
print(wordlist)

while len(wordlist) > 0:
    last = wordlist.pop()
    rev = rev + last
print(rev)

"""
# Method 1
txt = "Hello World" [::-1]
print(txt)
"""

"""
# method 2
def reverse(str1):
    rev = ""
    for i in str1:
        rev = i + rev
    return rev

inp = input("Enter your input: ")
print(inp)
print(f"reverse is", reverse(inp))
"""
"""
# reverse using slice
inp = input("Enter your input: ")
print(inp)
slic = inp[::-1]
print(slic)
"""
