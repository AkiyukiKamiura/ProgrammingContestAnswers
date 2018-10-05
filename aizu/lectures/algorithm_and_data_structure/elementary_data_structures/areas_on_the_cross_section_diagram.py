#! python3
# areas_on_the_cross_section_diagram.py

cross_section = input()

stack = []
areas_stack = []
area = 0
for i in range(len(cross_section)):
    c = cross_section[i]
    if c == '\\':
        stack.append(i)
    elif c == '/' and len(stack) != 0:
        j = stack.pop()
        a = i - j
        area += a
        while len(areas_stack) != 0 and areas_stack[-1][0] > j:
            a += areas_stack.pop()[1]
        areas_stack.append([j, a])

print(area)
if area == 0:
    print(0)
else:
    print(len(areas_stack), ' '.join([str(x[1]) for x in areas_stack]))
