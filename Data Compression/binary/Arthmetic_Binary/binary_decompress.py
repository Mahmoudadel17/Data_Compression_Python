from collections import Counter


def getRanges(prob):
    keys = list(prob.keys())
    values = list(prob.values())
    ranges = dict()
    for i in range(len(prob)):
        if i == 0:
            ranges.update({"L" + keys[i]: 0})
            ranges.update({"U" + keys[i]: values[i]})
        else:
            ranges.update({"L" + keys[i]: ranges["U" + keys[i - 1]]})
            ranges.update({"U" + keys[i]: round(ranges["U" + keys[i - 1]] + values[i], 2)})
    return ranges


def probabilty(inp):
    prob = Counter(inp)
    for i in prob:
        prob[i] = round(int(prob[i]) / len(inp), 2)
    return prob


def scaling(l, u):
    if l < 0.5 and u < 0.5:
        l = round(l * 2, 4)
        u = round(u * 2, 4)
        num = 0
    else:
        l = round((l - 0.5) * 2, 4)
        u = round((u - 0.5) * 2, 4)
        num = 1

    return l, u, num


inputFile = open("decompress.txt", 'r')
data = inputFile.read()

inp = data
prob = {'a': 0.5, 'b': 0.33, 'c': 0.17}
ranges = getRanges(prob)

prob = dict(sorted(prob.items(), key=lambda x: x[1]))

k = 0
while (True):
    if 1 / (pow(2, k)) < list(prob.values())[0]:
        break
    k += 1

u = 1
l = 0
code = 0
decomp = []
x = 0
for i in range(len(inp)):
    inp = inp[x::]
    x = 0

    if len(inp) == k and int(inp[:k], 2) / pow(2, k) == 0.5:

        code = ((int(inp[:k], 2) / pow(2, k)) - l) / (u - l)
        for j in range(0, len(ranges.values()) - 1, 2):
            if code >= list(ranges.values())[j] and code <= list(ranges.values())[j + 1]:
                decomp.append(list(ranges.keys())[j][1:])
                break
        break

    code = ((int(inp[:k], 2) / pow(2, k)) - l) / (u - l)
    g = int(inp[:k], 2) / pow(2, k)
    z = inp[:k]
    for j in range(0, len(ranges.values()) - 1, 2):
        if code >= list(ranges.values())[j] and code <= list(ranges.values())[j + 1]:
            decomp.append(list(ranges.keys())[j][1:])
            break

    c = ranges["L" + decomp[i]]
    b = ranges["U" + decomp[i]]
    tempL = round(l + (u - l) * ranges["L" + decomp[i]], 4)
    tempU = round(l + (u - l) * ranges["U" + decomp[i]], 4)
    l = tempL
    u = tempU

    while (l > 0.5 and u > 0.5) or (l < 0.5 and u < 0.5):
        l, u, num = scaling(l, u)
        x += 1

print("DeCompressed text :- " + ''.join(decomp))