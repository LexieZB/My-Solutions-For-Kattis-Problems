def judge_distance(x, y, p, q):
    dis = ((x - p) ** 2 + (y - q) ** 2) ** (1 / 2)
    meter_dis = dis / 1000
    if meter_dis <= 1:
        return True
    else:
        return False


temp = list(map(int, input().split()))
P = temp[0]
N = temp[1]
pings = []
for i in range(N):
    temp = list(map(int, input().split()))
    pings.append(temp)
pings.sort(key=lambda l: l[3])
select = []
result = []
for i in range(len(pings) - 1):
    for j in range(i + 1, len(pings)):
        if pings[j][0] != pings[i][0] and abs(pings[j][3] - pings[i][3]) <= 10:#就是这里下标的问题
            select.append([pings[i], pings[j]])
        else:
            break
for i in select:
    if judge_distance(i[0][1], i[0][2], i[1][1], i[1][2]):
        result.append(i)
L = len(result)
final = set()
for i in range(L):
    final.add(tuple((result[i][0][0], result[i][1][0])))
out = list(final)
out.sort()

cross = []
for i in out:
    if i not in cross and (i[1], i[0]) not in cross:
        cross.append(i)
end = []
for i in cross:
    if i[0]>i[1]:
        end.append([i[1],i[0]])
    else:
        end.append([i[0],i[1]])
end.sort()
print(len(end))
for i in end:
    print(i[0],i[1])
