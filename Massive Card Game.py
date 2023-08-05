def find_first_bigger(ls, begin, end, x):
    if ls[begin] >= x:
        return begin
    elif ls[end] < x:
        return -1
    elif begin == end:
        return begin
    else:
        mid = (begin + end) // 2
        if ls[mid] < x:
            return find_first_bigger(ls, mid + 1, end, x)
        elif ls[mid] >= x and ls[mid - 1] < x:
            return mid
        else:
            return find_first_bigger(ls, begin, mid - 1, x)


def find_last_smaller(ls, begin, end, x):
    if ls[end] <= x:
        return end
    elif ls[begin] > x:
        return -1
    elif begin == end:
        return begin
    else:
        mid = (begin + end) // 2
        if ls[mid] > x:
            return find_last_smaller(ls, begin, mid - 1, x)
        elif ls[mid] <= x and ls[mid + 1] > x:
            return mid
        else:
            return find_last_smaller(ls, mid + 1, end, x)


N = int(input())
cards = list(map(int, input().split()))  # input().split()得到的就已经是list了，是['1', '2', '3', '4']这样子的
Q = int(input())
ranges = []
for i in range(Q):
    temp = list(map(int, input().split()))
    ranges.append([temp[0],temp[1]])
result = []
cards.sort()

for i in ranges:
    if i[0] == i[1] and i[0] not in cards:
        result.append(0)
    elif i[1] < cards[0]:
        result.append(0)
    elif i[0] > cards[len(cards) - 1]:
        result.append(0)
    elif cards[0]>=i[0] and cards[N-1]<=i[1]:
        result.append(Q)
    else:
        pos1 = find_first_bigger(cards, 0, N - 1, i[0])
        pos2 = find_last_smaller(cards, 0, N - 1, i[1])
        if pos1 == -1 or pos2 == -1:
            result.append(0)
        else:
            result.append(pos2 - pos1 + 1)
for i in range(len(result)):
    print(result[i])
