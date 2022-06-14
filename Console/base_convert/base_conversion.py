import sys
from string import ascii_lowercase
from random import randint

sys.setrecursionlimit(10**6)

def list_to_str(l):
    return "".join([str(x) for x in l])

def base10_to_N(number, base, l, i=0, n=0):
    while n < number:
        l.append(0) if i >= len(l) else None
        if l[i] < base - 1:
            l[i] += 1
            n += 1
        else:
            l[i] = 0
            return base10_to_N(number, base, l ,i + 1, n)
        i = 0
    l.reverse()
    return l

def baseN_to_10(number, base):
    sum = 0
    for digit in range(len(number)):
        number[digit] = inverted_dict[number[digit]] if isinstance(number[digit], str) else number[digit]
        sum += base ** len(number[digit + 1:]) * number[digit]
    return sum

def convert(input_base, output_base, number):
    number_array = []
    for i in list(number):
        number_array.append(i) if i in ascii_lowercase else number_array.append(int(i))
    base10 = baseN_to_10(number=number_array, base=input_base)

    baseN = base10_to_N(number=base10, base=output_base, l=[0])
    for j in range(len(baseN)):
        baseN[j] = letters_dict[baseN[j]] if baseN[j] >= 10 else baseN[j]
    return number, list_to_str(baseN), base10


letters_dict = {x + 10: ascii_lowercase[x] for x in range(len(ascii_lowercase))}
inverted_dict = {letters_dict[value]: value for value in letters_dict}

# input_base, output_base, number = 12, 2, "a1" #str(randint(0, 100))
# input_num, baseN, base10 = convert(input_base, output_base, number)
# result = f"base {input_base}: {input_num} \nbase {output_base}: {baseN} \nbase 10: {base10}"
#
# print(result)






