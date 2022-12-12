# class tag:
#     def __init__(self,offset, length, char):
#         self.offset = offset
#         self.length = length
#         self.char = char
#     def gitOffset(self):
#         return self.offset
#
#     def gitlength(self):
#         return self.length
#
#     def gitchar(self):
#         return self.char
#
#
#
#
# def LZ77_Search(search, look_ahead):
#     ls = len(search)
#     # llh = len(look_ahead)
#
#     if (ls == 0):
#         return (0, 0, look_ahead[0])
#
#
#     best_length = 0
#     best_offset = 0
#     buf = search + look_ahead
#     x = False
#     search_pointer = ls
#
#     for i in range(0, ls):
#         length = 0
#         while buf[i + length] == buf[search_pointer + length]:
#             length = length + 1
#             x = True
#
#             if search_pointer + length == len(buf):
#                 length = length - 1
#                 break
#             if i + length >= search_pointer:
#                 break
#
#         #  check if found the best new index in search window
#         if length == best_length:
#             best_offset = i
#
#         #  check if found the best length in search window
#         if length > best_length:
#             best_offset = i
#             best_length = length
#     # ------------------------------------------------
#     if x:
#         return (ls - best_offset, best_length, buf[search_pointer + best_length])
#     else:
#         return (best_offset, best_length, buf[search_pointer + best_length])
#
# def LZ77_compress(lis,maxS,maxLH):
#     print(">>> LZ 77 (Compression):")
#     searchiterator = 0;
#     lhiterator = 0;
#     list = []
#     while lhiterator < len(lis):
#         search = lis[searchiterator:lhiterator]
#         look_ahead = lis[lhiterator:lhiterator + maxLH]
#         (offset, length, char) = LZ77_Search(search, look_ahead)
#         print("<",end="")
#         print(offset, end=",")
#         print(length, end=",\"")
#         print(char, end="\"")
#         print(">")
#         list.append(tag(offset,length,char))
#         # print(offset, length, char)
#
#         lhiterator = lhiterator + length + 1
#         searchiterator = lhiterator - maxS
#
#         if searchiterator < 0:
#             searchiterator = 0
#     return list
#
# def LZ77_decompress(list):
#     print(">>> DeLZ 77 (Compression):")
#     size = len(list)
#     arr = []
#     it = 0
#     for i in range(0,size):
#         if list[i].gitOffset() == 0:
#             arr.append(list[i].gitchar())
#             it = it +1
#             continue
#
#         for j in range(0,list[i].gitlength()):
#             a = list[i].gitOffset()
#             # print(it,end=" ")
#             # print( a ,end=" ")
#             arr.append(arr[it - a])
#             it = it +1
#         #     arr.append(list[it - a].gitchar())
#         #     it=+1
#         arr.append(list[i].gitchar())
#         it = it +1
#
#
#     x = len(arr)
#     for i in range(0, x):
#         print(arr[i],end=" ")
#     print("")
#
#
#
# def main():
#
#     MAXSEARCH = 12
#     MAXLH = 11
#     #         0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21
#     data77 = ['A','B','A','A','B','A','B','A','A','B','B','B','B','B','B','B','B','B','B','B','B','A']
#     # ------------------------------------------------------------------------------------------------
#
#     listt = LZ77_compress(data77,MAXSEARCH,MAXLH)
#     # ---------------------------------
#     LZ77_decompress(listt)
#     # ---------------------------------
#
#
# if __name__ == "__main__":
#     main()



import string
import random
from collections import Counter
import time

# Arithmetic Encoding
def ac_encode(txt):

    res = Counter(txt)

    # characters
    chars = list(res.keys())

    # frequency of characters
    freq = list(res.values())

    probability = []
    for i in freq:
        probability.append(i / len(txt))

    print(chars)
    print(probability)

    high = 1.0
    low = 0.0
    for c in txt:
        diff = high - low
        index = chars.index(c)
        for i in range(index):
            high = low + diff * probability[i]
            low = high

        high = low + diff * probability[index]
        print(f'char {c} -> Low: {low}   High: {high}')

    tag = (low+high)/2.0

    print('Input: ' + txt)
    print(str(low) + '< codeword <' + str(high))
    print('codeword = ' + str(tag))

    with open('encode.ac', 'w') as fw:
        for i in chars:
            fw.write(i + ' ')
        fw.write('\n')

        for i in probability:
            fw.write(str(i) + ' ')
        fw.write('\n')

        fw.write(str(tag))

    return chars, probability, tag


# Arithmetic Decoding
def ac_decode(chars, probability, tag):
    high = 1.0
    low = 0.0
    output = ''
    c = ''
    while (c != '$'):
        diff = high - low
        for i in range(len(chars)):
            high = low + diff * probability[i]
            if low < tag < high:
                break
            else:
                low = high

        c = chars[i]
        output += c

    return output


def arithmetic_coding(input):
    if '$' in input:
        input = input[0:input.index('$')]
    if input[-1] != '$':
        input += '$'

    print('Input: ' + input)

    start = time.time()
    (chars, probability, tag) = ac_encode(input)
    output = ac_decode(chars, probability, tag)
    end = time.time()

    print('Decode: ' + output)

    print('does match :  ' + str(input == output))
    print(f"Total Time: {end - start} sec\n\n")
    return input == output


############# INPUT ######################
# Random String , 100 test case
count = 0
testcase = 10
for i in range(testcase):
    # generating string
    letters = string.ascii_uppercase
    random_txt = ''.join(random.choice(letters) for i in range(13)) + '$'
    flag = arithmetic_coding(random_txt)
    if flag:
        count += 1

print(f"Total Test: {testcase}")
print(f"Succecss: {count}")


#----------------------------------------
# User given specific data
# Please use small string (less than 13 characters)
txt = "BANGLADESH$"
arithmetic_coding(txt)


##########################################
