
class LZ78_tag:
    def __init__(self ,index, char):
        self.index = index
        self.char = char


    def gitindex(self):
        return self.index

    def gitchar(self):
        return self.char

def LZ78_find(list,symbol):
    le = len(list)
    for i in range(0,le):
        if list[i] == symbol:
            return i;
    return -1;

def LZ78_compress(lis):
    le = len(lis)
    search = []
    search.append(-1)
    tags = []
    best_offeset = 0
    best_length = 0
    # for i in range(0,le):
    i = 0
    while i < le:
        find = LZ78_find(search, lis[i])
        if  find == -1:
            search.append(lis[i])
            tags.append(LZ78_tag(0,lis[i]))
            i = i + 1
            continue

        if find != -1:
            s = lis[i]
            best_offeset = find
            best_length = 1
            c = True
            x=i+1
            if x == le:
                tags.append(LZ78_tag(0,lis[i]))
            while c and x < le:
                s = s + lis[x]
                z = LZ78_find(search,s)
                x = x + 1
                if z == -1:
                    search.append(s)
                    tags.append(LZ78_tag(best_offeset,lis[x-1]))
                    best_length = len(s)
                    c = False
                elif z != -1:
                    best_offeset = z;

        i = i + best_length



    return tags

def printLZ_78(LIST):
    le = len(LIST)
    print(">>> LZ 78 (Compression):")
    for i in range(0, le):
        print("<",end="")
        print(LIST[i].gitindex(), end=",\"")
        print(LIST[i].gitchar(),end="\"")
        print(">")

def main():

    #         0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21
    data78 = ['A','B','A','A','B','A','B','A','A','B','A','B','B','B','B','B','B','B','B','B','B','A']
    # ---------------------------------
    co = LZ78_compress(data78)
    printLZ_78(co)


if __name__ == "__main__":
    main()

