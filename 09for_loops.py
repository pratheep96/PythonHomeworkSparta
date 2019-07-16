# For loops in Python
# Used to iterate over collections, lists and dictionaries

# Syntax
# for <placeholder> in  <list>: #placeholder is an internal variable that it's scope is limited to the loop
    # run block of code

# x_crazy_landlords = ['Cruella de Vill', 'Donald Duck', 'Popeye']
#
# for landlord in x_crazy_landlords:
#     print('hello')
#     breakpoint()
#

# Exercise 1
# Print the name of our landlords with nice formatting
# Listing them using numbers
#
# x_crazy_landlords = ['Cruella de Vill', 'Donald Duck', 'Popeye']
#
# counter = 1
# for land_lord in x_crazy_landlords:
#     print(counter, '-', land_lord)
#     counter += 1

## Further Loops

# list_data = [1, 2, 3, 4, 5]
# embeded_list = [[1,2,3],[5,6,7]]
#
# #for num in list_data:
# #    print(num)
#
# for data in embeded_list:
#     print(data)
#     print(type(data))
#     data_set = [1,2,3]
#     for number in data_set:
#         print (number)

# sparta_list_names = ['Zaid', 'Pratheep', 'Ally', 'Mujee', 'Adam', 'Shav', 'Julian', 'Matt', 'Omid', 'Humza', 'Payal', 'Michael', 'Naila', 'Humza', 'Daniel']
# embeded_list = [['Zaid', 'Ally', 'Mujee', 'Adam', 'Shav', 'Julian', 'Pratheep'], ['Omid', 'Matt', 'Payal', 'Michael', 'Naila', 'Humza', 'Daniel']]
#
# for name in sparta_list_names:
#     print ('If your name is ' + name + ' nobody likes you')

# list_scores = [1, 10, 3, 4, 5, 6]
#
# for num in list_scores:
#     result_percent = num / 10 * 100
#     print(result_percent)

list_embeded_scores = [[10,5,2], [3,4,6]]

# for ind_list in list_embeded_scores:
#     print(ind_list)
#     for num in ind_list:
#         print(num * 2)