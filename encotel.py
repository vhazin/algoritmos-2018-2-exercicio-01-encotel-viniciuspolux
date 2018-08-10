nums = ''
texto = (input('Digite o texto: ')).upper()

for i in texto:
    if i == 'A' or i == 'B' or i == 'C':
        nums = nums + '2'
    elif i == 'D' or i == 'E' or i == 'F':
        nums = nums + '3'
    elif i == 'G' or i == 'H' or i == 'I':
        nums = nums + '4'
    elif i == 'J' or i == 'K' or i == 'L':
        nums = nums + '5'
    elif i == 'M' or i == 'N' or i == 'O':
        nums = nums + '6'
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        nums = nums + '7'
    elif i == 'T' or i == 'U' or i == 'V':
        nums = nums + '8'
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        nums = nums + '9'
    else:
        nums = nums + i

print(nums)
