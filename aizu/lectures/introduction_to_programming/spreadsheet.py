#! python3
# spreadsheet.py

r, c = [int(x) for x in input().split(' ')]

sheet = [[int(x) for x in input().split(' ')] for i in range(r)]
for i in range(r):
    sheet[i].append(0)
sheet.append([0 for i in range(c+1)])

for i in range(r):
    for j in range(c):
        sheet[i][c] += sheet[i][j]
        sheet[r][j] += sheet[i][j]
        sheet[r][c] += sheet[i][j]

for i in range(r+1):
    print(' '.join([str(x) for x in sheet[i]]))
