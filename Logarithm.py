# How to calculate Logarithm of any numbers in any bases :
# Rather than other slow algorithms to calculate Log(num, base)
# This code is really fast. This code does not use Taylor Series but some simple 
# functions.

def domain_check(num, base):

    '''
    Throwing an error if : num<=0
    Throwing an error if : base<=0 or base=1
    '''
    
    if num<=0 or base<=0 or base==1:

        raise Exception("Not in Domain...")
        exit()


def be_greater_than_one(num):

    '''
    num is nonzero and positive.

    This function will inverse the number if it is less
    than one. Otherwise, it does not do anything.

    This function also return the second arguman {-1, +1}. "-1"
    means the number was less than one and "+1" means it was 
    greater than one.

    be_greater_than_one(2.23) = 2.23, +1
    be_greater_than_one(0.2) = 5, -1
    '''
    
    if num < 1.0 :
        num = 1/num
        return (num, -1)
    return (num, 1)


def normalize(num):
    
    '''
    num is equal or greater than 1.

    This function will convert the number to the scientific
    form(coeff*(10)^b) and return coeff.
    
    normalize(123) = 1.23
    normalize(1234.56) = 1.23456
    normalize(1.0) = 1.0
    normalize(12) = 1.2
    '''
    
    # Convert the number to a list 
    num_list = list(str(num))
    # Remove '.'
    if '.' in num_list : num_list.remove('.')
    # Insert '.' at index 1
    num_list.insert(1, '.')
    # List to string
    num_str = ''.join(num_list)
    # Return the float version of the normalized number
    return float(num_str)


def digit_counter(num):

    '''
    num is equal or greater than 1.

    This function return the number of digits for both 
    integer and float numbers. By simply considering our 
    number as a string and splitting that over "." the number 
    of digits is counted.

    digit_counter(1234) = 4
    digit_counter(12.34) = 2

    '''

    return len(str(num).split('.')[0])

def list_to_float(lst):

    '''
    Simply convert a list with integer elements to a float number

    list_to_float([1,2,3,4,5,6]) = 1.23456
    '''

    sum = 0

    for i in range(len(lst)):
        sum += lst[i] * (10**-i)
        
    return sum


def log_ten(num, accuracy = 12):
    '''
    Return Logarithm(num, 10)
    Accuracy : number of iterations
    '''

    log_result = []
    # Make sure that we will use the greater_than_one version of
    # our number. We also use variable "sign" when reporting the
    # result
    num, sign = be_greater_than_one(num)

    for _ in range(accuracy+1):

         number_of_digits_minus_one = digit_counter(num) - 1

         log_result.append(number_of_digits_minus_one)

         num = normalize(num)

         num = num**10
    
    logTen = list_to_float(log_result)
    
    # LOG(A, B) = - LOG(1/A, B)
    return sign * logTen

def log(num, base=10, accuracy=12):
    
    # Domain Check
    domain_check(num, base)
    
    #LOG(A,B) = LOG(A,10) / LOG(B,10)
    return log_ten(num, accuracy) / log_ten(base, accuracy)

# Let's try
'''
print(log(43)) 
print(log(0.356))
print(log(1.0))
print(log(123456789101112))
print(log(17,3))
print(log(0.2,0.3))
print(log(0.3, 0.2))
print(log(0.4,1.1))
print(log(0.20, 0.998))
''' 
