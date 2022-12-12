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
#----------------------------------------------------------------

#Enter the text to compress
inputFile = open("compress.txt", 'r')
data = inputFile.read()
inp = data
prob = dict(probabilty(inp))
print("Prob :- ", prob)
# prob = {"A":0.8,"B":0.02,"C":0.18}
ranges = getRanges(prob)
prob = dict(sorted(prob.items(), key=lambda x: x[1]))

k = 0
while (True):
    if 1 / (pow(2, k)) < list(prob.values())[0]:
        break
    k += 1

u = 0
l = 0
comp = []
for i in range(len(inp)):
    if i == 0:
        l = ranges["L" + inp[i]]
        u = ranges["U" + inp[i]]
        continue

    tempL = round(l + (u - l) * ranges["L" + inp[i]], 4)
    tempU = round(l + (u - l) * ranges["U" + inp[i]], 4)
    l = tempL
    u = tempU

    while (l > 0.5 and u > 0.5) or (l < 0.5 and u < 0.5):
        l, u, num = scaling(l, u)
        comp.append(str(num))

    if i == len(inp) - 1:
        val = "1"
        for j in range(k - 1):
            val += "0"
        comp.append(val)

print("Compressed text :- " + ''.join(comp))
