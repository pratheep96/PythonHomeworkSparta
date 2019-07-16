# For loops - using dictionaries / hashes

# Syntax
# for <placeholder> in  <dict>:
    # run block of code

# dict_data = {
#     'name': 'Branson',
#     'money': 200
# }
#
# # We use the key to access the values of our dictionary
# # print(dict_data['name'])
#
# for key_placeholder in dict_data:
#     #When we iterate over a hash/dictionary
#     # the placeholder, holds an individual key during each iteration
#     print(key_placeholder) # THIS is the key
#     value = dict_data[key_placeholder] #User key and dictionary to extra individual value of key
#     print(value)
#
# dict_data = {
#     'name': 'Branson',
#     'money': 200
# }
#
# for key_placeholder in dict_data:
#     print(key_placeholder + ':', dict_data[key_placeholder])

embeded_dict_data = {
    1: {
    'name': 'Branson',
    'money': 200
    },
    2: {
    'name': 'Tania',
    'money': 300
    },
    3: {
    'name': 'Tyler',
    'money': 400
    }
}

#for key in embeded_dict_data:
#    print (key)

for item in embeded_dict_data.values():
    print(item)
    print(type(item))