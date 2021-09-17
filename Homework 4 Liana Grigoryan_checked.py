"""LOOPS"""
import re
# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

# Սա բազմապատկման աղյուսակի խնդրի լուծումն է՞
for i in range(1, 10):
    for j in range(1, 10):
        print('{:>2} * {} = {:>2}'.format(i, j, i**j), end='\t')
    print()

# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։
nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'

nonsense = "Mary had a little lamb"
len(re.findall("b", nonsense))  # regular expression-ներ չենք անցել, կարող ե՞ք ցիկլերով հաշվել տառերի քանակը :)



# 5. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print(" Factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

# TODO: Վատ չէ, բայց կոդի ֆորմատավորմանն ուշադրություն դարձրեք միշտ։ Բացատները մի մոռացեք օպերատորների շուրջ ու արգումենտների
# TODO: ստորակետներից հետո