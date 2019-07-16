# Our Bread Factory

def make_dough(ingridient1, ingridient2):
    if 'wheat' in ingridient1 and 'water' in ingridient2:
        return 'dough'
    else:
        return 'wrong ingridients'

def bake_bread(semi_product):
    if semi_product == 'dough':
        return 'bread'
    else:
        return 'wrong ingridients'

print(make_dough('wheat', 'water'))
print(make_dough('cement', 'water'))

# #Tests
# print('call function make_dough, expect dough to be returned')
# print(make_dough('wheat', 'water')  == 'dough')
#
# print('call function make_dough with wrong ingridients. Expect it to return wrong ingridients')
# print(make_dough('cement', 'water') == 'wrong ingridients')
#
# print('call function bake_bread, expect bread to be returned')
# print(bake_bread('dough') == 'bread')
#
# print('called function bake_bread wiht wrong ingridients. expect outcome to be wrong ingridients')
# print(bake_bread('chocolate cement') == 'wrong ingridients')