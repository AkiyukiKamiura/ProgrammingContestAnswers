#! python3
# toggling_cases.py

x = input()

rst = ''
for c in x:
    if c.isupper():
        rst += c.lower()
    elif c.islower():
        rst += c.upper()
    else:
        rst += c

print(rst)
