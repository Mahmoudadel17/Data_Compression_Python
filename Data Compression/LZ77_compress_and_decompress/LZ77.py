class tag:
    def __init__(self,offset, length, char):
        self.offset = offset
        self.length = length
        self.char = char
    def gitOffset(self):
        return self.offset

    def gitlength(self):
        return self.length

    def gitchar(self):
        return self.char




def LZ77_Search(search, look_ahead):
    ls = len(search)
    # llh = len(look_ahead)

    if (ls == 0):
        return (0, 0, look_ahead[0])


    best_length = 0
    best_offset = 0
    buf = search + look_ahead
    x = False
    search_pointer = ls

    for i in range(0, ls):
        length = 0
        while buf[i + length] == buf[search_pointer + length]:
            length = length + 1
            x = True

            if search_pointer + length == len(buf):
                length = length - 1
                break
            if i + length >= search_pointer:
                break

        #  check if found the best new index in search window
        if length == best_length:
            best_offset = i

        #  check if found the best length in search window
        if length > best_length:
            best_offset = i
            best_length = length
    # ------------------------------------------------
    if x:
        return (ls - best_offset, best_length, buf[search_pointer + best_length])
    else:
        return (best_offset, best_length, buf[search_pointer + best_length])

def LZ77_compress(lis,maxS,maxLH):
    print(">>> LZ 77 (Compression):")
    searchiterator = 0;
    lhiterator = 0;
    list = []
    while lhiterator < len(lis):
        search = lis[searchiterator:lhiterator]
        look_ahead = lis[lhiterator:lhiterator + maxLH]
        (offset, length, char) = LZ77_Search(search, look_ahead)
        print("<",end="")
        print(offset, end=",")
        print(length, end=",\"")
        print(char, end="\"")
        print(">")
        list.append(tag(offset,length,char))
        # print(offset, length, char)

        lhiterator = lhiterator + length + 1
        searchiterator = lhiterator - maxS

        if searchiterator < 0:
            searchiterator = 0
    return list

def LZ77_decompress(list):
    print(">>> DeLZ 77 (Compression):")
    size = len(list)
    arr = []
    it = 0
    for i in range(0,size):
        if list[i].gitOffset() == 0:
            arr.append(list[i].gitchar())
            it = it +1
            continue

        for j in range(0,list[i].gitlength()):
            a = list[i].gitOffset()
            # print(it,end=" ")
            # print( a ,end=" ")
            arr.append(arr[it - a])
            it = it +1
        #     arr.append(list[it - a].gitchar())
        #     it=+1
        arr.append(list[i].gitchar())
        it = it +1


    x = len(arr)
    for i in range(0, x):
        print(arr[i],end=" ")
    print("")



def main():

    MAXSEARCH = 12
    MAXLH = 11
    #         0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21
    data77 = ['A','B','A','A','B','A','B','A','A','B','B','B','B','B','B','B','B','B','B','B','B','A']
    # ------------------------------------------------------------------------------------------------

    listt = LZ77_compress(data77,MAXSEARCH,MAXLH)
    # ---------------------------------
    LZ77_decompress(listt)
    # ---------------------------------


if __name__ == "__main__":
    main()