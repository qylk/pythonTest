__author__ = 'qylk'

data = ['name', 23, (2018, 2, 3)]

name, age, date = data
print name
print age
print date

name, age, (year, month, day) = data
print name
print age
print year

# ignore one
_, _, date = data
print date

# ignore some
# *ignore, date = data
# print date
