def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)
number=int(input("enter a value:"))
res=fact_rec(number)

print("the factorial of {} is {}.".format(number, res))
def isleapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
    return True 
  else:
      return False

year = int(input("enter a year : "))

if isleapYear(year):
     print(' {} is a leap year.'.format(year))
else:
    print('{} is not a leap year.'.format(year))