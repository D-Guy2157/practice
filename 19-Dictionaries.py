# dictionary = A changeable, unordered collection of unique key: value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Las Vegas',  # Intentionally wrong
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Washington DC'})  # Fixes Las Vegas
# capitals.pop('China')  # Removes a key+value
# capitals.clear()  # Clears the dictionary

# print(capitals['Moon'])  # Throws an error since moon isn't a key
print(capitals.get('Moon'))  # Returns None but no error so .get is much safer
print(capitals.get('Russia'))
print(capitals.keys())  # Prints all keys
print(capitals.values())  # Prints all values
print(capitals.items())  # Prints whole dictionary

for key, value in capitals.items():  # This for loop prints whole dictionary with a line for each
    print(key, value)
