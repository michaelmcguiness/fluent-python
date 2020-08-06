"""List Comprehension: Page 23"""

# List Comprehension and Readability
symbols = '#$%@!'
codes = [ord(symbol) for symbol in symbols]
print(codes) # [35, 36, 37, 64, 33]

# Listcomps vs. map and filter
beyond_ascii  = [ord(s) for s in symbols if ord(s) > 60]
print(beyond_ascii) # [64]
beyond_ascii = list(filter(lambda c: c > 60, map(ord, symbols)))
print(beyond_ascii) # [64]

# Cartesian Products
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for size in sizes
                         for color in colors]
print(tshirts)
# [('black', 'S'), ('white', 'S'), ('black', 'M'), 
# ('white', 'M'), ('black', 'L'), ('white', 'L')]

"""Generator Expressions: Page 27"""
symbols = '#$%@!'
print(tuple(ord(symbol) for symbol in symbols))
# (35, 36, 37, 64, 33)

import array
print(array.array('I', (ord(symbol) for symbol in symbols)))
# array('I', [35, 36, 37, 64, 33])

# us generator expressions to initialize sequences other than lists
# or to prodcue output that you don't need to keep in memory
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

"""Tuples are not just Immutable Lists: Page 28"""
# Tuples hold records: each item in tuple holds data for one field and position gives its meaning
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), 
    ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
# BRA/CE342567
# ESP/XDA205856
# USA/31195855

# "unpacking" items of tuple separately
for country, _ in traveler_ids:
    print(country)

# USA
# BRA
# ESP

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # tuple unpacking

# using * to grab excess items
a, b, *rest = range(5)
print(a, b, rest) # 0 1 [2, 3, 4]

a, b, *rest = range(3)
print(a, b, rest) # 0 1 [2]

a, b, *rest = range(2)
print(a, b, rest) # 0 1 []

a, *body, c, d = range(5)
print(a, body, c, d) # 0 [1, 2] 3 4

# with a namedtuple, you can access fields by name or position
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo) 
# City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))

print(tokyo.population) # 36.933
print(tokyo.coordinates) # (35.689722, 139.691667) 
print(tokyo[1]) # JP
print(City._fields) # ('name', 'country', 'population', 'coordinates')
print(tokyo._asdict())
# OrderedDict([('name', 'Tokyo'), ('country', 'JP'), ('population', 36.933), ('coordinates', (35.689722, 139.691667))])

# assigning to slcies
l = list(range(10))
l[2:5] = [100]
print(l) # [0, 1, 100, 5, 6, 7, 8, 9]

# Building lists of lists
board = [['_'] * 3 for i in range(3)]
print(board) # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'X' 
print(board) # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]

l = [1, 2, 3]
l *= 2
print(l) # [1, 2, 3, 1, 2, 3]