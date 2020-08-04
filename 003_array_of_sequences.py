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