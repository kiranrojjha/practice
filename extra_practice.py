# def is_leap(year):
#     leap = False
#     if year % 400 == 0:
#         leap= True                   #leap year
#     elif year % 100 == 0:
#         leap =  False
#     elif year % 4 == 0:
#         leap =  True
#     else:
#         leap =  False

    
#     return leap

# year = int(input())

def solve():
    s = input()
    words = s.split(' ')
    result = []

    for word in words:
        if word:
            first = word[0].upper() if word[0].isalpha() else word[0]
            rest = word[1:]
            result.append(first + rest)
        else:
            result.append('')
    
    print(' '.join(result))

solve()

