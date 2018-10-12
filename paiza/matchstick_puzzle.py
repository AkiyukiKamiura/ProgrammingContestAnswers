#! python3
# coding: utf-8

# TODO: やり直し

add_to = {'0': ['8'], '1': ['7'], '2': [], '3': ['9'], '4': [], '5': ['6', '9'], '6': ['8'], '7': [], '8': [], '9': ['8']}
minus_to = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': ['5'], '7': ['1'], '8': ['0', '6', '9'], '9': ['3']}
move_self = {'0': ['6', '9'], '1': [], '2': ['3'], '3': ['2', '5'], '4': [], '5': ['3'], '6': ['0', '9'], '7': [], '8': [], '9': ['0', '6']}

s = input()

ans = []
for i in range(len(s)):
    if move_self[s[i]] != 0:
        for c in move_self[s[i]]:
            new_s = s[:i] + c + s[i+1:]
            ans.append(new_s)

    for c_ad in add_to[s[i]]:
        for j in range(len(s)):
            if i == j: continue
            for c_mi in minus_to[s[j]]:
                new_s = s[:i] + c_ad + s[i+1:]
                new_s = new_s[:j] + c_mi + new_s[j+1:]
                ans.append(new_s)


if len(ans) == 0:
    print('none')
else:
    for a in sorted(ans):
        print(a)
