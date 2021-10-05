"""RECURSION"""
import math
# 1. Write a recursive function to calculate the sum of reciprocals of powers of 2. Try increasing the n and see the
# magic.
# Գրել ռեկուրսիվ ֆունկցիա, որը կհաշվի երկրաչափական գումարը, որտեղ r = 1 / 2 է։ Փորձեք բացրձրացնել n-ի արժեքը հետաքրքիր
# արդյունք ստանալու համար։
#Պահանջը չեմ հասակցել

# 2. Write a recursive function to calculate n-th power of a.
# Գրել ֆունկցիա, որը ռեկուրսիվ կերպով կհաշվի a-ի n աստիճանը։
'''def power(n, a):

    return (a ** n)
print(power(3, 2))'''



# 3. Write a recursive function that evaluates a mathematical expression. Example input - "5 + 6"
# Գրել ռեկուրսիվ ֆունկցիա, որը կհաշվի մաթեմատիկական արտահայտություն փոխանցված սթրինգի միջոցով։ Օրինակ՝ "5 + 6"
'''def  express (a, b):
    return (a + b)
express = (input("Enter : "))
print(5 + 6)'''
# 4. Write a recursive function that reverses a string
# Գրել ֆունկցիա, որը ռեկուրսիվ կերպով կշրջի և կվերադարձնի փոխանցված սթրինգը։
'''def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string : "))
print(reverse(a))'''



# 5. Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved
# to the end of the string.
# Գրել ռեկուրսիվ ֆունկցիա, որը որպես արգումենտ կվերցնի սթրինգ և կվերադարձնի նոր սթրինգ, որտեղ օրիգինալ սթրինգում գտնվող
# բոլոր x-երը տեղափոխվել են սթրինգի ամենավերջը։

"""OLD STUFF"""

# 6. Write a function that sorts a list in ascending. Additionally, the function may take a keyword argument that will
# reverse the sort (without recursion is fine).
# Գրել ֆունկցիա, որը կսորտավորի դրան փոխանցված լիստը աճման կարգով։ Կարելի է ֆունկցիային նաև ավելացնել kwarg, որը փոփոխելիս
# կկարողանանք լիստը սորտավորել նաև նվազման կարգով։


 #def lst_1 ('b', 'c', 'd', 'w'):
  #   return len(lst_1)
  #  lst_1.sort()

#print(lst_1(5,2,6,3))

# 7. Write a function that will take 4 arguments. First two are tuples and represent 2D coordinates of two circles.
# The others are the radii of our circles. The function must tell us whether one of the circles is inside the other, or
# do circles intersect, or are they far apart.
# Գրել ֆունկցիա, որը կվերցնի 4 արգումենտ։ Առաջին երկուսը tuple են, որոնք իրենցից ներկայացնելու են 2-չափ տարածության մեջ
# շրջանագծերի կենտրոնների կոորդինատներ։ Մյուս երկուսը լինելու են integer տիպի և ներկայացնելու են վերոնշյալ շրջանագծերի
# շառավիղները։ Ֆունկցիան պետք է տպի արդյո՞ք օղակները հատվում են, կամ մեկը մյուսի մեջ է, կամ իրարից հեռու են։

"""OPTIONAL"""

# 8. Write a program to combine two dictionaries adding values for common keys.
# Գրել ծրագիր, որը կմիացնի երկու dictionary։ Համընկնող բանալիների արժեքները պետք է գումարվեն։
'''dict_1 = {'x': 2, 'b': 3, 'c': 5}
dict_2 = {'x': 4, 'l': 7, 'd': 6}


dict_3 = {}

for i, j in dict_1.items():

    for x, y in dict_2.items():

        if i == x:

            dict_3[i] = (j+y)

print(dict_3)'''



# 9. Write a program to create a dictionary from a string. The letters are the keys and the values are the counts of
# the corresponding letters.
# Սթրինգից ստեղծել dictionary: Սթրինգի տառերը հանդես են գալու որպես բանալիներ, իսկ սթրինգում դրանց քանակը որպես արժեքներ