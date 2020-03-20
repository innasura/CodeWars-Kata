# https://www.codewars.com/kata/546e2562b03326a88e000020/python
# In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out

def square_digits(num):
    txt=''
    for i in str(num):
        txt = txt + (str((int(i) * int(i))))
    return(int(txt))

print(square_digits(9119))

#-------------- Best Practice ---------------------

def square_digits2(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

print(square_digits2(9119))

#-------------- Best Practice ---------------------

square_digits3 = lambda num: int(''.join(str(int(d)**2) for d in str(num)))

print(square_digits3(9119))