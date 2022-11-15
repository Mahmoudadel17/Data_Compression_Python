import filecmp

def find(data,elem):
    n = len(data)
    for i in range(0,n):
        if data[i] == elem:
            return i

    return -1

def LZW_compress(data):
    n = len(data)
    list = []
    compress = []
    i = 0
    while i < n:
        length = 1
        str = data[i]
        best_index = ord(str)
        while i+length < n and find(list,str + data[i+length]) != -1:
            best_index = find(list,str + data[i+length]) + 128
            str = str + data[i+length]
            length  = length + 1
        if i+length < n:
            str = str + data[i + length]
            list.append(str)
        compress.append(best_index)
        i = i + length
    return compress

def print_LZW(da):
    n = len(da)
    for i in range(0,n):
        print(da[i])


def DeCompress_LZW(data):
    n = len(data)
    list = []
    now = ""
    str = ""
    for i in range(0,n):
        c = True
        num = data[i]
        if num < 128:
            str += chr(num)
            now = chr(num)
        else:
            check = len(list)
            if num - 128 < check:
                now = list[num - 128]
                str += now
            else:
                c = False

        if i != 0:
            num0 = data[i-1]
            if c:
                if num0 < 128:
                 list.append(chr(num0)+now[0])
                else:
                    list.append(list[num0 - 128] + now[0])
            else:
                if num0 < 128:
                    list.append(chr(num0)+chr(num0))
                    str += chr(num0)+chr(num0)
                else:
                    s = list[num0 - 128]
                    list.append(s+s[0])
                    str+=s+s[0]

    return str


def main():
    f = open("inn.txt", "r")
    Data = f.read()
    comp = LZW_compress(Data)
    with open('out_compress.txt', 'w') as file:
        file.write(''.join(str(comp)))
    # print_LZW(comp)
    st = DeCompress_LZW(comp)
    with open('out_decompress.txt', 'w') as file:
        file.write(''.join(str(st)))
    # print(st)


if __name__ == "__main__":
    main()
