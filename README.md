# logarithm
How to calculate logarithm from scratch without using Taylor Series

### Dependencies
python3

### What's the Idea?
From math we all know following logarithm-related equations:

#### 1- To get the number of digits of numbers, we can simply calculate floor of the 1 added to the **10-based logarithm** of that number.

*number_of_digits(num) = [1 + logarithm(num, 10)]*

#### 2- If **base** were not equal to 10, we can use the following equation:

*logarithm(num, base) = logarithm(num, 10) / logarithm(base, 10)*

#### 3- In the case of less-than-one-numbers:

*logarithm(num, base) = - logarith(1/num, base)*

Combining these equations, we calculate the logarithm(num, base) without using python libraries ot Taylor Series.

### Algorithm to calculate 10-based logarithm

This algorithm has following steps:
###### Step 0
Replace **num** with **1/num** if **num** were less than one
###### Step 1
Store (number_of_digits(**num**) - 1)
###### Step 2
Convert **num** to its scientific form(**coeff** * 10^b)
###### Step 3
Replace **num** with **coeff**
###### Step 4
Replace **num** with **num^10**
###### Step 5
Go to Step 1

### Running Algorithm on **num = 17**
Step 0 : num = 17
\
\
First Iteration : 
Step 1 : Store 2-1=**1**  ,  Step 2 : 17=1.7 * 10^1  ,  Step 3 : num=1.7  ,  Step 4 : num=201.59
\
\
Second Iteration :
Step 1 : Store 3-1=**2**  ,  Step 2 : 201.59=2.0159 * 10^2  ,  Step 3 : num=2.0159  ,  Step 4 : num=1108.38
\
\
Third Iteration :
Step 1 : Store 4-1=**3**  ,  Step 2 : 1108.38=1.10838 * 10^3  ,  Step 3 : num=1.10838  ,  Step 4 : num=2.79
\
\
Forth Iteration :
Step 1 : Store 1-1=**0**  ,  Step 2 : 2.79=2.79 * 10^0  ,  Step 3 : num=2.79  ,  Step 4 : num=28578.67
\
\
Fifth Iteration :
Step 1 : Store 5-1=**4**    ...
\
\
Storage = [1, 2, 3 ,0 ,4] and Logarithm(17, 10) = 1.2304

As the number of iteration increases, result will be more accurate.

### Algorithm to calculate non-10-based logarithm

Simply use following equation:\
\
*logarithm(num, base) = logarithm(num, 10) / logarithm(base, 10)*

### How to use : 

Simply call the function log(num, base, accuracy)
\
accuracy : Int => number of iterations
